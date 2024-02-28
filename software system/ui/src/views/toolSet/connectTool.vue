<template>
    <div class="page-container">
        <div class="header-container">
            <img style="width: 50px;margin-right: 20px;" src="../../image/connect.png" alt="Evaluation" />
            <h4 class="title">执行一次新的关联</h4>
        </div>
        <div class="body-container">
            <el-form ref="form" :model="sizeForm" :rules="rules" label-width="150px" size="medium ">
                <h4 style="width:800px;margin-bottom: 20px; text-align: left;">1.选择需要进行计算的属性。
                </h4>
                <el-select v-model="sizeForm.indicators" placeholder="请选择你需要进行计算的属性"
                    style="margin-bottom: 20px; display: flex;">
                    <el-option label="时间" value="time"></el-option>
                    <el-option label="空间" value="space"></el-option>
                    <el-option label="主题" value="topic"></el-option>
                    <el-option label="全部属性" value="all"></el-option>
                </el-select>
                <!-- <el-input type="textarea" :rows="3" placeholder="" v-model="sizeForm.indicators" readonly
                    style="margin-bottom: 20px; display: flex;">
                </el-input> -->
                <h4 style="margin-bottom: 20px; text-align: left;">2. 上传你要计算的数据集。<el-tooltip class="item" effect="light"
                        placement="top">
                        <div slot="content">最好的办法是使用URL，又称URI，因为它是最标准<br />
                            、最明确的在线资源识别协议。
                        </div>
                        <i class="el-icon-question" />
                    </el-tooltip>
                </h4>
                <FileUpload></FileUpload>
                <el-button type="primary" icon="el-icon-wifi" @click="onSubmit">开始计算</el-button>
                <el-button type="primary" icon="el-icon-wifi" @click="cancel">取消</el-button>
                <h3 v-show="this.start" v-loading="loading" element-loading-text="数据评估中....."
                    element-loading-svg-view-box="-10, -10, 50, 50" element-loading-background="rgba(122, 122, 122, 0.8)"
                    style="margin-top: 20px;">An evaluation can take up to 1 minute depending on the URL evaluated,<br />
                    and
                    the collection used.If you
                    leave this page the evaluation will not stop,<br />and you will be able to find it in the list below
                    when it
                    is done.</h3>
                <!-- <el-result v-show="resultShow" icon="success" title="Success" subTitle="">
                    <template slot="extra">
                        <el-button type="primary" size="medium">查看本次评价结果</el-button>
                    </template>
                </el-result> -->
            </el-form>
        </div>
        <div class="header-container">
            <img style="width: 50px;margin-right: 20px;" src="../../image/connect_result.png" alt="Evaluation" />
            <h4 class="title">最近的关联记录</h4>
        </div>
        <div class="table-container">
            <el-table v-loading="tableLoading" :data="tableData" height="400" border style="width: 100%">
                <el-table-column fixed="left" label="操作" width="150">
                    <template slot-scope="scope">
                        <el-button @click="handleClick(scope.row)" type="text" size="small">详情</el-button>
                        <el-button type="text" size="small"></el-button>
                        <el-button @click="handleClick(scope.row)" type="text" size="small">查看关联网络</el-button>

                    </template>
                </el-table-column>
                <el-table-column prop="evaluateTime" label="构建时间" width="160">
                </el-table-column>
                <el-table-column prop="url" label="数据集名称">
                </el-table-column>
                <el-table-column prop="score" label="得分" width="80">
                </el-table-column>
            </el-table>
        </div>
        <evaluteResult :visible="showResult" :data="selectedData" @closeDetail="closeDetail"></evaluteResult>
    </div>
</template>
  
<script>
import evaluteResult from './evaluteResult.vue'
import FileUpload from '../../components/FileUpload/index.vue';
import { getLatestEvaluation, addEvaluation } from '../../api/evaluation/evaluate'
export default {
    data() {
        return {
            sizeForm: {
                indicators: '',
                url: this.$route.query.url ? this.$route.query.url : "",
            },
            loading: false,
            start: false,
            resultShow: false,
            tableData: [],
            showResult: false,
            selectedData: {},
            tableLoading: false,
            total: 0,
            queryParams: {
                pageNum: 1,
                pageSize: 10
            },
        }
    },
    components: {
        evaluteResult,
        FileUpload
    },
    created() {
        this.getTableData();
    },
    methods: {
        // 开始执行
        onSubmit() {
            if (!this.sizeForm.url) {
                const h = this.$createElement;
                this.$message({
                    message: h('p', null, [
                        h('span', null, '指标集合 '),
                        h('i', { style: 'color: red' }, '不能为空!')
                    ])
                });
                return;
            }
            if (!this.sizeForm.indicators) {
                const h = this.$createElement;
                this.$message({
                    message: h('p', null, [
                        h('span', null, 'url '),
                        h('i', { style: 'color: red' }, '不能为空!')
                    ])
                });
                return;
            }
            this.start = true;
            this.loading = true;
            addEvaluation(this.sizeForm).then(response => {
                if (response.code == 200) {
                    this.$modal.msgSuccess("计算成功");
                    this.selectedData = response.data
                    this.getTableData();
                    this.start = false;
                    this.loading = false;
                    this.showResult = true
                } else {
                    this.$modal.msgSuccess("计算失败！请重试！");
                    this.start = false;
                    this.loading = false;
                }
            });
        },
        cancel() {
            this.start = false;
            this.loading = false;
        },
        handleClick(data) {
            this.selectedData = data
            this.showResult = true
        },
        closeDetail() {
            this.showResult = false
        },
        getTableData() {
            let query = this.queryParams
            this.tableLoading = true
            getLatestEvaluation(query).then(response => {
                if (response.code === 200) {
                    this.tableData = response.rows
                    this.total = response.total
                } else {

                }
                this.tableLoading = false;
            })
        }
    },
}
</script>
  
<style scoped>
.page-container {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 20px;
    margin: 20px;
    text-align: center;
    background-color: #f1f1f1 !important;
    height: calc(100vh - 90px);
}

.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.body-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.title {
    float: left;
    margin: 0px;
    font-family: "Open Sans", Roboto, Arial;
    font-weight: 400;
    font-size: 2rem;
    line-height: 1.235;
}

.table-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    width: 800px;
    margin: 0 auto;
    text-align: center;
}
</style>
  