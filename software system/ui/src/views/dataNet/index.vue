<template>
    <div>
        <div class="search-bar">
            <svg-icon class-name="search-icon" style="color: white;" icon-class="search" @click.stop="click" />
            <div class="search-container" v-show="show">
                <el-form size="medium" label-width="100px">
                    <el-row type="flex" justify="start" align="top">
                        <el-col :span="12">
                            <el-form-item label="关键词" prop="keyWord">
                                <el-input v-model="params.keyWord" placeholder="请输入关键词" clearable
                                    :style="{ width: '100%' }">
                                </el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="数据来源" prop="origin">
                                <el-select v-model="params.origin" placeholder="请选择数据来源" clearable
                                    :style="{ width: '100%' }">
                                    <el-option v-for="(item, index) in options" :key="index" :label="item.label"
                                        :value="item.value" :disabled="item.disabled"></el-option>
                                </el-select>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="12">
                            <el-form-item label="学科">
                                <el-select v-model="params.subject" placeholder="请选择学科" clearable
                                    :style="{ width: '100%' }">
                                    <el-option v-for="(item, index) in options" :key="index" :label="item.label"
                                        :value="item.value" :disabled="item.disabled"></el-option>
                                </el-select>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="规模">
                                <el-input-number style="width: 181px;" v-model="params.limit" placeholder="规模">
                                </el-input-number>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <el-form-item size="large">
                        <el-button style="margin-left: 90px;" icon="el-icon-search" type="primary"
                            @click="handleSearch">搜索</el-button>
                        <el-button @click="concel" icon="el-icon-refresh">重置</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
        <NetChart ref="NetChart" :dataList="dataList" style="position: absolute;width: 1920px;height: 100vh; z-index: 1;"
            v-loading="loading" element-loading-text="数据关联网络加载中....." @nodeClick="nodeClick" @edgeClick="edgeClick">
        </NetChart>
        <tableDetail :visible="showDataDetailsPopup" :recommendations="recommendation" :data="selectedData"
            @closeDetail="closeDetail" />
        <relationDetail :visible="showRelationDetail" @closeRelationDetail="closeRelationDetail" />
    </div>
</template>

<script>
import { getDataNet, getDataCatalogByName } from '../../api/dataNet/dataNet';
import NetChart from './NetChartModel.vue';
import tableDetail from '../dataMap/component/tableDetail.vue';
import relationDetail from './component/relationDetail.vue';
export default {
    data() {
        return {
            search: '',
            selectedCategory: '',
            show: false,
            dataList: {
                nodes: [],
                links: []
            },
            params: {
                keyWord: '',
                limit: 1000
            },
            options: [{
                value: '选项1',
                label: '黄金糕'
            }, {
                value: '选项2',
                label: '双皮奶'
            }, {
                value: '选项3',
                label: '蚵仔煎'
            }, {
                value: '选项4',
                label: '龙须面'
            }, {
                value: '选项5',
                label: '北京烤鸭'
            }],
            value: '',
            loading: false,
            selectedData: {},
            recommendation: [],
            showDataDetailsPopup: false,
            showRelationDetail: false
        }
    },
    components: {
        NetChart,
        tableDetail,
        relationDetail
    },
    created() {
    },
    mounted() {
        this.handleSearch();
    },
    methods: {
        async handleSearch() {
            this.loading = true;
            await this.getNetData(this.params);
            this.loading = false;
        },
        concel() {
            this.params = {}
        },
        async click() {
            this.show = !this.show
        },
        async getNetData(params) {
            this.dataList = {
                nodes: [],
                links: []
            };
            let response = await getDataNet(params);
            let data = response.data;
            let nodes = data.netNodeList;
            let relationships = data.relationships;
            nodes.forEach(item => {
                let node = {
                    x: item.x,
                    y: item.y,
                    id: item.id,
                    name: item.dataName,
                    symbolSize: item.size
                };
                this.dataList.nodes.push(node);
            });
            relationships.forEach(item => {
                let relationship = {
                    id: item.id,
                    source: item.startNode.id.toString(),
                    target: item.endNode.id.toString(),
                    relationName: item.relationName,
                    time: item.time,
                    space: item.space,
                    topic: item.topic,
                    label: {
                        formatter: item.relationName
                    }
                };
                this.dataList.links.push(relationship);
            });
            this.$refs.NetChart.initCharts(this.dataList);
        },
        // 网络图 节点点击事件
        nodeClick(data) {
            let query = {
                name: data.name
            }
            this.selectedData = {}
            getDataCatalogByName(query).then(response => {
                if (response.code == 200) {
                    this.showDataDetailsPopup = true;
                    this.selectedData = response.data.detail;
                    this.recommendation = response.data.relate;
                } else {
                    this.$message.error(response.msg);
                }
            })
        },
        /**
         * 网络图 边点击事件
         * @param {*} data 
         */
        edgeClick(data) {
            this.showRelationDetail = true;
            console.log(data);
        },
        closeDetail() {
            this.showDataDetailsPopup = false;
        },
        closeRelationDetail() {
            this.showRelationDetail = false;
        }
    }
};
</script>

<style scoped>
.el-loading-spinner {
    color: #409EFF;
}

.search-icon {
    cursor: pointer;
    font-size: 18px;
    vertical-align: middle;
    margin: 80px;
}

.el-input {
    width: 300px;
    margin-right: 20px;
}

.el-loading-spinner {
    color: #409EFF;
}

.search-bar {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
}

.search-container {
    position: absolute;
    top: 90px;
    left: 110px;
    width: 600px;
    height: auto;
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid #ccc;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    padding: 10px;
}
</style>