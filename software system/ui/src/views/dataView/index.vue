<template>
  <div>
    <div class="main-layout">
      <el-select v-model="value"
                 class="m-2"
                 placeholder="Select"
                 style="width: 240px">
        <el-option v-for="item in options"
                   :key="item.value"
                   :label="item.label"
                   :value="item.value" />
      </el-select>
      <el-header style="background-color: #409EFF;height: 110px; display: flex; align-items: center; justify-content: center;border-radius:10px; ">
        <!-- <h1 class="head-title">地球表层系统开放数据挖掘关联及共享工具集-分析报告</h1> -->
        <h1 class="head-title">Earth Surface System Open Data Mining Linkage and Sharing Toolset - Monthly Analysis Report</h1>
      </el-header>
      <el-main>
        <div class="title-wrapper">
          <h3 class="section-title"><span>| </span>Introduction </h3>
          <!-- <h3 class="section-title"><span>| </span>报告简介</h3> -->
        </div>
        <el-row :gutter="20">
          <el-col :span="24">
            <el-card shadow="always">
              <div class="report-introduction">
                <!-- <p>
                                    &nbsp;&nbsp;地球表层科学数据是研究地球表层系统的重要资源，包含了大量关于地球表层的各种数据，如地形地貌数据、气象数据、地质数据、生态环境数据等。这些数据的分析和挖掘对于地球科学研究、环境保护、资源管理和决策制定具有重要意义。
                                </p>
                                <p>
                                    &nbsp;&nbsp;本报告旨在通过对地球表层科学数据的元数据分析、关联网络分析和数据质量评价分析，揭示其中的潜在信息和关联关系，为相关领域的研究和应用提供有益的支持和指导。
                                </p>
                                <p>
                                    &nbsp;&nbsp;<strong>元数据分析：</strong>我们将对地球表层科学数据的元数据进行深入分析，包括数据来源和可靠性分析、数据采集和处理方法分析、数据的时空特征分析等，以揭示数据的基本信息和质量，并为后续的数据挖掘和分析提供基础。
                                </p>
                                <p>
                                    &nbsp;&nbsp;<strong>关联网络分析：</strong>我们将基于地球表层科学数据的关联关系，构建关联网络模型，并进行网络分析和挖掘。通过分析关联网络的拓扑结构、节点属性和边权重等，我们可以揭示数据之间的关联模式、关键节点和重要路径，为地球表层系统的动态变化和相互作用提供深入理解。
                                </p>
                                <p>
                                    &nbsp;&nbsp;<strong>数据质量评价分析：</strong>我们将对地球表层科学数据的质量进行评价和分析，包括数据的准确性、完整性、一致性、时效性等方面。通过数据质量评价分析，我们可以发现数据存在的问题和潜在的误差，提出数据质量改进的措施和建议，以确保数据的可信度和有效性。
                                </p>
                                <p>
                                    &nbsp;&nbsp;通过对地球表层科学数据的元数据分析、关联网络分析和数据质量评价分析，本报告旨在揭示数据中的潜在信息和关联关系，为地球科学研究、环境保护、资源管理和决策制定提供有益的支持和指导。我们相信，对于地球表层科学数据的深入分析和挖掘将为我们更好地理解和保护地球表层系统提供重要的科学依据和决策支持。
                                </p> -->
                <p>
                  &nbsp;&nbsp;Earth surface scientific data is an important resource for the study of the Earth's surface system and contains a large amount of various data about the Earth's surface, such as topographic and geomorphologic data, meteorological data, geological data, ecological and environmental data and so on. The analysis and mining of these data are of great significance for geoscientific research, environmental protection, resource management and decision-making.

                  Translated with www.DeepL.com/Translator (free version)。
                </p>
                <p>
                  &nbsp;&nbsp;This report aims to reveal the potential information and correlations in the Earth's surface scientific data through metadata analysis, correlation network analysis and data quality evaluation analysis, so as to provide useful support and guidance for research and application in related fields.
                </p>
                <p>
                  &nbsp;&nbsp;<strong>metadata analysis:&nbsp;</strong>We will conduct an in-depth analysis of the metadata of the Earth's surface scientific data, including the analysis of data sources and reliability, the analysis of data acquisition and processing methods, and the analysis of the spatial and temporal characteristics of the data, in order to reveal the basic information and the quality of the data, and to provide the basis for subsequent data mining and analysis.
                </p>
                <p>
                  &nbsp;&nbsp;<strong>Correlation Network Analysis:&nbsp;</strong>We will construct an association network model based on the association relationships of the Earth's surface scientific data, and perform network analysis and mining. By analyzing the topology, node attributes and edge weights of the association network, we can reveal the association patterns, key nodes and important paths between the data, and provide an in-depth understanding of the dynamics and interactions of the Earth's surface system.
                </p>
                <p>
                  &nbsp;&nbsp;<strong>Data quality evaluation analysis:&nbsp;</strong>We will evaluate and analyze the quality of scientific data on the Earth's surface, including the accuracy, completeness, consistency and timeliness of the data. Through data quality evaluation and analysis, we can identify problems and potential errors in the data, and propose measures and recommendations for data quality improvement to ensure the credibility and validity of the data.
                </p>
                <p>
                  &nbsp;&nbsp;Through metadata analysis, association network analysis and data quality evaluation analysis of the Earth's surface scientific data, this report aims to reveal the potential information and association relationships in the data, and provide useful support and guidance for Earth science research, environmental protection, resource management and decision-making. We believe that in-depth analysis and excavation of the Earth's surface scientific data will provide an important scientific basis and decision-making support for better understanding and protection of the Earth's surface system.
                </p>
              </div>

            </el-card>
          </el-col>
        </el-row>
        <div class="title-wrapper">
          <h3 class="section-title"><span>| </span>Toolset Analysis</h3>
          <!-- <h3 class="section-title"><span>| </span>工具集分析</h3> -->
        </div>
        <el-row :gutter="20">
          <el-col :span="6">
            <el-card shadow="always"
                     style="height: 200px;">
              <h1 style="text-align: center;">Users in Total</h1>
              <div class="eye-catching-number"
                   style="background-color: #ff0000;">
                <span>149</span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always"
                     style="height: 200px;">
              <h1 style="text-align: center;">Active Users</h1>
              <div class="eye-catching-number"
                   style="background-color:#6699FF ;">
                <span>30</span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always"
                     style="height: 200px;">

              <h1 style="text-align: center;">New Users</h1>
              <div class="eye-catching-number"
                   style="background-color:#19CAAD ;">
                <span>12</span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always"
                     style="height: 200px;">
              <h1 style="text-align: center;">Unused Users</h1>
              <div class="eye-catching-number"
                   style="background-color:#D1BA74 ;">
                <span>11</span>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <!-- <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="16">
            <el-card shadow="always">
              <div class="card-title">Distribution of website</div>
              <mapModel></mapModel>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="always"
                     style="height: 561px;">
              <div class="card-title">Top website of Data number </div>
              <el-table :data="tableData"
                        height="100%"
                        style="width: 100%">
                <el-table-column prop="website"
                                 label="website"
                                 width="280" />
                <el-table-column prop="num"
                                 label="ration"
                                 width="100" />
                <el-table-column prop="ration"
                                 label="num" />
              </el-table>
            </el-card>
          </el-col>
        </el-row> -->
        <el-row :gutter="20"
                style="margin-top:40px; margin-bottom: 40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <!-- <div class="card-title">每周用户活跃量</div> -->
              <div class="card-title">Weekly User Activity</div>
              <lineChart ref="lineChart"
                         style="width: 100%; height: 460px; " />
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <!-- <div class="card-title">功能使用频率统计</div> -->
              <div class="card-title">Function Usage Frequency Statistics</div>
              <featureUsedChart ref="featureUsedChart"
                                style="width: 100%; height: 500px; " />
            </el-card>
          </el-col>
        </el-row>
        <div class="title-wrapper">
          <h3 class="section-title"><span>| </span>Metadata Analysis</h3>
          <!-- <h3 class="section-title"><span>| </span>元数据分析</h3> -->
        </div>
        <el-row :gutter="20"
                style="margin-top:20px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">Hot Search Terms</div>
              <!-- <div class="card-title">热点搜索词汇</div> -->
              <wordCloudChart />
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <!-- <div class="card-title">近一年数据变化量</div> -->
              <div class="card-title">Amount Of Change In Data Over The Last Year</div>
              <monthDataChart ref="monthDataChart"
                              style="width: 100%; height: 500px; " />
            </el-card>
          </el-col>
        </el-row>
        <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">Statistics By Theme</div>
              <!-- <div class="card-title">各主题数据统计</div> -->
              <themeChart ref="themeChart"
                          style="width: 100%; height: 500px; " />
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">Statistics On Data Sources</div>
              <!-- <div class="card-title">数据来源统计</div> -->
              <originChart ref="originChart"
                           style="width: 100%; height: 500px; " />
            </el-card>
          </el-col>
        </el-row>
        <!-- <div class="title-wrapper">
          <h3 class="section-title"><span>| </span>关联数据分析</h3>
        </div>
        <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">热点搜索词汇</div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">近一年数据变化量</div>
            </el-card>
          </el-col>
        </el-row>
        <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">各主题数据统计</div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">数据来源统计</div>
            </el-card>
          </el-col>
        </el-row>
        <div class="title-wrapper">
          <h3 class="section-title"><span>| </span>数据质量评价分析</h3>
        </div>
        <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">热点搜索词汇</div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">近一年数据变化量</div>
            </el-card>
          </el-col>
        </el-row>
        <el-row :gutter="20"
                style="margin-top:40px;">
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">各主题数据统计</div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="always"
                     style="height: 500px;">
              <div class="card-title">数据来源统计</div>
            </el-card>
          </el-col>
        </el-row> -->
      </el-main>

    </div>
    <!-- <el-button class="pdfDownload" @click="getPdf('自定义文件名', '.main-layout')"> -->
    <div class="pdfDownload"
         @click="open()"><svg t="1708660370701"
           class="icon"
           viewBox="0 0 1365 1024"
           version="1.1"
           xmlns="http://www.w3.org/2000/svg"
           p-id="4267"
           width="48"
           height="48">
        <path d="M513.877333 0h120.448c21.632 0 32.384 10.624 32.384 32v510.72c0 21.376-10.752 32-32.384 32h-120.448c-21.632 0-32.384-10.624-32.384-32v-510.72c-0.128-21.376 10.752-32 32.384-32z m0 0"
              fill="#13227a"
              p-id="4268"></path>
        <path d="M893.525333 567.68L607.061333 851.2c-18.048 17.28-46.72 17.28-64.768 0L254.677333 567.68c-13.184-13.312-17.152-33.152-9.856-50.432C251.989333 499.968 268.885333 488.576 287.829333 488.32h572.672c18.944 0.256 35.712 11.648 43.008 28.928 7.04 17.28 3.2 37.12-9.984 50.432zM1018.453333 1024H129.621333c-38.272-3.584-67.584-35.328-67.584-73.344 0-38.016 29.312-69.76 67.584-73.216h888.832c38.272 3.584 67.584 35.328 67.584 73.216 0 38.016-29.184 69.76-67.584 73.344z m0 0"
              fill="#13227a"
              p-id="4269"></path>
      </svg>
    </div>
    <!-- </el-button> -->
  </div>
