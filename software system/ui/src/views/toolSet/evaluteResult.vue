<template>
  <el-dialog :visible="visible"
             title="数据评估详情"
             append-to-body
             :before-close="handleClose"
             width="60%">
    <el-row style="max-height: 700px;overflow: scroll;">
      <div class="score">
        <h4 class="url">{{ data.url }}</h4>
      </div>
      <div class="score">
        <img style="width: 50px;margin-right: 20px;"
             src="../../image/score.png"
             alt="Evaluation" />
        <h4 class="score_num">Evaluation score:{{ data.score }}</h4>
      </div>
      <div class="radar-chart">
        <div id="leida"
             style="height: 250px; width:350px ; "></div>
      </div>
      <el-col :span="24">
        <el-card>
          <el-collapse>
            <el-collapse-item name="Findable">
              <template #title
                        style="background-color: rgb(179, 229, 252);">
                <el-link @click="showDetails()">
                  <h4 style="font-size: 20px; background-color: rgb(179, 229, 252);">可发现性</h4>
                </el-link>
              </template>
              <el-table :data="findable"
                        height="357"
                        border
                        style="width: 100%;">
                <el-table-column prop="name"
                                 label="指标"
                                 width="200">
                </el-table-column>
                <el-table-column prop="des"
                                 label="描述">
                </el-table-column>
                <el-table-column label="检测通过"
                                 width="80">
                  <template slot-scope="scope">
                    <img v-if="scope.row.result == 1"
                         src="../../image/success.png">
                    <img v-if="scope.row.result == 0"
                         src="../../image/failure.png">
                  </template>
                </el-table-column>
              </el-table>
            </el-collapse-item>
          </el-collapse>
          <el-collapse>
            <el-collapse-item name="Findable">
              <template #title>
                <el-link @click="showDetails()">
                  <h4 style="font-size: 20px; background-color: rgb(255, 224, 178);">可获得性</h4>
                </el-link>
              </template>
              <el-table :data="accessible"
                        height="357"
                        border
                        style="width: 100%;">
                <el-table-column prop="name"
                                 label="指标"
                                 width="200">
                </el-table-column>
                <el-table-column prop="des"
                                 label="描述">
                </el-table-column>
                <el-table-column label="检测通过"
                                 width="80">
                  <template slot-scope="scope">
                    <img v-if="scope.row.result == 1"
                         src="../../image/success.png">
                    <img v-if="scope.row.result == 0"
                         src="../../image/failure.png">
                  </template>
                </el-table-column>
              </el-table>
            </el-collapse-item>
          </el-collapse>
          <el-collapse>
            <el-collapse-item name="Findable">
              <template #title>
                <el-link @click="showDetails()">
                  <h4 style="font-size: 20px; background-color: rgb(200, 230, 201)">可互操作性</h4>
                </el-link>
              </template>
              <el-table :data="interoperable"
                        height="357"
                        border
                        style="width: 100%;">
                <el-table-column prop="name"
                                 label="指标"
                                 width="200">
                </el-table-column>
                <el-table-column prop="des"
                                 label="描述">
                </el-table-column>
                <el-table-column label="检测通过"
                                 width="80">
                  <template slot-scope="scope">
                    <img v-if="scope.row.result == 1"
                         src="../../image/success.png">
                    <img v-if="scope.row.result == 0"
                         src="../../image/failure.png">
                  </template>
                </el-table-column>
              </el-table>
            </el-collapse-item>
          </el-collapse>
          <el-collapse>
            <el-collapse-item name="Findable">
              <template #title>
                <el-link @click="showDetails()">
                  <h4 style="font-size: 20px;    background-color: rgb(209, 196, 233)">可重用性</h4>
                </el-link>
              </template>
              <el-table :data="reusable"
                        height="357"
                        border
                        style="width: 100%;">
                <el-table-column prop="name"
                                 label="指标"
                                 width="200">
                </el-table-column>
                <el-table-column prop="des"
                                 label="描述">
                </el-table-column>
                <el-table-column label="检测通过"
                                 width="80">
                  <template slot-scope="scope">
                    <img v-if="scope.row.result == 1"
                         src="../../image/success.png">
                    <img v-if="scope.row.result == 0"
                         src="../../image/failure.png">
                  </template>
                </el-table-column>
              </el-table>
            </el-collapse-item>
          </el-collapse>
        </el-card>
      </el-col>
    </el-row>
  </el-dialog>
</template>
  
