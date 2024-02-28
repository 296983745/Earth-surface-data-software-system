<template>
    <el-dialog :visible.sync="dialogVisible" append-to-body :title="this.web + this.title" :destroy-on-close="true">
        <el-row :gutter="23">
            <el-col :span="6" :xs="24" style="padding: 10px;">
                <div class="head-container">
                    <el-input placeholder="输入关键字" v-model="filterText" style="margin-bottom: 20px" />
                </div>
                <div class="head-container" style="overflow: auto; max-height:580px">
                    <el-tree
                        :data="treeData"
                        :props="defaultProps"
                        :expand-on-click-node="false"
                        :filter-node-method="filterNode"
                        ref="tree"
                        node-key="id"
                        default-expand-all
                        highlight-current
                        @node-click="handleNodeClick"
                    />
                </div>
            </el-col>
            <el-col :span="18" :xs="24" style="padding: 10px;">
                <el-form :model="queryParams" ref="queryForm" size="small" :inline="true">
                    <el-form-item label="名称" prop="name">
                        <el-input v-model="queryParams.name" placeholder="请输入名称" clearable style="width: 150px"
                            @keyup.enter.native="handleQuery" />
                    </el-form-item>
                    <el-form-item label="学科" prop="subject">
                        <el-input v-model="queryParams.subject" placeholder="请输入学科" clearable style="width: 150px"
                            @keyup.enter.native="handleQuery" />
                    </el-form-item>
                    <el-form-item label="来源" prop="subject" v-show="this.title == 'all'">
                        <!-- <el-input v-model="queryParams.subject" placeholder="请输入来源" clearable style="width: 120px"
                            @keyup.enter.native="handleQuery" /> -->
                        <el-select v-model="queryParams.origin" filterable placeholder="请选择" clearable style="width: 200px"
                            @change="handleQuery">
                            <el-option v-for="item in this.optionsData" :key="item.id" :label="item.value"
                                style="width: 200px" :value="item.name">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
                        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
                        <!-- <el-button icon="el-icon-coordinate" size="mini" @click="setTableDataMarker()">显示到地图</el-button>
                        <el-button icon="el-icon-delete" size="mini" @click="concelTableDataMarker()">取消地图显示</el-button> -->
                    </el-form-item>
                </el-form>
                <el-table v-loading="loading" height="630" :data="dataList" style="width: 100%" ref="multipleTable"
                    :row-key="getRowKey" @selection-change="handleSelectionChange">
                    <el-table-column fixed="left" type="selection" width="50" reserve-selection />
                    <el-table-column fixed="left" align="center" width="60" label="序号">
                        <template slot-scope="scope">
                            <span>{{ (queryParams.pageNum - 1) * queryParams.pageSize + scope.$index + 1 }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column fixed show-overflow-tooltip width="200" property="name" label="数据名称" />
                    <!-- <el-table-column show-overflow-tooltip property="coordinate" label="坐标" width="300" /> -->
                    <el-table-column show-overflow-tooltip property="subject" align="center" label="学科" width="100" />
                    <el-table-column show-overflow-tooltip align="center" property="mainWord" label="主题词" width="300" />
                    <el-table-column show-overflow-tooltip label="创建时间" align="center" width="300" prop="createTime">
                        <template slot-scope="scope">
                            <span>{{ parseTime(scope.row.createTime) }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column fixed="right" align="center" label="操作" width="120">
                        <template #default="scope">
                            <el-button @click="handleDetail(scope.row)">详情</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <pagination v-show="total > 0" :total="total" :page.sync="queryParams.pageNum"
                    :limit.sync="queryParams.pageSize" @pagination="getList" />
            </el-col>
        </el-row>
        <tableDetail :visible="showDataDetailsPopup" :data="selectedData" @closeDetail="closeDetail"></tableDetail>
    </el-dialog>
</template>
  
<script>
import { getDataCatalog } from '@/api/dataMap/dataMap'
import {dataEntityTreeSelect }from '@/api/dataNet/dataEntity'
import "@riophae/vue-treeselect/dist/vue-treeselect.css";
import tableDetail from './tableDetail.vue';
export default {
    data() {
        return {
            dialogVisible: false,
            loading: false,
            queryParams: {
                name: '',
                subject: '',
                origin: '',
                pageNum: 1,
                pageSize: 10,
            },
            title: "",
            total: 0,
            web: "数据网站：",
            dataList: [],
            defaultProps: {
                children: 'children',
                label: 'label',
            },
            multipleSelection: [],
            treeData: [],
            filterText: '',
            optionsData: [],
            showDataDetailsPopup: false,
            selectedData: {

            }
        }
    },
    computed: {
        tableKey() {
            return this.searchKeyword; // 用于刷新表格数据的关键字侦听
        }
    },
    watch: {
        filterText(val) {
            this.$refs.tree.filter(val);
        }
    },
    components: {
        tableDetail
    },
    methods: {
        openDialog(params) {
            this.title = params.name;
            if (params.name != 'all') {
                this.queryParams.origin = params.name;
            } else {
                this.queryParams.origin = ''
            }
            if (params.data) {
                this.$nextTick(function () {
                    params.data.forEach(row => {
                        this.$refs.multipleTable.toggleRowSelection(row, true);
                    })
                })
            }
            if (params.options) {
                this.optionsData = params.options
            }
            this.dialogVisible = true;
            this.getList();
            this.getDataEntityTree();
        },
          /** 查询部门下拉树结构 */
        getDataEntityTree() {
            dataEntityTreeSelect().then(response => {
                this.treeData = response.data;
            });
        },
        handleQuery() {
            this.getList();
        },
        getList() {
            this.loading = true
            getDataCatalog(this.queryParams).then(response => {
                this.dataList = response.rows;
                this.total = response.total;
                this.loading = false;
            }
            );
        },
        resetQuery() {
            this.resetForm("queryForm");
            if (this.title == 'all') {
                this.queryParams.origin = ''
            }
            this.handleQuery();
        },
        handleNodeClick(data) {
            // 处理节点点击事件
            console.log('点击了节点:', data);
        },
        // 树形数据过滤
        filterNode(value, data) {
            if (!value) return true;
            return data.label.indexOf(value) !== -1;
        },
        handleSelectionChange(val) {
            this.multipleSelection = val;
        },
        getRowKey(row) {
            return row.id
        },
        setTableDataMarker() {
            this.$emit('setTableDataMarker', this.multipleSelection)
        },
        concelTableDataMarker() {
            this.$refs.multipleTable.clearSelection()
            this.$emit('concelTableDataMarker')
        },
        handleDetail(data) {
            this.selectedData = {}
            this.showDataDetailsPopup = true;
            this.selectedData = data
        },
        closeDetail() {
            this.showDataDetailsPopup = false;
        }
    }
};
</script>
<style scoped>
.el-scrollbar {
    width: 218px !important;
}

.el-form-item {
    margin-right: 20px;
}

.el-form-item__label {
    width: 70px;
    font-weight: bold;
    font-size: 14px;
}

.el-form-item__content {
    margin-left: 80px;
}

/* Style the table */
.el-table__header-wrapper {
    background-color: #f5f6fa;
}

.el-table__body-wrapper {
    overflow: auto;
    max-height: 480px;
}

.el-table__row:hover {
    background-color: #f5f5f5;
}

.el-table__column--selection {
    width: 50px;
}

.el-table__column--selection .cell {
    text-align: center;
}

.el-table__column--selection .cell>.el-checkbox {
    margin: 0;
}

.el-table__column--selection.is-leaf .cell {
    padding-left: 16px;
}

.el-table__column--selection.is-leaf .cell .el-checkbox {
    margin-left: -16px;
}
</style>