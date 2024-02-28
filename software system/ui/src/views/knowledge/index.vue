<template>
    <div class="earth-system">
        <div class="header">
            <h1>地球表层系统知识百科</h1>
        </div>
        <div class="content">
            <el-row :gutter="20" style="margin-top: 20px; height: 48%;">
                <el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/v1.jpg" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>{{ data1.name }}</p>
                            <p class="data-theme"><span class="bold-text">类别：</span>{{ data1.type }}</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openDetail(data1)">地球内部结构.mp4</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">简介：</span>
                                地球内部结构是指地球内<br />
                                结构。根据地震波在地下不同深<br />
                                度传播速度的变化，一般将地球<br />
                                内部分为三个同心球层：地核、<br />
                                地幔和地壳。中心层是地核；中<br />
                                间是地幔；外层是地壳。地壳与<br />
                                地幔之间由莫霍面界开，地幔与<br />
                                地核之间由古登堡面界开。
                            </p>

                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/v2.jpg" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>{{ data2.name }}</p>
                            <p class="data-theme"><span class="bold-text">类别：</span>{{ data2.type }}</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openDetail(data2)">地球表层系统概论.mp4</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">简介：</span>
                            </p>

                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/v3.png" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>{{ data3.name }}</p>
                            <p class="data-theme"><span class="bold-text">类别：</span>{{ data3.type }}</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openDetail(data3)">地球表层生物圈mp4</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">简介：</span>
                            </p>

                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <el-row :gutter="20" style="margin-top: 40px; height: 48%;">
                <el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/lunwen1.jpg" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>
                                A fundamental theorem<br /> for
                                eco-environmental surface <br />
                                modelling and its applications</p>
                            <p class="data-theme"><span class="bold-text">类别：</span>文献</p>
                            <p class="data-theme"><span class="bold-text">来源：</span>引用</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openPdf(data3)">FTEEM.pdf</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">摘要：</span>
                                我们提出了生态环境表面<br />
                                建模基本定理(FTEEM)，以便继<br />
                                地球表面系统建模基本定理<br />
                                (FTESM)之后更容易地应用于<br />
                                生态学和环境科学领域.
                            </p>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/lunwen2.jpg" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>
                                地球表层系统数据目录<br />关联网络构建研究及展望</p>
                            <p class="data-theme"><span class="bold-text">类别：</span>文献</p>
                            <p class="data-theme"><span class="bold-text">来源：</span>团队（待发表）</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openPdf(data5)">关联网络构建研究.pdf</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">摘要：</span>
                                关联网络可以为地表数据<br />
                                的开放和共享提供完整的解决方<br />
                                案。本文介绍了地表关联网络的<br />
                                发展现状、构建方法和构建内容<br />
                                设计。
                            </p>
                        </div>
                    </el-card>
                </el-col><el-col :span="8" style="height: 100%;">
                    <el-card style="height: 100%; margin: 10px;" shadow="always">
                        <img src="../../image/lunwen3.jpg" class="image">
                        <div class="data-info-container">
                            <p class="data-theme"><span class="bold-text">名称：</span>
                                地球表层科学数据共享程<br />度现状调研</p>

                            <p class="data-theme"><span class="bold-text">类别：</span>调研报告</p>
                            <p class="data-theme"><span class="bold-text">来源：</span>团队</p>
                            <p class="data-links">
                                <span class="bold-text">地址：</span><a
                                    style="color: blue;text-decoration: underline;cursor: pointer;"
                                    @click="openPdf(data6)">现状调研报告.pdf</a>
                            </p>
                            <p class="data-introduction">
                                <span class="bold-text">简介：</span>
                                国外研究机构和科研团<br />
                                体等已开发FAIR评估方法和指<br />
                                标体系，具有代表性的主要是<br />
                                Go FAIR Metric Group (GFMG)<br />
                                的FAIR通用指标框架。<br />
                            </p>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <detail ref="detail"></detail>
    </div>
</template>
  
<script>
import detail from './detail.vue'
export default {

    data() {
        return {
            data1: {
                name: "地球内部结构",
                type: "视频",
                url: "/static/v1.mp4"
            },
            data2: {
                name: "地球表层系统概论",
                type: "视频",
                url: "/static/v2.mp4"
            },
            data3: {
                name: "地球表层生物圈",
                type: "视频",
                url: "/static/v3.mp4"
            },
            data4: {
                name: "Afundamentaltheoremforeco-environmentalsurfacemodellinganditsapplications.pdf",
                url: "/static/lunwen1.pdf"
            },
            data5: {
                name: "地球表层系统数据目录关联网络构建研究及展望.pdf",
                url: "/static/lunwen2.pdf"
            },
            data6: {
                name: "地球表层科学数据共享程度现状调研.pdf",
                url: "/static/lunwen3.pdf"
            }
        }
    },
    components: {
        detail
    },
    methods: {
        openDetail(data) {
            this.$refs.detail.openDialog(data.url)
        },
        openPdf(data) {
            var a = document.createElement("a"); //创建一个<a></a>标签
            a.href = data.url; // 给a标签的href属性值加上地址，注意，这里是绝对路径，不用加 点.
            a.download = data.name; //设置下载文件文件名，这里加上.xlsx指定文件类型，pdf文件就指定.fpd即可
            a.style.display = "none"; // 障眼法藏起来a标签
            document.body.appendChild(a); // 将a标签追加到文档对象中
            a.click(); // 模拟点击了a标签，会触发a标签的href的读取，浏览器就会自动下载了
            a.remove(); // 一次性的，用完就删除a标签
        }
    }
}
</script>
  
<style scoped>
.earth-system {
    display: flex;
    flex-direction: column;
    height: calc(100vh-90px);
}

.header {
    display: flex;
    margin-top: 10px;
    flex-direction: row;
    align-items: center;
    padding: 20px;
    background-color: #409EFF;
    color: #FFFFFF;
}

.content {
    height: 800px;
}

.time {
    font-size: 13px;
    color: #999;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
}

.button {
    padding: 0;
    float: right;
}

.image {
    width: 313px;
    height: 340px;
    display: block;
    float: left;
}

.data-info-container {
    float: left;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-left: 20px;
}


.data-theme,
.data-links {
    margin-bottom: 10px;
    font-size: 16px;
}

.data-introduction {
    font-size: 16px;
    line-height: 30px;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}

.bold-text {
    font-weight: bold;
}
</style>