<template>
    <!-- 绘图面板区域 -->
    <div id="graph-panel" style="width:100%;height:calc(100vh - 16px);background-color:#efefef;"></div>
</template>
    
<script>

import VisGraph from '@/assets/js/visgraph.min.js'
import LayoutFactory from '@/assets/js/visgraph-layout.min.js'
import { config } from 'process';

export default {
    data() {
        return {
            visGraph: null,
            config: {
                node: { //节点的默认配置
                    label: { //标签配置
                        show: true, //是否显示
                        color: '250,250,250', //字体颜色
                        font: 'normal 14px Arial', //字体大小及类型 
                        textPosition: 'Bottom_Center' //文字位置 Top_Center,Bottom_Center,Middle_Right,Middle_Center
                    },
                    shape: 'circle', //rect,circle,star
                    size: 30, //节点宽度
                    color: '80,200,255', //节点颜色
                    borderColor: '80,80,255', //边框颜色
                    borderWidth: 1, //边框宽度,
                    alpha: 1, //节点透明度
                    selected: { //选中时的样式设置
                        borderColor: '180,240,120', //选中时边框颜色
                        borderAlpha: 0.8, //选中时的边框透明度
                        borderWidth: 4 //选中时的边框宽度
                    }
                },
                link: { //连线的默认配置
                    label: { //连线标签
                        show: false, //是否显示
                        color: '50,50,50', //字体颜色
                        font: 'normal 13px Arial' //字体大小及类型
                    },
                    lineType: 'bezier', //连线类型,direct,curver,vlink,hlink,vbezier,hbezier,bezier
                    colorType: 'defined', //连线颜色类型 source:继承source颜色,target:继承target颜色 both:用双边颜色，d:自定义
                    color: '230,150,120', //连线颜色
                    showArrow: false //显示连线箭头
                },
                highLightNeiber: true //相邻节点高亮开关
            },
        }
    },
    components: {
        VisGraph,
        LayoutFactory
    },
    mounted() {

    },
    methods: {
        initCharts(dataList) {
            this.visGraph = new VisGraph(document.getElementById(''), config);//初始化绘图客户端
            this.visGraph.drawData(dataList);//绘制图完成
            this.runLayout(this.visgraph.getGraphData());
        },
        runLayout(graphData) {
            var fastLayout = new LayoutFactory(graphData).createLayout('fastFR');
            fastLayout.initAlgo();//初始化布局算法
            var layoutConf = {
                'froce': 0.95,
                'linkDistance': 180,
                'linkStrength': 0.09,
                'charge': -200,
                'gravity': 0.009,
                'noverlap': false
            };
            fastLayout.resetConfig(layoutConf);//设置布局算法参数
            var runLoopNum = 0;
            while (runLoopNum++ < 300) {
                fastLayout.runLayout();//执行布局计算
            }

            //3、画布元素居中
            visgraph.setZoom('auto');//自动缩放
        }
    }
}
</script>