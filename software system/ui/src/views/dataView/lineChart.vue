<template>
    <div id="userActiveChart" style="width:100%;height:100%"></div>
</template>
<script>
import * as echarts from 'echarts';
export default {
    data() {
        return {
            chart: null,
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
            const pastDatesArray = this.getPastDates();
            const yArray = [];
            for (let i = 0; i < 7; i++) {
                yArray.push(
                    Math.floor(Math.random() * 10) + 10
                )
            }
            this.chart = echarts.init(document.getElementById('userActiveChart'))
            var option = {
                tooltip: {
                    trigger: 'axis'
                },
                grid: {
                    left: '5%',
                    right: '15%',
                    bottom: '10%'
                },
                xAxis: {
                    data: pastDatesArray
                },
                yAxis: {},
                // toolbox: {
                //     right: 10,
                //     feature: {
                //         dataZoom: {
                //             yAxisIndex: 'none'
                //         },
                //         restore: {},
                //         saveAsImage: {}
                //     }
                // },
                visualMap: {
                    top: 50,
                    right: 10,
                    pieces: [
                        {
                            gt: 0,
                            lte: 5,
                            color: '#93CE07'
                        },
                        {
                            gt: 5,
                            lte: 10,
                            color: '#FBDB0F'
                        },
                        {
                            gt: 10,
                            lte: 15,
                            color: '#FC7D02'
                        },
                        {
                            gt: 15,
                            lte: 20,
                            color: '#FD0100'
                        },
                        {
                            gt: 20,
                            lte: 25,
                            color: '#AA069F'
                        },
                        {
                            gt: 30,
                            color: '#AC3B2A'
                        }
                    ],
                    outOfRange: {
                        color: '#999'
                    }
                },
                series: {
                    type: 'line',
                    data: yArray,
                    markLine: {
                        silent: true,
                        lineStyle: {
                            color: '#333'
                        },
                        data: [
                            {
                                yAxis: 50
                            },
                            {
                                yAxis: 100
                            },
                            {
                                yAxis: 150
                            },
                            {
                                yAxis: 200
                            },
                            {
                                yAxis: 300
                            }
                        ]
                    }
                }
            }
            option && this.chart.setOption(option);
        },
        getPastDates() {
            const pastDates = [];
            const today = new Date();
            // 循环获取过去7天的日期
            for (let i = 0; i < 7; i++) {
                const pastDate = new Date(today);
                pastDate.setDate(today.getDate() - i);
                pastDates.push(pastDate.toLocaleDateString());
            }

            return pastDates;
        }
    }
};

</script>