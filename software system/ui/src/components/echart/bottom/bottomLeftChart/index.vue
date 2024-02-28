<template>
    <div>
        <Chart :cdata="this.cdata" />
    </div>
</template>

<script>
import Chart from './chart.vue'
import { getDataCatalogMonthStatistics } from '@/api/dataMap/dataMap'
export default {
    data() {
        return {
            cdata: {
            },
            response: [
                {
                    "month": "2022-07",
                    "add_data_count": 80,
                    "update_data_count": 84
                },
                {
                    "month": "2022-08",
                    "add_data_count": 99,
                    "update_data_count": 86
                },
                {
                    "month": "2022-09",
                    "add_data_count": 76,
                    "update_data_count": 82
                },
                {
                    "month": "2022-10",
                    "add_data_count": 88,
                    "update_data_count": 71
                },
                {
                    "month": "2022-11",
                    "add_data_count": 81,
                    "update_data_count": 88
                },
                {
                    "month": "2022-12",
                    "add_data_count": 82,
                    "update_data_count": 83
                },
                {
                    "month": "2023-01",
                    "add_data_count": 87,
                    "update_data_count": 102
                },
                {
                    "month": "2023-02",
                    "add_data_count": 85,
                    "update_data_count": 80
                },
                {
                    "month": "2023-03",
                    "add_data_count": 80,
                    "update_data_count": 78
                },
                {
                    "month": "2023-04",
                    "add_data_count": 84,
                    "update_data_count": 77
                },
                {
                    "month": "2023-05",
                    "add_data_count": 73,
                    "update_data_count": 85
                },
                {
                    "month": "2023-06",
                    "add_data_count": 15,
                    "update_data_count": 20
                }
            ]
        };
    },
    components: {
        Chart,
    },
    mounted() {
        this.setData();
    },
    methods: {
        // 根据自己的业务情况修改
        setData() {
            let monthData = [];
            let addData = [];
            let updateData = [];
            let data = this.response
            data.forEach(item => {
                monthData.push(item.month)
                addData.push(item.add_data_count)
                updateData.push(item.update_data_count)
            })
            this.cdata.monthData = monthData
            console.log(monthData)
            this.cdata.addData = addData
            console.log(addData)
            this.cdata.updateData = updateData
            console.log(updateData)
        },
    }
};
</script>

<style lang="scss" scoped></style>