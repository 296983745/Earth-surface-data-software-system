<template>
    <div>
        <Chart :cdata="cdata" />
    </div>
</template>

<script>
import Chart from './chart.vue';
export default {
    data() {
        return {
            cdata: [
                { name: '北京', value: Math.floor(Math.random() * 100) },
                { name: '天津', value: Math.floor(Math.random() * 100) },
                { name: '河北', value: Math.floor(Math.random() * 100) },
                { name: '山西', value: Math.floor(Math.random() * 100) },
                { name: '内蒙古', value: Math.floor(Math.random() * 100) },
                { name: '辽宁', value: Math.floor(Math.random() * 100) },
                { name: '吉林', value: Math.floor(Math.random() * 100) },
                { name: '黑龙江', value: Math.floor(Math.random() * 100) },
                { name: '上海', value: Math.floor(Math.random() * 100) },
                { name: '江苏', value: Math.floor(Math.random() * 100) },
                { name: '浙江', value: Math.floor(Math.random() * 100) },
                { name: '安徽', value: Math.floor(Math.random() * 100) },
                { name: '福建', value: Math.floor(Math.random() * 100) },
                { name: '江西', value: Math.floor(Math.random() * 100) },
                { name: '山东', value: Math.floor(Math.random() * 100) },
                { name: '河南', value: Math.floor(Math.random() * 100) },
                { name: '湖北', value: Math.floor(Math.random() * 100) },
                { name: '湖南', value: Math.floor(Math.random() * 100) },
                { name: '广东', value: Math.floor(Math.random() * 100) },
                { name: '广西', value: Math.floor(Math.random() * 100) },
                { name: '海南', value: Math.floor(Math.random() * 100) },
                { name: '重庆', value: Math.floor(Math.random() * 100) },
                { name: '四川', value: Math.floor(Math.random() * 100) },
                { name: '贵州', value: Math.floor(Math.random() * 100) },
                { name: '云南', value: Math.floor(Math.random() * 100) },
                { name: '西藏', value: Math.floor(Math.random() * 100) },
                { name: '陕西', value: Math.floor(Math.random() * 100) },
                { name: '甘肃', value: Math.floor(Math.random() * 100) },
                { name: '青海', value: Math.floor(Math.random() * 100) },
                { name: '宁夏', value: Math.floor(Math.random() * 100) },
                { name: '新疆', value: Math.floor(Math.random() * 100) },
                { name: '台湾', value: Math.floor(Math.random() * 100) },
                { name: '香港', value: Math.floor(Math.random() * 100) },
                { name: '澳门', value: Math.floor(Math.random() * 100) },
                { name: '南海诸岛', value: Math.floor(Math.random() * 100) }
            ]
        }
    },
    components: {
        Chart,
    },
    mounted() {
    },
    methods: {
    }
}
</script>

<style lang="scss" scoped></style>