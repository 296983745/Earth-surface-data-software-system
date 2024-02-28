<template>
    <div id="chart" class="chart">
    </div>
</template>
  
<script>
import * as echarts from 'echarts';
import 'echarts-gl';
export default {
    name: "NetChart",
    data() {
        return {
            myChart: null,

        };
    },
    props: {
        dataList: {
            type: Object,
            required: true
        }
    },
    components: {
    },
    watch: {
        dataList(newValue) {
            this.initCharts(newValue);
        }
    },
    methods: {
        /**
         * 节点点击事件
         */
        nodeClick(params) {
            this.$emit("nodeClick", params);
        },
        /**
         * 边点击事件
         * @param {*} params 
         */
        edgeClick(params) {
            this.$emit("edgeClick", params);
        },
        /**
         * 设置echarts配置项,重绘画布
         */
        initCharts(list) {
            if (list.nodes.length == 0) {
                return;
            }
            let option;
            if (list.nodes.length > 500) {
                option = this.getOptionA();
            } else {
                option = this.getOptionB();
            }
            if (!this.myChart) {
                var chartDom = document.getElementById("chart");
                this.myChart = echarts.init(chartDom);
                this.myChart.on("click", params => {
                    debugger
                    if (params.dataType === "node") {
                        //判断点击的是图表的节点部分
                        this.nodeClick(params);
                    }
                    if (params.dataType === "edge") {
                        //判断点击的是图表的节点部分
                        this.edgeClick(params);
                    }
                });
            }
            // 指定图表的配置项和数据
            // 设置多个option  在数据量不同时，使用不同的option来进行展示
            this.myChart.setOption({
                backgroundColor: '#000', // 背景颜色
                ...option
            });
        },
        closeDetail() {
            this.showDataDetailsPopup = false;
            this.selectedData = {}
        },
        getOptionA() {
            return {
                title: {}, // 图表标题，可根据需要进行配置
                use3D: true,
                renderer: 'webgl',
                tooltip: {
                    trigger: "item",
                    formatter: function (params) {
                        if (params.dataType === "node") {
                            return params.data.name;
                        } else if (params.dataType === "edge") {
                            return `关系名称:${params.data.relationName} <br> 时间：${params.data.time} <br> 空间： ${params.data.space}<br> 主题： ${params.data.topic}`;
                        }
                    }
                },
                legend: [], // 图例，可根据需要进行配置
                // animationDuration: 2000, // 动画持续时间
                animationEasingUpdate: 'quinticInOut', // 动画缓动效果
                color: [],
                series: [
                    {
                        name: '数据目录',
                        type: 'graph',
                        layout: 'none',
                        force: {
                            repulsion: 30,
                            gravity: 0.01,
                            edgeLength: [100, 200],
                        },
                        itemStyle: {
                            color: function () {
                                var colors = ['rgb(203,239,15)',
                                    'rgb(73,15,239)',
                                    'rgb(239,231,15)',
                                    'rgb(15,217,239)',
                                    'rgb(30,15,239)',
                                    'rgb(15,174,239)',
                                    'rgb(116,239,15)',
                                    'rgb(239,15,58)',
                                    'rgb(15,239,174)',
                                    'rgb(239,102,15)',
                                    'rgb(239,15,15)',
                                    'rgb(15,44,239)',
                                    'rgb(239,145,15)',
                                    'rgb(30,239,15)',
                                    'rgb(239,188,15)',
                                    'rgb(159,239,15)',
                                    'rgb(159,15,239)',
                                    'rgb(15,239,44)',
                                    'rgb(15,239,87)',
                                    'rgb(15,239,217)',
                                    'rgb(203,15,239)',
                                    'rgb(239,15,188)',
                                    'rgb(239,15,102)',
                                    'rgb(239,58,15)',
                                    'rgb(239,15,145)',
                                    'rgb(116,15,239)',
                                    'rgb(15,131,239)',
                                    'rgb(73,239,15)',
                                    'rgb(15,239,131)',
                                    'rgb(15,87,239)',
                                    'rgb(239,15,231)'];
                                return colors[Math.round(Math.random() * 32)];
                            }
                        },
                        data: this.dataList.nodes, // 节点数据，根据实际情况进行配置
                        links: this.dataList.links, // 连接数据，根据实际情况进行配置
                        zoom: 1.4, // 缩放比例
                        roam: true, // 是否可缩放和漫游
                        label: {
                            show: true,
                            position: 'right',
                            formatter: function (params) {
                                if (params.data.symbolSize > 15) {
                                    return params.data.name;
                                } else {
                                    return '';
                                }
                            }
                        },
                        labelLayout: {
                            hideOverlap: true
                        },
                        lineStyle: {
                            color: 'rgba(255,255,255,1)',
                            opacity: 0.05,
                            curveness: 0.2,
                            with: 0.8
                        },
                        emphasis: {
                            focus: 'adjacency',
                            blurScope: 'global',
                            lineStyle: {
                                width: 2,
                                opacity: 0.5,
                            }
                        }
                    }
                ]
            };
        },
        getOptionB() {
            return {
                title: {}, // 图表标题，可根据需要进行配置
                use3D: true,
                renderer: 'webgl',
                tooltip: {
                    trigger: "item",
                    formatter: function (params) {
                        if (params.dataType === "node") {
                            return params.data.name;
                        } else if (params.dataType === "edge") {
                            return `关系名称:${params.data.relationName} <br> 时间：${params.data.time} <br> 空间： ${params.data.space}<br> 主题： ${params.data.topic}`;
                        }
                    }
                },
                legend: [], // 图例，可根据需要进行配置
                animationDuration: 2, // 动画持续时间
                animationEasingUpdate: 'quinticInOut', // 动画缓动效果
                color: ["red", "blue", "green"],
                series: [
                    {
                        name: '数据目录',
                        type: 'graphGL',
                        layout: 'force',
                        force: {
                            repulsion: 30,
                            gravity: 0.01,
                            edgeLength: [100, 200],
                        },
                        itemStyle: {
                            color: function () {
                                var colors = ['#FF7F0E', '#1F77B4', '#2CA02C'];
                                return colors[Math.round(Math.random() * 3)];
                            }
                        },
                        forceAtlas2: {
                            steps: 1,
                            stopThreshold: 1,
                            jitterTolerence: 10,
                            edgeWeight: [0.2, 1],
                            gravity: 0,
                            edgeWeightInfluence: 1,
                            scaling: 0.2
                        },
                        data: this.dataList.nodes, // 节点数据，根据实际情况进行配置
                        links: this.dataList.links, // 连接数据，根据实际情况进行配置
                        zoom: 1.4, // 缩放比例
                        roam: true, // 是否可缩放和漫游
                        label: {
                            show: true,
                            position: 'right',
                            formatter: function (params) {
                                if (params.data.symbolSize > 5) {
                                    return params.data.name;
                                } else {
                                    return '';
                                }
                            }
                        },
                        labelLayout: {
                            hideOverlap: true
                        },
                        lineStyle: {
                            color: 'source',// 连接线颜色
                            opacity: 0.2,
                            curveness: 0.2 // 连接线曲度，可以根据需要进行配置
                        },
                        emphasis: {
                            focus: 'adjacency',
                            blurScope: 'global',
                            lineStyle: {
                                color: 'red',
                                width: 1
                            }
                        }
                    }
                ]
            };
        }
    },
    beforeDestroy() {
        if (this.myChart) {
            this.myChart.dispose();
            this.myChart = null;
        }
    }
};
</script>
  
<style scoped>
/* 根据需要自定义样式 */
</style>
  