<template>
    <div id="bottomCenter">
        <div class="bg-color-black">
            <div class="d-flex pt-2 pl-2">
                <span>
                    <icon name="chart-bar" class="text-icon"></icon>
                </span>
                <div class="d-flex">
                    <span class="fs-xl text mx-2">词云</span>
                </div>
                <bottomCenterChart />
            </div>
        </div>
    </div>
</template>

<script>
import bottomCenterChart from '@/components/echart/bottom/bottomCenterChart/bottomCenterChart.vue';
export default {
    components: {
        bottomCenterChart
    }
}
</script>

<style lang="scss" scoped>
$box-height: 430px;
$box-width: 100%;

#bottomCenter {
    padding: 20px 16px;
    height: $box-height;
    width: $box-width;
    border-radius: 5px;

    .bg-color-black {
        height: $box-height - 35px;
        border-radius: 10px;
    }

    .text {
        color: #c3cbde;
    }

    .chart-box {
        margin-top: 16px;
        width: 170px;
        height: 170px;

        .active-ring-name {
            padding-top: 10px;
        }
    }
}
</style>
