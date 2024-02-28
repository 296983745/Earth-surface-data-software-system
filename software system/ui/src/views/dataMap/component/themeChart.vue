<template>
    <div id="themeDatachart" style="width:100%;height:100%"></div>
</template>
<script>
import * as echarts from 'echarts';
import { getDataCatalogSubjectStatistics } from '@/api/dataMap/dataMap'
export default {
    data() {
        return {
            myChart: null,
            legendData: [],
            dataList: []
        }
    },
    // mounted() {
    //     this.$nextTick(() => {
    //         this.initChart()
    //     })
    // },
    methods: {
        async initChart() {
            let response = await getDataCatalogSubjectStatistics()
            if (response.code == 200) {
                this.dataList = response.data
                this.dataList.forEach(item => {
                    this.legendData.push(item.name)
                })
            } else {
                return;
            }
            let filteredDataList = this.dataList.slice(0, 10);
            var chartDom = document.getElementById('themeDatachart');
            this.myChart = echarts.init(chartDom);
            var option;
            option = {
                title: {
                    text: '数据主题前十占比统计',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                series: [{
                    name: '数据主题前十占比统计',
                    type: 'pie',
                    radius: ['50%', '75%'],
                    label: {
                        formatter: '{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                        // formatter: params => {
                        //     let text = params.name
                        //     let count = 8
                        //     let displayName = text.length < count
                        //         ? text : `${text.slice(0, count)}` + '...'

                        //     return `{hr|}\n{b|${displayName}}：{v|${params.value}}  {per|${params.percent} %}`
                        // },
                        backgroundColor: '#eee',
                        borderColor: '#aaa',
                        borderWidth: 1,
                        borderRadius: 4,
                        rich: {
                            a: {
                                color: '#999',
                                lineHeight: 22,
                                align: 'center'
                            },
                            hr: {
                                borderColor: '#aaa',
                                width: '100%',
                                borderWidth: 0.5,
                                height: 0
                            },
                            b: {
                                fontSize: 12,
                                lineHeight: 25
                            },
                            per: {
                                color: '#eee',
                                backgroundColor: '#334455',
                                padding: [2,
                                    4],
                                borderRadius: 2
                            }
                        }
                    },
                    data: filteredDataList
                }]
            };
            option && this.myChart.setOption(option);
        }
    }
};

</script>