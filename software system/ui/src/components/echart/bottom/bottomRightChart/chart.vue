<template>
    <div>
        <Echart :options="options" id="centreLeft1Chart" height="420px" width="100%"></Echart>
    </div>
</template>
  
<script>
import Echart from '@/common/echart'
import echarts from 'echarts' // 引入 Echarts 库

export default {
    data() {
        return {
            options: {},
            // 定义颜色
        }
    },
    components: {
        Echart
    },
    props: {
        cdata: {
            type: Object,
            default: () => ({})
        }
    },
    watch: {
        cdata: {
            handler() {
                this.options = {
                    legend: {
                        data: ['可发现', '可查找', '可互操作', '可重用'],
                        textStyle: { // 图例样式
                            fontSize: 14,
                        }
                    },
                    xAxis: {
                        data: ['0-0.25', '0.25-0.5', '0.5-075', '0.75-1'],
                        axisLine: { // 坐标轴样式
                            lineStyle: { color: '#999' }
                        },
                        axisLabel: {
                            color: '#666'
                        }
                    },
                    yAxis: {
                        name: '数据量',
                        axisLine: {
                            lineStyle: { color: '#999' }
                        },
                        axisTick: {
                            lineStyle: { color: '#999' }
                        },
                        axisLabel: {
                            color: '#666'
                        }
                    },
                    series: [
                        {
                            name: '可发现',
                            data: [100, 300, 1900, 2100],
                            type: 'bar',
                            shapeType: 'leftEchelon',
                            itemStyle: { // 系列样式
                                color: '#337ab7'
                            },
                            label: { // 标签样式
                                show: true,
                                position: 'top',
                                color: '#666'
                            }
                        },
                        {
                            name: '可查找',
                            data: [201, 499, 1600, 2300],
                            type: 'bar',
                            shapeType: 'rightEchelon',
                            itemStyle: {
                                color: '#5cb85c'
                            },
                            label: {
                                show: true,
                                position: 'top',
                                color: '#666'
                            }
                        }, {
                            name: '可互操作',
                            data: [800, 2600, 200, 100],
                            type: 'bar',
                            shapeType: 'leftEchelon',
                            itemStyle: {
                                color: '#f0ad4e'
                            },
                            label: {
                                show: true,
                                position: 'top',
                                color: '#666'
                            }
                        },
                        {
                            name: '可重用',
                            data: [1200, 2000, 400, 200],
                            type: 'bar',
                            shapeType: 'rightEchelon',
                            itemStyle: {
                                color: '#d9534f'
                            },
                            label: {
                                show: true,
                                position: 'top',
                                color: '#666'
                            }
                        }
                    ]
                }
                // 使用 Echarts 对象的 setOption 方法将配置项应用到图表中
                echarts.init(document.getElementById('centreLeft1Chart')).setOption(this.options)
            },
            immediate: true,
            deep: true
        }
    }
}
</script>