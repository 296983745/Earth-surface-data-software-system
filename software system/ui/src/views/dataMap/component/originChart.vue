<template>
    <div id="originChart" style="width:100%;height:100%"></div>
</template>
<script>
import * as echarts from 'echarts';
import { getDataCatalogStatistics } from '@/api/dataMap/dataMap'
export default {
    data() {
        return {
            chart: null,
            activeName: 'first'
        }
    },
    beforeDestroy() {
        this.disposeChart()
    },

    methods: {
        disposeChart() {
            if (!this.chart) {
                return
            }
            this.chart.dispose()
            this.chart = null
        },
        async initChart() {
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
            this.chart = echarts.init(document.getElementById('originChart'))
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