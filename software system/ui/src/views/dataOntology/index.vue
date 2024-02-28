<template>
    <div class="app-container">
        <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch">
            <el-form-item label="数据本体名称" prop="name">
                <el-input v-model="queryParams.name" placeholder="请输入本体名称" clearable
                    @keyup.enter.native="handleQuery" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
                <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
            </el-form-item>
        </el-form>

        <el-row :gutter="10" class="mb8">
            <el-col :span="1.5">
                <el-button type="primary" plain icon="el-icon-plus" size="mini" @click="handleAdd"
                    v-hasPermi="['system:dept:add']">新增</el-button>
            </el-col>
            <el-col :span="1.5">
                <el-button type="info" plain icon="el-icon-sort" size="mini" @click="toggleExpandAll">展开/折叠</el-button>
            </el-col>
            <right-toolbar :showSearch.sync="showSearch" @queryTable="getList"></right-toolbar>
        </el-row>

        <el-table v-if="refreshTable" v-loading="loading" :data="dataEntityList" row-key="entityId"
            :default-expand-all="isExpandAll" :tree-props="{ children: 'children', hasChildren: 'hasChildren' }">
            <el-table-column prop="name" label="本体名称" width="460"></el-table-column>
            <el-table-column prop="dataOrigin" label="来源" width="300"></el-table-column>
            <el-table-column label="创建时间" align="center" prop="createTime" width="200">
                <template slot-scope="scope">
                    <span>{{ parseTime(scope.row.createTime) }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="orderNum" label="排序" width="100"></el-table-column>
            <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
                <template slot-scope="scope">
                    <el-button size="mini" type="text" icon="el-icon-edit" @click="handleUpdate(scope.row)"
                        v-hasPermi="['system:dept:edit']">修改</el-button>
                    <el-button size="mini" type="text" icon="el-icon-plus" @click="handleAdd(scope.row)"
                        v-hasPermi="['system:dept:add']">新增</el-button>
                    <el-button v-if="scope.row.parentId != 0" size="mini" type="text" icon="el-icon-delete"
                        @click="handleDelete(scope.row)" v-hasPermi="['system:dept:remove']">删除</el-button>
                </template>
            </el-table-column>
        </el-table>

        <!-- 添加或修改本体对话框 -->
        <el-dialog :title="title" :visible.sync="open" width="600px" append-to-body>
            <el-form ref="form" :model="form" :rules="rules" label-width="80px">
                <el-row>
                    <el-col :span="24" v-if="form.parentId !== 0">
                        <el-form-item label="上级本体" prop="parentId">
                            <treeselect v-model="form.parentId" :options="dataEntityOptions" :normalizer="normalizer"
                                placeholder="选择上级本体" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <el-form-item label="本体名称" prop="name">
                            <el-input v-model="form.name" placeholder="请输入本体名称" />
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="显示排序" prop="orderNum">
                            <el-input-number v-model="form.orderNum" controls-position="right" :min="0" />
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <el-form-item label="数据来源" prop="dataOrigin">
                            <el-input v-model="form.dataOrigin" placeholder="请输入本体数据来源" />
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button type="primary" @click="submitForm">确 定</el-button>
                <el-button @click="cancel">取 消</el-button>
            </div>
        </el-dialog>
    </div>
</template>
  
<script>
import { listDataEntity, getDataEntity, delDataEntity, addDataEntity, updateDataEntity, listDataEntityExcludeChild } from "@/api/dataNet/dataEntity";
import Treeselect from "@riophae/vue-treeselect";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";

export default {
    name: "Dept",
    dicts: ['sys_normal_disable'],
    components: { Treeselect },
    data() {
        return {
            // 遮罩层
            loading: true,
            // 显示搜索条件
            showSearch: true,
            // 表格树数据
            dataEntityList: [],
            // 本体树选项
            dataEntityOptions: [],
            // 弹出层标题
            title: "",
            // 是否显示弹出层
            open: false,
            // 是否展开，默认全部展开
            isExpandAll: true,
            // 重新渲染表格状态
            refreshTable: true,
            // 查询参数
            queryParams: {
                name: undefined,
            },
            // 表单参数
            form: {},
            // 表单校验
            rules: {
                parentId: [
                    { required: true, message: "上级本体不能为空", trigger: "blur" }
                ],
                name: [
                    { required: true, message: "本体名称不能为空", trigger: "blur" }
                ],
                orderNum: [
                    { required: true, message: "显示排序不能为空", trigger: "blur" }
                ]
            }
        };
    },
    created() {
        this.getList();
    },
    methods: {
        /** 查询本体列表 */
        getList() {
            this.loading = true;
            listDataEntity(this.queryParams).then(response => {
                this.dataEntityList = this.handleTree(response.data, "entityId");
                this.loading = false;
            });
        },
        /** 转换本体数据结构 */
        normalizer(node) {
            if (node.children && !node.children.length) {
                delete node.children;
            }
            return {
                id: node.entityId,
                label: node.name,
                children: node.children
            };
        },
        // 取消按钮
        cancel() {
            this.open = false;
            this.reset();
        },
        // 表单重置
        reset() {
            this.form = {
                entityId: undefined,
                parentId: undefined,
                name: undefined,
                orderNum: undefined,
                dataOrigin: undefined
            };
            this.resetForm("form");
        },
        /** 搜索按钮操作 */
        handleQuery() {
            this.getList();
        },
        /** 重置按钮操作 */
        resetQuery() {
            this.resetForm("queryForm");
            this.handleQuery();
        },
        /** 新增按钮操作 */
        handleAdd(row) {
            this.reset();
            if (row != undefined) {
                this.form.parentId = row.entityId;
            }
            this.open = true;
            this.title = "添加本体";
            listDataEntity().then(response => {
                debugger
                this.dataEntityOptions = this.handleTree(response.data, "entityId");
            });
        },
        /** 展开/折叠操作 */
        toggleExpandAll() {
            this.refreshTable = false;
            this.isExpandAll = !this.isExpandAll;
            this.$nextTick(() => {
                this.refreshTable = true;
            });
        },
        /** 修改按钮操作 */
        handleUpdate(row) {
            this.reset();
            getDataEntity(row.entityId).then(response => {
                this.form = response.data;
                this.open = true;
                this.title = "修改本体";
                listDataEntityExcludeChild(row.entityId).then(response => {
                    this.dataEntityOptions = this.handleTree(response.data, "entityId");
                    if (this.dataEntityOptions.length == 0) {
                        const noResultsOptions = { entityId: this.form.parentId, name: this.form.parentName, children: [] };
                        this.dataEntityOptions.push(noResultsOptions);
                    }
                });
            });
        },
        /** 提交按钮 */
        submitForm: function () {
            this.$refs["form"].validate(valid => {
                if (valid) {
                    if (this.form.entityId != undefined) {
                        updateDataEntity(this.form).then(response => {
                            this.$modal.msgSuccess("修改成功");
                            this.open = false;
                            this.getList();
                        });
                    } else {
                        addDataEntity(this.form).then(response => {
                            this.$modal.msgSuccess("新增成功");
                            this.open = false;
                            this.getList();
                        });
                    }
                }
            });
        },
        /** 删除按钮操作 */
        handleDelete(row) {
            this.$modal.confirm('是否确认删除名称为"' + row.name + '"的数据项？').then(function () {
                return delDataEntity(row.entityId);
            }).then(() => {
                this.getList();
                this.$modal.msgSuccess("删除成功");
            }).catch(() => { });
        }
    }
};
</script>
  