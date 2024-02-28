<template>
    <div class="page-container">
        <el-col>
            <FileUpload></FileUpload>
        </el-col>
        <el-select v-model="selectedOption" placeholder="选择选项">
            <el-option v-for="option in options" :key="option" :label="option" :value="option"></el-option>
        </el-select>
        <el-button type="primary" @click="runProgram">运行程序</el-button>
        <div class="result-container">{{ result }}</div>
    </div>
</template>
  
<script>
import FileUpload from '../../components/FileUpload/index.vue';

export default {
    data() {
        return {
            files: [], // 数据文件列表
            selectedFile: '', // 当前选择的数据文件
            options: ['时间', '空间', '主题'], // 选项列表
            selectedOption: '', // 当前选择的选项
            result: '' // 返回的结果
        }
    },
    components: {
        FileUpload
    },
    methods: {
        // 获取数据文件列表
        fetchFiles() {
            // 调用后台API获取文件列表
            // 将文件列表赋值给this.files
        },
        // 运行程序
        runProgram() {
            // 调用后台API运行程序
            // 将返回的结果赋值给this.result
        }
    },
    mounted() {
        this.fetchFiles(); // 获取数据文件列表
    }
}
</script>
  
<style scoped>
.page-container {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 20px;
    margin: 20px;
    text-align: center;
}

.form-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.FileUpload {
    margin-right: 20px;
}

.el-select {
    width: 200px;
    margin-right: 20px;
}

.el-select__caret {
    color: #999;
}

.el-select__input {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 5px 30px 5px 10px;
    background-color: #fff;
    color: #333;
}

.el-select__tags-text {
    background-color: #eee;
    color: #666;
    border-radius: 4px;
    margin-right: 5px;
    padding: 2px 5px;
}

.el-button {
    border-radius: 4px;
    padding: 10px 20px;
    font-weight: bold;
    background-color: #409EFF;
    color: #fff;
}

.el-button:hover {
    background-color: #66b1ff;
}

.result-container {
    margin-top: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 20px;
    background-color: #f5f5f5;
    color: #333;
}
</style>
  