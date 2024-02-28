<template>
    <div>
        <div id="worldgraph" style="width: 100%; height: 500px"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts';
import worldData from '../../api/world.json';
export default {
    data() {
        return {
            worldGraph: {},
            dataWebsites: [
                {
                    id: 1,
                    name: "NASA EOSDIS",
                    latitude: 38.9917,
                    longitude: -77.0259
                },
                {
                    id: 2,
                    name: "USGS EarthExplorer",
                    latitude: 39.0222,
                    longitude: -77.0519
                },
                {
                    id: 3,
                    name: "ESA Earth Online",
                    latitude: 52.2370,
                    longitude: 0.0968
                },
                {
                    id: 4,
                    name: "NOAA NCEI",
                    latitude: 35.7886,
                    longitude: -78.6417
                },
                {
                    id: 5,
                    name: "GBIF",
                    latitude: 55.7062,
                    longitude: 12.5729
                },
                {
                    id: 6,
                    name: "WorldClim",
                    latitude: 43.4748,
                    longitude: 11.8839
                },
                {
                    id: 7,
                    name: "MODIS Land Rapid Response System",
                    latitude: 38.8895,
                    longitude: -77.0353
                },
                {
                    id: 8,
                    name: "OpenStreetMap",
                    latitude: 51.5074,
                    longitude: -0.1278
                },
                {
                    id: 9,
                    name: "Copernicus Open Access Hub",
                    latitude: 41.9050,
                    longitude: 12.4951
                },
                {
                    id: 10,
                    name: "Earthdata Search",
                    latitude: 38.8895,
                    longitude: -77.0353
                },
                {
                    id: 11,
                    name: "Geoscience Australia",
                    latitude: -35.3082,
                    longitude: 149.1244
                },
                {
                    id: 12,
                    name: "CIESIN - Center for International Earth Science Information Network",
                    latitude: 41.2587,
                    longitude: -73.7899
                },
                {
                    id: 13,
                    name: "Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center",
                    latitude: 35.6528,
                    longitude: 139.8395
                },
                {
                    id: 14,
                    name: "South African Environmental Observation Network (SAEON)",
                    latitude: -33.9249,
                    longitude: 18.4241
                },
                {
                    id: 15,
                    name: "Brazil Data Cube",
                    latitude: -15.7801,
                    longitude: -47.9292
                },
                {
                    id: 16,
                    name: "中国地球科学数据共享网",
                    latitude: 39.9087,
                    longitude: 116.3975
                },
                {
                    id: 17,
                    name: "中国国家卫星气象中心",
                    latitude: 39.9922,
                    longitude: 116.3338
                },
                {
                    id: 18,
                    name: "中国科学院地理科学与资源研究所",
                    latitude: 39.9323,
                    longitude: 116.3805
                },
                {
                    id: 19,
                    name: "中国环境监测总站",
                    latitude: 39.9087,
                    longitude: 116.3975
                },
                {
                    id: 20,
                    name: "中国地震局",
                    latitude: 39.9502,
                    longitude: 116.3527
                }
            ]
        }
    },
    components: {
    },
    methods: {
        initData() {
            if (this.worldGraph.value) {
                this.worldGraph.value.dispose();
                this.worldGraph.value = null;
            }
            this.drawnWorldChart();
        },
        drawnWorldChart() {
            if (!document.getElementById('worldgraph')) {
                return;
            }
            echarts.registerMap('world', JSON.stringify(worldData));
            this.worldGraph.value = echarts.init(document.getElementById('worldgraph'));
            this.worldGraph.value.on("click", params => {
                if (params.componentType == 'series') {
                    this.openTable(params);
                }
            });
            let option = {
                grid: {
                    width: '100%',
                    height: '100%',
                    left: '0%',
                    right: '0%',
                    bottom: '0%',
                    containLabel: true
                },
                geo: {
                    type: 'map',
                    map: 'world',
                    roam: false,
                    label: {
                        show: false
                    },
                    emphasis: {
                        label: {
                            show: false
                        }
                    },
                    zoom: 1.1,
                    itemStyle: {
                        areaColor: {
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 1,
                            y2: 1,
                            colorStops: [
                                {
                                    offset: 0,
                                    color: '#F6FBFF'
                                },
                                {
                                    offset: 1,
                                    color: '#CEE0E7'
                                }
                            ]
                        },
                        borderColor: '#ccc',
                        borderWidth: 0.5,
                    },
                },
                series: [
                    {
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        symbol: 'path://M808.442084 750.473323c-19.128663-12.814864-45.00603-23.89727-76.91374-32.93818-29.814026-8.447393-64.333214-14.988366-101.734032-19.411095 8.888438-13.238512 17.989723-27.236318 27.111474-41.869596 35.539424-57.014528 63.920822-111.757317 84.355223-162.708755 26.170033-65.25419 39.440267-124.84131 39.440267-177.104627 0-34.364669-7.223518-67.695798-21.468964-99.06832-13.684674-30.134321-33.229822-57.155744-58.09207-80.313164-24.708751-23.014156-53.446259-41.069371-85.416392-53.6632-32.979112-12.990872-67.976184-19.578917-104.018052-19.578917-36.042891 0-71.039963 6.588045-104.019075 19.578917-31.968086 12.593829-60.706617 30.649044-85.415368 53.6632-24.862247 23.157419-44.407396 50.178843-58.091046 80.313164-14.246469 31.372521-21.469987 64.703651-21.469987 99.06832 0 52.264341 13.269211 111.850437 39.440267 177.104627 20.434401 50.952462 48.815799 105.695251 84.355223 162.708755 9.123798 14.636349 18.22713 28.637224 27.117614 41.877783-37.374212 4.421706-71.868841 10.960633-101.664448 19.402909-31.906687 9.041934-57.784054 20.123316-76.912717 32.93818-37.658691 25.228591-45.563732 54.501288-45.563732 74.614371s7.90504 49.386804 45.562708 74.615395c19.128663 12.814864 45.00603 23.898293 76.91374 32.93818 59.391668 16.829294 137.445372 26.098401 219.785705 26.098401 82.33931 0 160.394037-9.269108 219.785705-26.098401 31.906687-9.04091 57.784054-20.123316 76.912717-32.93818 37.658691-25.228591 45.562708-54.502311 45.562708-74.615395S846.100776 775.701914 808.442084 750.473323zM511.705799 198.241017c66.177212 0 119.839389 53.661154 119.839389 119.838366 0 66.177212-53.661154 119.838366-119.839389 119.838366-66.176189 0-119.838366-53.661154-119.838366-119.838366C391.866411 251.90217 445.528588 198.241017 511.705799 198.241017zM511.743662 907.575384c-160.768567 0-291.096844-36.930097-291.096844-82.486666 0-37.220716 87.008656-68.678172 206.531843-78.945003 34.139541 46.972824 59.659775 76.699869 61.278645 78.576613l23.248494 26.960025 23.249517-26.960025c1.617847-1.876744 27.140127-31.606859 61.282738-78.582753 119.559003 10.260691 206.602452 41.723264 206.602452 78.951143C802.840506 870.645286 672.511205 907.575384 511.743662 907.575384z',
                        symbolSize: 10,
                        data: this.dataWebsites.map(item => ({
                            name: item.name,
                            value: [item.longitude, item.latitude],
                        })),
                    }
                ]
            };
            this.worldGraph.value.setOption(option);
        },

    },
    mounted() {
        this.initData();
    },
    beforeDestroy() {
        if (this.worldGraph.value) {
            this.worldGraph.value.dispose();
            this.worldGraph.value = null;
        }
    }
}
</script>