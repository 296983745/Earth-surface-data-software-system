<template>
    <div id="monthDatachart" style="width:100%;height:100%"></div>
</template>
<script>
import * as echarts from 'echarts';
import { getDataCatalogMonthStatistics } from '@/api/dataMap/dataMap'
export default {
    data() {
        return {
            myChart: null
        }
    },
    // mounted() {
    //     this.$nextTick(() => {
    //         this.initChart()
    //     })
    // },
    methods: {
        async initChart() {
            let response = await getDataCatalogMonthStatistics()
            let monthData = [];
            let addData = [];
            let updateData = [];
            if (response.code == 200) {
                let data = response.data
                data.forEach(item => {
                    monthData.push(item.month)
                    addData.push(item.add_data_count)
                    updateData.push(item.update_data_count)
                })
            } else {
                return;
            }
            var chartDom = document.getElementById('monthDatachart');
            this.myChart = echarts.init(chartDom);
            var option;
            option = {
                title: {},
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['新增数据', '更新数据']
                },
                toolbox: {
                    show: false,
                    feature: {
                        magicType: { show: true, type: ['line', 'bar'] },
                        restore: { show: true },
                        saveAsImage: { show: true }
                    }
                },
                calculable: true,
                xAxis: [
                    {
                        type: 'category',
                        // prettier-ignore
                        data: monthData
                    }
                ],
                yAxis: [
                    {
                        type: 'value'
                    }
                ],
                series: [
                    {
                        name: '新增数据',
                        type: 'bar',
                        data: addData,
                        markPoint: {
                            data: [
                                { type: 'max', name: 'Max' },
                                { type: 'min', name: 'Min' }
                            ]
                        },
                        markLine: {
                            data: [{ type: 'average', name: 'Avg' }]
                        }
                    },
                    {
                        name: '更新数据',
                        type: 'bar',
                        data: updateData,
                        markPoint: {
                            data: [
                                { type: 'max', name: 'Max' },
                                { type: 'min', name: 'Min' }
                            ]
                        },
                        markLine: {
                            data: [{ type: 'average', name: 'Avg' }]
                        }
                    }
                ]
            };
            option && this.myChart.setOption(option);
        }
    }
};

</script>