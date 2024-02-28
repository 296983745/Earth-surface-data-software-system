<template>
    <div id="centerRight1">
        <div class="bg-color-black">
            <dv-scroll-board class="dv-scr-board" :config="config" style="width:448px;height:413px" />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            config: {
                header: ['名称', '数据量', '占比率'],
                data: [
                    ['国家地理资源分中心', '1000', "<span  class='colorGrass'>15.21%</span>"],
                    ['长江三角洲分中心', '911', "<span  class='colorGrass'>12.75%</span>"],
                    ['湖泊-流域分中心', '730', "<span  class='colorGrass'>10.25%</span>"],
                    ['黄河中下游分中心', '600', "<span  class='colorGrass'>9.55%</span>"],
                    ['黄土高原分中心', '580', "<span  class='colorGrass'>8.44%</span>"],
                    ['河图与湿地分中心', '510', "<span  class='colorGrass'>7.23%</span>"],
                    ['南海及邻近海区分中心', '430', "<span  class='colorGrass'>6.52%</span>"],
                    ['地球物理分中心', '401', "<span  class='colorGrass'>6.12%</span>"],
                    ['土壤分中心', '392', "<span  class='colorGrass'>5.21%</span>"],
                    ['大气分中心', '380', "<span  class='colorGrass'>5.1%</span>"]
                ],
                rowNum: 7, //表格行数
                headerHeight: 35,
                headerBGC: '#0f1325', //表头
                oddRowBGC: '#0f1325', //奇数行
                evenRowBGC: '#171c33', //偶数行
                index: true,
                columnWidth: [50],
                align: ['center']
            }
        }
    }
}
</script>

<style lang="scss" scoped>
$box-height: 100%;
$box-width: 100%;

#centerRight1 {
    padding: 16px;
    padding-top: 20px;
    height: $box-height;
    width: $box-width;
    border-radius: 5px;

    .bg-color-black {
        height: calc(100% - 30px);
        border-radius: 10px;
    }

    .text {
        color: #c3cbde;
    }
}

.dv-scr-board {
    margin-top: 45px;
}
</style>