<script>
import * as echarts from 'echarts';
export default {
  name: "DataDetailsPopup",
  data () {
    return {
      score: 1 / 100,
      findable: [{
        name: '元数据标识符唯一性',
        des: '元数据被分配一个全局唯一的标识符，该指标用于评估元数据的标识符是否全局唯一，即没有两个相同的标识符来标识不同的元数据记录。',
        result: 1
      }, {
        name: '数据标识符唯一性',
        des: '数据被分配一个全局唯一的标识符。',
        result: 0
      }, {
        name: '元数据标识符持久性',
        des: '元数据被分配一个永久的标识符。持久标识符可确保元数据随着时间的推移保持可查找状态，并降低链接断开的风险。',
        result: 0
      },
      {
        name: '数据标识符持久性',
        des: '数据被分配一个永久的标识符',
        result: 1
      }],
      accessible: [
        {
          name: '元数据的永续性',
          des: '即使数据不再可用，元数据也是存在并可访问的，因为它包含对数据的IRI的明确引用。',
          result: 1
        }, {
          name: '访问限制性',
          des: '该指标是指允许请求者访问数字对象所需的信息。关于访问数据是否有限制即对数据的访问可能是开放的、限制的或关闭的。',
          result: 0
        }, {
          name: '数据人工干预性',
          des: '该指标是指请求者想要访问数字对象（数据）时所需的任何人工交互。可以通过在元数据中查找描述如何可通过人为干预获得对数字对象的访问的信息来评估该指标。',
          result: 0
        },
        {
          name: '数据验证访问性',
          des: '该指标要求对数字对象的访问进行身份验证和授权，并具体描述和充分记录数据可访问性。',
          result: 1
        }
      ],
      interoperable: [
        {
          name: '知识语言表现性',
          des: '数据使用正式的、可访问的、共享的和广泛适用的编程语言来表示知识。例如语言具有解析URL能力，具有BNF范式，以及是可拓展的语言。知识表示语言的例子有RDF、RDFS和OWL。',
          result: 1
        }, {
          name: 'FAIR词汇使用性',
          des: '数据使用遵循FAIR原则的词汇表，数据和数据的出处描述符应该使用本身就是FAIR的词汇和术语。',
          result: 0
        }, {
          name: '元数据、数据与其相关实体之间的链接性',
          des: '该指标是指数据与其相关实体是否链接，以便增加其重用能力。链接信息应作为元数据的一部分进行捕获。数据集可以链接到其先前版本、相关数据集或资源（例如出版物、实物样本、资助者、储存库、平台、站点或观测网络注册中心）。',
          result: 0
        },
        {
          name: '数据对其他元数据的引用性',
          des: '数据包括对其他（元数据）数据的合格引用。该指标是关于数据与其他数据连接的方式，例如链接到先前或相关的研究数据，为数据提供额外的上下文。',
          result: 1
        }
      ],
      reusable: [
        {
          name: '许可证机器可读性',
          des: '许可证不应是人类可读的文本，而应以机器可以处理的方式表达，而无需人工干预，例如在自动搜索中即可获取。',
          result: 1
        }, {
          name: '元数据的出处性',
          des: '该指标指元数据与详细来源相关联。该指标要求元数据包括有关数据来源的信息，即有关生成数据的来源、历史或工作流程，谁/什么/什么时候产生了数据的信息。',
          result: 0
        }, {
          name: '元数据领域标准符合性',
          des: '该指标要求元数据符合社区标准。即遵循目标领域相关的社区标准。',
          result: 0
        },
        {
          name: '数据格式领域符合性',
          des: '该指标指数据以目标研究领域推荐的文件格式提供。文件格式是指对数字信息进行编码的方法。例如，CSV用于表格数据，NetCDF用于多维数据，数据应以研究领域支持的文件格式提供，以实现数据共享和重用。',
          result: 1
        }
      ],
      leidaData: []
    }
  },
  props: {
    visible: {
      type: Boolean,
      required: true,
    },
    data: {
      type: Object,
      required: false,
    },
  },
  watch: {
    data: {
      handler (newData) {
        const obj = JSON.parse(newData.result);
        this.leidaData = [];
        let count1 = 0;
        let count2 = 0;
        let count3 = 0;
        let count4 = 0;
        for (let i = 0; i < 4; i++) {
          this.findable[i].result = obj.findable[i]
          this.accessible[i].result = obj.accessible[i]
          this.interoperable[i].result = obj.interoperable[i]
          this.reusable[i].result = obj.reusable[i]
          if (obj.findable[i] == 1) {
            count1++;
          }
          if (obj.accessible[i] == 1) {
            count2++;
          }
          if (obj.interoperable[i] == 1) {
            count3++;
          }
          if (obj.reusable[i] == 1) {
            count4++
          }
        }
        this.leidaData.push(count1)
        this.leidaData.push(count2)
        this.leidaData.push(count3)
        this.leidaData.push(count4)
        this.$nextTick(() => {
          this.getChart()
        })
      }
    },
    immediate: true,
    deep: true
  },
  components: {
  },
  methods: {
    handleClose () {
      this.$emit("closeDetail");
    },
    showDetails (id) {
      this.$emit('show-details', id)
    },
    getChart () {
      var chartDom = document.getElementById('leida');
      var myChart = echarts.init(chartDom);
      var option = {
        radar: {
          shape: 'circle',
          indicator: [
            { name: 'findable', max: 4 },
            { name: 'accessible', max: 4 },
            { name: 'interoperable', max: 4 },
            { name: 'reusable', max: 4 },

          ]
        },
        series: [
          {
            name: '',
            type: 'radar',
            tooltip: {
              trigger: 'item'
            },
            label: {
              show: true
            },
            data: [
              {
                value: this.leidaData,
              }
            ]
          }
        ]
      };
      option && myChart.setOption(option);
    }

  },
};
</script>
  
<style scoped>
.score {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.url {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 80%;
  font-weight: bold;
  font-size: 1.5rem;
  line-height: 1.235;
}

.score_num {
  float: left;
  margin: 0px;
  font-family: 'Open Sans', Roboto, Arial;
  font-weight: 400;
  font-size: 2rem;
  line-height: 1.235;
}

.title_box {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.title {
  float: left;
  margin: 0px;
  font-family: 'Open Sans', Roboto, Arial;
  font-weight: 400;
  font-size: 2rem;
  line-height: 1.235;
}

.radar-chart {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
</style>