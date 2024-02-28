<template>
    <div id="index" ref="appRef">
        <div class="bg">
            <dv-loading v-if="loading">Loading...</dv-loading>
            <div v-else class="host-body">
                <div class="d-flex jc-center">
                    <dv-decoration-10 class="dv-dec-10" />
                    <div class="d-flex jc-center">
                        <dv-decoration-8 class="dv-dec-8" :color="decorationColor" />
                        <div class="title">
                            <span class="title-text">数据可视化平台</span>
                            <dv-decoration-6 class="dv-dec-6" :reverse="true" :color="['#50e3c2', '#67a1e5']" />
                        </div>
                        <dv-decoration-8 class="dv-dec-8" :reverse="true" :color="decorationColor" />
                    </div>
                    <dv-decoration-10 class="dv-dec-10-s" />
                </div>

                <!-- 第二行 -->
                <div class="d-flex jc-between px-2">
                    <div class="d-flex aside-width">
                        <div class="react-left ml-4 react-l-s">
                            <span class="react-left"></span>
                            <span class="text"></span>
                        </div>
                        <div class="react-left ml-3">
                            <span class="text"></span>
                        </div>
                    </div>
                    <div class="d-flex aside-width">
                        <div class="react-right bg-color-blue mr-3">
                            <span class="text fw-b"></span>
                        </div>
                        <div class="react-right mr-4 react-l-s">
                            <span class="react-after"></span>
                            <span class="text">数据更新时间： {{ dateYear }} {{ dateWeek }} {{ dateDay }}</span>
                        </div>
                    </div>
                </div>

                <div class="body-box">
                    <!-- 第三行数据 -->
                    <div class="content-box">
                        <div style="margin-right: 20px;">
                            <dv-border-box-11 title="数据访问量排行榜Top10">
                                <centerLeft1 />
                            </dv-border-box-11>
                        </div>
                        <div>
                            <dv-border-box-12>
                                <centerLeft2 />
                            </dv-border-box-12>
                        </div>
                        <div>
                            <dv-border-box-11 title="数据来源统计Top10">
                                <centerRight1 />
                            </dv-border-box-11>
                        </div>
                    </div>

                    <!-- 第四行数据 -->
                    <div class="bottom-box">
                        <dv-border-box-12>
                            <bottomLeft />
                        </dv-border-box-12>
                        <dv-border-box-12>
                            <bottomCenter />
                        </dv-border-box-12>
                        <dv-border-box-12>
                            <bottomRight />
                        </dv-border-box-12>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import drawMixin from "../../utils/drawMixin";
import { screenFormatTime } from '../../utils/index.js'
import centerLeft1 from './centerLeft1'
import centerLeft2 from './centerLeft2'
import centerRight1 from './centerRight1'
import centerRight2 from './centerRight2'
import bottomLeft from './bottomLeft'
import bottomRight from './bottomRight'
import bottomCenter from "./bottomCenter.vue";

export default {
    mixins: [drawMixin],
    data() {
        return {
            timing: null,
            loading: true,
            dateDay: null,
            dateYear: null,
            dateWeek: null,
            weekday: ['周日', '周一', '周二', '周三', '周四', '周五', '周六'],
            decorationColor: ['#568aea', '#000000']
        }
    },
    components: {
        centerLeft1,
        centerLeft2,
        centerRight1,
        centerRight2,
        bottomLeft,
        bottomRight,
        bottomCenter
    },
    mounted() {
        this.timeFn()
        this.cancelLoading()
    },
    beforeDestroy() {
        clearInterval(this.timing)
    },
    methods: {
        timeFn() {
            this.timing = setInterval(() => {
                this.dateDay = screenFormatTime(new Date(), 'HH: mm: ss')
                this.dateYear = screenFormatTime(new Date(), 'yyyy-MM-dd')
                this.dateWeek = this.weekday[new Date().getDay()]
            }, 1000)
        },
        cancelLoading() {
            setTimeout(() => {
                this.loading = false
            }, 500)
        }
    }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';
</style>
