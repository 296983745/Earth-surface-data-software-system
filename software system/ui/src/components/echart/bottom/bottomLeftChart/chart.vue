<template>
    <div>
        <Echart :options="options" id="bottomLeftChart" height="420px" width="100%"></Echart>
    </div>
</template>

<script>
import Echart from '@/common/echart'
import * as echarts from 'echarts';
export default {
    data() {
        return {
            options: {},
        };
    },
    components: {
        Echart,
    },
    props: {
        cdata: {
            type: Object,
            default: () => ({})
        },
    },
    watch: {
        cdata: {
            handler(newData) {
                this.options = {
                    tooltip: {
                        trigger: "axis",
                        backgroundColor: "rgba(255,255,255,0.1)",
                        axisPointer: {
                            type: "shadow",
                            label: {
                                show: true,
                                backgroundColor: "#7B7DDC"
                            }
                        }
                    },
                    legend: {
                        data: ["新增数据", "更新数据"],
                        textStyle: {
                            color: "#B4B4B4"
                        },
                        top: "0%"
                    },
                    grid: {
                        x: "8%",
                        width: "88%",
                        y: "4%"
                    },
                    xAxis: {
                        data: [
                            "2022-07",
                            "2022-08",
                            "2022-09",
                            "2022-10",
                            "2022-11",
                            "2022-12",
                            "2023-01",
                            "2023-02",
                            "2023-03",
                            "2023-04",
                            "2023-05",
                            "2023-06"
                        ],
                        axisLine: {
                            lineStyle: {
                                color: "#B4B4B4"
                            }
                        },
                        axisTick: {
                            show: false
                        }
                    },
                    yAxis: [
                        {
                            splitLine: { show: false },
                            axisLine: {
                                lineStyle: {
                                    color: "#B4B4B4"
                                }
                            },

                            axisLabel: {
                                formatter: "{value} "
                            }
                        },
                        {
                            splitLine: { show: false },
                            axisLine: {
                                lineStyle: {
                                    color: "#B4B4B4"
                                }
                            },
                            axisLabel: {
                                formatter: "{value} "
                            }
                        }
                    ],
                    series: [
                        {
                            name: "新增数据",
                            type: "bar",
                            barWidth: 10,
                            itemStyle: {
                                normal: {
                                    barBorderRadius: 5,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                        { offset: 0, color: "#956FD4" },
                                        { offset: 1, color: "#3EACE5" }
                                    ])
                                }
                            },
                            data: [
                                80,
                                99,
                                76,
                                88,
                                81,
                                82,
                                87,
                                85,
                                80,
                                84,
                                73,
                                15
                            ]
                        },
                        {
                            name: "更新数据",
                            type: "bar",
                            barGap: "-100%",
                            barWidth: 10,
                            itemStyle: {
                                normal: {
                                    barBorderRadius: 5,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                        { offset: 0, color: "rgba(156,107,211,0.8)" },
                                        { offset: 0.2, color: "rgba(156,107,211,0.5)" },
                                        { offset: 1, color: "rgba(156,107,211,0.2)" }
                                    ])
                                }
                            },
                            z: -12,
                            data: [
                                84,
                                86,
                                82,
                                71,
                                88,
                                83,
                                102,
                                80,
                                78,
                                77,
                                85,
                                20
                            ]
                        }
                    ]
                }
            },
            immediate: true,
            deep: true
        }
    }
}
</script>