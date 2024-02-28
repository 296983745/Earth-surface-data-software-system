<template>
    <div id="centerLeft1">
        <div class="bg-color-black">
            <dv-scroll-ranking-board class="dv-scr-rank-board" :config="config" style="width:448px;height:413px" />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            config: {
                data: [
                    {
                        name: '全球0.05度增强日光诱导叶绿素荧光（eSIF）产品（2021年）',
                        value: 55
                    },
                    {
                        name: '中国30米分辨率长时序湖泊水体透明度数据集LAWSD30（1985-2021年）',
                        value: 120
                    },
                    {
                        name: '全球2°×2.5°分辨率逐月大气二氧化碳浓度栅格模拟数据集（1992-2020年）',
                        value: 78
                    },
                    {
                        name: '东北地区30m分辨率主要作物分布数据集（2017-2021年）',
                        value: 66
                    },
                    {
                        name: '蒙古高原500m分辨率植被物候及变化趋势数据集(2001–2019年)',
                        value: 80
                    },
                    {
                        name: '全球大气二氧化碳与甲烷月平均垂直柱浓度分布空间连续数据集（2010-2021年）',
                        value: 45
                    },
                    {
                        name: '蒙古高原500米分辨率动态生境指数数据集（2001-2018年）',
                        value: 29
                    },
                    {
                        name: '长江流域0.008333°分辨率数字河网数据集(2020年)',
                        value: 29
                    },
                    {
                        name: '基于“两叶模型”的贵州省500m分辨率8天APAR数据集（2001-2016年）',
                        value: 19
                    },
                    {
                        name: '蒙古高原250m分辨率植被生长季年际时空变化数据集（2001-2021年）',
                        value: 9
                    }
                ]
            }
        }
    },
    components: {
    },
    mounted() {

    },
    methods: {

    }
}
</script>

<style lang="scss" scoped>
$box-width: 100%;
$box-height: 100%;

#centerLeft1 {
    padding: 16px;
    height: $box-height;
    width: $box-width;
    border-radius: 10px;

    .bg-color-black {
        height: calc(100% - 30px);
        border-radius: 10px;
    }

}

.dv-scr-rank-board {
    margin-top: 45px;
}
</style>
