<template>
    <el-dialog :visible.sync="dialogVisible" title="统计分析">
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="数据来源统计" name="first">
                <div ref="dataChart" style="width: 100%; height: 500px; "></div>
            </el-tab-pane>
            <el-tab-pane label="热点搜索词汇" name="second">
                <wordCloudChart />
            </el-tab-pane>
            <el-tab-pane label="近一年数据变化量" name="third">
                <monthDataChart ref="monthDataChart" style="width: 100%; height: 500px; " />
            </el-tab-pane>
            <el-tab-pane label="各主题数据统计" name="fourth">
                <themeChart ref="themeChart" style="width: 100%; height: 500px; " />
            </el-tab-pane>
        </el-tabs>


    </el-dialog>
</template>
<script>
// 折线堆叠图
import * as echarts from 'echarts';
import wordCloudChart from './wordCloudChart.vue';
import monthDataChart from './monthDataChart.vue';
import themeChart from './themeChart.vue';
import { getDataCatalogStatistics } from '@/api/dataMap/dataMap'
export default {
    props: {
    },
    data() {
        return {
            chart: null,
            dialogVisible: false,
            activeName: 'first'
        }
    },
    components: {
        wordCloudChart,
        monthDataChart,
        themeChart
    },
    mounted() {

    },
    beforeDestroy() {
        this.disposeChart()
    },
    created() {
    },
    methods: {
        handleClick(tab, event) {
            if (tab.name == 'third') {
                this.$refs.monthDataChart.initChart()
            }
            if (tab.name == 'fourth') {
                this.$refs.themeChart.initChart()
            }
        },
        openDialog() {
            this.dialogVisible = true;
            this.$nextTick(() => {
                this.drawChart();
            });
        },
        disposeChart() {
            if (!this.chart) {
                return
            }
            this.chart.dispose()
            this.chart = null
        },
        async drawChart() {
            let total = 0;
            let charts = [];
            let response = await getDataCatalogStatistics()
            if (response.code == 200) {
                let data = response.data
                data.forEach(item => {
                    total += item.count;
                    charts[item.origin] = item.count;
                })
            } else {
                return;
            }

            let charts1 = Object.keys(charts).map(function (key) { return charts[key]; })
            let charts2 = Object.keys(charts).map(function (key) { return total - charts[key]; })
            let charts3 = Object.keys(charts).map(function (key) {
                return {
                    name: key,
                    value: charts[key]
                };
            })
            this.chart = echarts.init(this.$refs.dataChart)
            let option = {
                tooltip: {},
                title: [
                    {
                        text: '数据目录',
                        subtext: '总计 ' + total,
                        left: '50%',
                        textAlign: 'center'
                    }
                ],
                xAxis: [
                    {
                        type: 'value',
                        max: total,
                        splitLine: {
                            show: false
                        }
                    }
                ],
                yAxis: [
                    {
                        type: 'category',
                        data: Object.keys(charts),
                        axisLabel: {
                            interval: 0,
                            rotate: 30,
                            fontSize: 8
                        },
                        splitLine: {
                            show: false
                        }
                    }
                ],
                series: [
                    {
                        type: 'bar',
                        stack: 'chart',
                        z: 3,
                        label: {
                            position: 'right',
                            show: true
                        },
                        data: charts1
                    },
                    {
                        type: 'bar',
                        stack: 'chart',
                        silent: true,
                        itemStyle: {
                            color: '#eee'
                        },
                        data: charts2
                    }
                ]
            }
            option && this.chart.setOption(option);
        }
    }
};

</script>
<style scoped>
.el-dialog {
    width: 800px;
    height: 800px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    margin: 0px !important;
}
</style>