</template>
  
<script>
import mapModel from './mapModel.vue';
import wordCloudChart from '../dataMap/component/wordCloudChart.vue';
import monthDataChart from '../dataMap/component/monthDataChart.vue';
import themeChart from '../dataMap/component/themeChart.vue';
import originChart from '../dataMap/component/originChart.vue';
import lineChart from './lineChart.vue';
import featureUsedChart from './featureUsedChart.vue'
export default {

  data () {
    return {
      value: 'Month',
      options: [
        {
          value: 'Month',
          label: 'Month',
        },
        {
          value: 'Quarter',
          label: 'Quarter',
        },
        {
          value: 'Year',
          label: 'Year',
        }],
      tableData: [
        {
          website: '中国地球科学数据共享网',
          ration: '10%',
          num: '10',
        },
        {
          website: '中国科学院地理科学与资源研究所',
          ration: '10%',
          num: '9',
        },
        {
          website: 'NOAA NCEI',
          ration: '10%',
          num: '8',
        },
        {
          website: 'WorldClim',
          ration: '10%',
          num: '7',
        },
        {
          website: 'Brazil Data Cube',
          ration: '10%',
          num: '6',
        },
        {
          website: 'Geoscience Australia',
          ration: '10%',
          num: '5',
        },
        {
          website: 'Earthdata Search',
          ration: '10%',
          num: '4',
        },
        {
          website: 'Copernicus Open Access Hub',
          ration: '10%',
          num: '3',
        },
        {
          website: 'OpenStreetMap',
          ration: '10%',
          num: '2',
        },
        {
          website: 'NASA EOSDIS',
          ration: '10%',
          num: '1',
        },
      ]
    }
  },
  components: {
    mapModel,
    wordCloudChart,
    monthDataChart,
    themeChart,
    originChart,
    lineChart,
    featureUsedChart
  },
  mounted () {
    this.$refs.monthDataChart.initChart();
    this.$refs.themeChart.initChart();
    this.$refs.originChart.initChart();
    this.$refs.lineChart.initChart()
    this.$refs.featureUsedChart.initChart()
  },
  methods: {
    open () {
      const h = this.$createElement;
      this.$notify({
        title: '文件下载',
        message: h('i', { style: 'color: teal' }, 'pdf文件下载中，请稍后!!!'),
      });
      this.getPdf("地球表层系统开放数据挖掘关联及共享工具集-数据分析报告", ".main-layout")
    },
  }
};
</script>
  
<style>
.main-layout {
  background-color: #f5f7fa;
  padding: 20px;
}

.pdfDownload {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  position: absolute;
  top: 80px;
  right: 20px;
  z-index: 900;
}

.head-title {
  text-align: center;
  color: white;
  /*设置文字颜色*/
  text-shadow: 0 8px 10px #6699ff;
  /*设置文字阴影*/
  font-weight: bolder;
  /*设置文字宽度*/
}

.title-wrapper {
  display: flex;
  /*1. 设置宽度*/
  width: 100%;
  margin: 9px auto 9px auto;
}

.section-title {
  color: #6699ff;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-title {
  top: 20px;
  left: 30px;
  font-size: 16px;
  font-weight: bold;
}

.report-introduction {
  font-size: 17px;
  line-height: 2;
  text-align: justify;
}

.report-introduction p {
  margin-bottom: 10px;
}

.report-introduction strong {
  font-weight: bold;
}

.report-introduction em {
  font-style: italic;
}

.eye-catching-number {
  width: 100px;
  height: 80px;
  text-align: center;
  display: inline-block;
  position: relative;
  left: 200px;
  top: 20px;
  color: #ffffff;
  font-size: 48px;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
}
</style>
  