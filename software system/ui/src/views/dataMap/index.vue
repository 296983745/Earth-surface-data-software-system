<template>
    <div>
        <div id="map" class="map"></div>
        <div id="control1">
            <div class="ol-control" style=" top:100px!important;left: 9px!important;  z-index: 11; ">
                <el-tooltip class="item" effect="dark" content="数据展示" placement="right">
                    <button><i class="el-icon-data-analysis" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="openDataStatistics()" /></button>
                </el-tooltip>
            </div>
            <div class="ol-control" style=" top:125px!important;left: 9px!important;  z-index: 11;">
                <el-tooltip class="item" effect="dark" content="目录树" placement="right">
                    <el-button><i class="el-icon-tickets" style="margin: 3px!important;"
                            @click.stop="openCatalogTree" /></el-button>
                </el-tooltip>
            </div>
            <div class="tree-container" v-if="treeVisible">
                <catalogTree ref="catalogTree" :data="this.treeData" @handleNodeClick="handleNodeClick"></catalogTree>
            </div>
            <div class="ol-control" style=" top:150px!important;left: 9px!important; z-index: 11;">
                <el-tooltip class="item" effect="dark" content="搜索" placement="right">
                    <button><i class="el-icon-search" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="openSearch" /></button>
                </el-tooltip>
            </div>
            <div class="search-container" v-if="searchVisible">
                <el-row :gutter="20" class="statistics-row">
                    <el-col :span="6">
                        <el-card shadow="always" class="statistics-card">
                            <h1 class="statistics-title">数据总量</h1>
                            <div class="eye-catching-number total">
                                <span>1000</span>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card shadow="always" class="statistics-card">
                            <h1 class="statistics-title">亚洲</h1>
                            <div class="eye-catching-number YAZHOU">
                                <span>12</span>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card shadow="always" class="statistics-card">
                            <h1 class="statistics-title">欧洲</h1>
                            <div class="eye-catching-number OUZHOU">
                                <span>456</span>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card shadow="always" class="statistics-card">
                            <h1 class="statistics-title">美洲</h1>
                            <div class="eye-catching-number MEIZHOU">
                                <span>789</span>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <el-row class="search-section">
                    <el-input placeholder="关键字搜索" class="search-input"></el-input>
                    <el-select class="website-select" placeholder="所有网站">
                        <el-option label="网站1" value="site1"></el-option>
                        <el-option label="网站2" value="site2"></el-option>
                        <!-- 添加更多选项 -->
                    </el-select>
                    <el-button class="search-button" type="primary">搜索</el-button>
                    <el-button class="show-map-button" type="primary">显示到地图</el-button>
                </el-row>
            </div>
            <div class="ol-control" style=" top:175px!important;left: 9px!important;">
                <el-tooltip class="item" effect="dark" content="目录数据列表" placement="right">
                    <button><i class="el-icon-notebook-2" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="openTable()" /></button>
                </el-tooltip>
            </div>
            <div class="ol-control" style=" top:100px!important;right: 9px!important;">
                <el-tooltip class="item" effect="dark" content="还原到主视角" placement="left">
                    <button><i class="el-icon-view" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="revertToMainPerspective()" /></button>
                </el-tooltip>
            </div>
            <div class="ol-control" style=" top:125px!important;right: 9px!important;">
                <el-tooltip class="item" effect="dark" content="聚合显示" placement="left">
                    <button><i class="el-icon-setting" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="clusterShow(this)" /></button>
                </el-tooltip>

            </div>
            <div class="ol-control" style=" top:150px!important;right: 9px!important;">
                <el-tooltip class="item" effect="dark" content="热力图显示" placement="left">
                    <button><i class="el-icon-setting" style="margin: 3px!important; cursor: pointer;"
                            @click.stop="hotShow(this)" /></button>
                </el-tooltip>

            </div>
        </div>
        <tableModel ref="tableModel" style="height: 950px;" @setTableDataMarker="setTableDataMarker"
            @concelTableDataMarker="concelTableDataMarker" />
        <dataChart ref="dataChart" />
        <nodeSvg />
        <!-- 数据中心介绍弹窗弹框 -->
        <div ref="popup" class="popup" v-show="shopPopup">
            <div class="popup-content">
                <button class="close-button" @click="closePopup">×</button>
                <h3><strong>{{ this.tableDataDetail.name }}</strong></h3>
                <div class="image-container">
                    <img v-show="this.tableDataDetail.image" class="data-image" :src="this.tableDataDetail.image" />
                    <img v-show="!this.tableDataDetail.image" class="data-image" src="../../image/noImage.jpg" />
                </div>
                <div class="info">
                    <p><strong>简介：</strong>{{ this.tableDataDetail.introduction }}</p>
                    <p><strong>服务地址：</strong>{{ this.tableDataDetail.place }}</p>
                    <p><strong>网址：</strong><a :href="this.tableDataDetail.url" style="color: #409eff;text-decoration: none;"
                            target="_blank">{{ this.tableDataDetail.url
                            }}</a></p>
                    <p><strong>数据列表： </strong><button @click="checktable()">查看</button></p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>

import 'ol/ol.css';
import { Map, View, Overlay } from 'ol';
import TileLayer from 'ol/layer/Tile';
import { Heatmap as HeatmapLayer } from "ol/layer";
import OSM from 'ol/source/OSM';
import { XYZ } from 'ol/source'
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import Feature from 'ol/Feature';
import Cluster from 'ol/source/Cluster';
import Point from 'ol/geom/Point';
import * as olProj from "ol/proj";
import { Text, Style, Fill, Circle, Stroke, Icon } from "ol/style";
import { defaults as defaultControls, ScaleLine, FullScreen, Control } from 'ol/control';
import OverviewMap from 'ol/control/OverviewMap';
import { getDataCatalogAll } from '@/api/dataMap/dataMap'
import { fromLonLat } from 'ol/proj';
// 表格组件
import tableModel from './component/tableModel.vue'
// 目录树组件
import catalogTree from './component/catalogTree.vue';
// 数据统计组件
import dataChart from './component/dataChart.vue';

import nodeSvg from './component/nodeSvg.vue';


export default {
    name: 'WorldMap',
    data() {
        return {
            dataWebsites: [
                {
                    id: 1,
                    name: "国家地理资源分中心",
                    shortName:"",
                    latitude: 40.988393,
                    longitude: 116.562244,
                    introduction: "国家地球系统科学数据中心-地理资源分中心（以下简称“中心”），围绕地球系统科学与全球变化领域科技创新、国家重大需求与区域可持续发展， 依托中国科学院地理科学与资源研究所共享共建20余年，形成国内规模最大的地理资源综合数据库群。",
                    image: require("../../image/center/diliziyuanzhongxin.jpg"),
                    place: "北京市朝阳区大屯路甲11号D426房间",
                    url: "http://gre.geodata.cn/"
                },
                {
                    id: 2,
                    name: "长江三角洲分中心",
                    shortName:"",
                    latitude: 32.115388,
                    longitude: 118.928692,
                    introduction:
                        "国家地球系统科学数据中心-长江三角洲分中心依托南京师范大学而建立，由虚拟地理环境教育部重点实验室与地理信息科学江苏省重点实验室负责建设。为地球系统科学研究与区域可持续发展决策提供数据支撑。",
                    image: require("../../image/center/changjiangsanjiaozhoufenzhongxin.png"),
                    place: "江苏省南京市栖霞区文苑路1号 南京师范大学地理科学学院 (210023)",
                    url: "http://geodata.nnu.edu.cn"
                },
                {
                    id: 3,
                    name: "湖泊-流域分中心",
                    latitude: 30.048418,
                    shortName:"",
                    longitude: 118.783950,
                    introduction:
                        "国家地球系统科学数据中心湖泊—流域分中心是国家科技基础条件平台“国家地球系统科学数据中心”（http://www.geodata.cn）的分中心，由中国科学院南京地理与湖泊研究所下属支撑部门湖泊—流域科学数据中心（以下简称“数据中心”）负责承建。为国内外用户提供数据共享服务。",
                    image: require("../../image/center/hupoliuyufenzhongxin.png"),
                    place: "南京市北京东路73号(210008)",
                    url: "http://lake.geodata.cn/"

                },
                {
                    id: 4,
                    name: "黄河中下游分中心",
                    latitude: 34.806024,
                    shortName:"",
                    longitude: 114.353128,
                    introduction:
                        "黄河中下游分中心依托河南大学环境与规划学院以及教育部人文社科重点研究基地黄河文明与可持续发展研究中心建立，为全球范围内进行黄河研究的科研人员、相关政府部门和社会公众提供在线、离线多种形式数据共享服务。",
                    image: require("../../image/center/huanghezhongxiayoufenzhongxin.png"),
                    place: "河南省开封市河南大学金明校区环境与规划学院,黄河中下游分中心运行服务中心 （475000）",
                    url: "http://henu.geodata.cn/"
                },
                {
                    id: 5,
                    name: "黄土高原分中心",
                    shortName:"",
                    latitude: 34.281017,
                    longitude: 108.086262,
                    introduction: "黄土高原分中心是国家科技基础条件平台“国家地球系统科学数据共享服务平台”的区域数据共享与运行服务中心，承担单位是西北农林科技大学水土保持研究所（原中国科学院水利部水土保持研究所）为该地区生态环境建设和农业发展从科学研究、生产实践、政府决策、科技教育等不同层面上提供科学数据支撑和服务。",
                    image: require("../../image/center/huangtugaoyuanfenzhongxin.png"),
                    place: "陕西省杨凌农业示范区西农路26号水保所(712100)",
                    url: "http://loess.geodata.cn/"
                },
                {
                    id: 6,
                    name: "黑土与湿地分中心",
                    shortName:"",
                    latitude: 45.720042,
                    longitude: 126.645117,
                    introduction: "黑土与湿地科学数据中心是国家地球系统科学数据中心的区域中心之一，为高等院校、科研机构、政府部门、生产经营企业等提供了详实的原始数据及筛选、整合、加工的权威数据，开展了黑土区水土流失治理跨平台专题服务，为社会提供了全方位的数据、技术、实物、培训于一体的综合科技支撑服务。",
                    image: require("../../image/center/heituyushidifenzhongxin.png"),
                    place: "黑龙江省哈尔滨市南岗区哈平路138号中国科学院东北地理与农业生态研究所（150081）",
                    url: "http://northeast.geodata.cn/"
                },
                {
                    id: 7,
                    name: "南海及邻近海区分中心",
                    shortName:"",
                    latitude: 23.102453,
                    longitude: 113.329873,
                    introduction:
                        "国家地球系统科学数据共享服务平台-- - 国家地球系统科学数据共享服务平台---南海及其邻近海区科学数据中心立足于我国最大的边缘海和唯一的热带海区——南海，南海的数据不仅仅对科学研究、经济发展、国家安全有重要意义，在全球变暖研究也具有现实意义。",
                    image: require("../../image/center/nanhaijijinlinhaifenzhongxin.png"),
                    place: "中国科学院南海海洋研究所 数据中心 广东省广州市新港西路164号 (510301)",
                    url: "http://ocean.geodata.cn/"
                },
                {
                    id: 8,
                    name: "地球物理分中心",
                    shortName:"",
                    latitude: 38.955434,
                    longitude: 116.417334,
                    introduction:
                        "地球物理分中心主要包括地球空间环境和固体地球物理数据，其数据来源于中国科学院地质与地球物理研究所多个综合野外观测站自主观测的中国地区数据，以及通过参与国际联合观测和数据交换共享（包括建立数据镜像服务器）等获得的全球空间环境和固体地球观测数据。数据中心建立了包括地磁场、中高层大气和电离层等有关学科多个数据库。",
                    image: require("../../image/center/diqiuwulifenzhongxin.png"),
                    place: "北京市朝阳区北土城西路19号 中国科学院地质与地球物理研究所 邮编:100029",
                    url: "http://geospace.geodata.cn/"
                },
                {
                    id: 9,
                    name: "土壤分中心",
                    shortName:"",
                    latitude: 31.049779,
                    longitude: 118.788533,
                    introduction:
                        "国家地球系统科学数据中心土壤分中心是开展土壤科学数据存储、管理、集成、加工及共享服务，支撑土壤科学研究、农业生产、生态环境保护的数据服务基地。中心为国家农业生产、生态环境保护等重大需求提供土壤科学数据支撑服务。",
                    image: require("../../image/center/turangfenzhongxin.png"),
                    place: "江苏省南京市玄武区北京东路71号 中国土壤研究所 邮编:210008",
                    url: "http://soil.geodata.cn/"
                },
                {
                    id: 10,
                    name: "NASA EOSDIS",
                    shortName:"",
                    introduction: "NASA's Earth Observing System Data and Information System (EOSDIS) provides access to a vast collection of earth science data, tools, and services. EOSDIS is designed to support interdisciplinary studies of the earth's climate, land, oceans, and atmosphere.",
                    place: "United States",
                    latitude: 38.9917,
                    longitude: -77.0259,
                    url: "https://earthdata.nasa.gov/"
                },
                {
                    id: 11,
                    name: "USGS EarthExplorer",
                    shortName:"",
                    introduction: "The USGS Earth Explorer is a web-based tool that provides access to an extensive collection of satellite and aerial imagery, as well as other geospatial data. Users can search, preview, and download data from a variety of sources, including Landsat, MODIS, and Sentinel.",
                    place: "United States",
                    latitude: 39.0222,
                    longitude: -77.0519,
                    url: "https://earthexplorer.usgs.gov/"
                },
                {
                    id: 12,
                    name: "ESA Earth Online",
                    shortName:"",
                    introduction: "ESA's Earth Online is a platform that provides access to a wide range of Earth observation data, products and services. Users can search, view, and download data from ESA's satellites such as Sentinel, Envisat, and ERS.",
                    place: "Europe",
                    latitude: 52.2370,
                    longitude: 0.0968,
                    url: "https://earth.esa.int/web/guest/home"
                },
                {
                    id: 13,
                    name: "NOAA NCEI",
                    shortName:"",
                    introduction: "The National Centers for Environmental Information (NCEI) is the world's largest provider of weather and climate data. NCEI provides access to a variety of data, including climate data, oceanographic data, and geophysical data, as well as software and tools for analyzing and visualizing data.",
                    place: "United States",
                    latitude: 35.7886,
                    longitude: -78.6417,
                    url: "https://www.ncei.noaa.gov/"
                },
                {
                    id: 14,
                    name: "GBIF",
                    shortName:"",
                    introduction: "The Global Biodiversity Information Facility (GBIF) is an international network that provides free and open access to data about all types of life on Earth. GBIF collects, synthesizes, and shares data from a variety of sources, including museums, herbaria, and research institutions.",
                    place: "Global",
                    latitude: 55.7062,
                    longitude: 12.5729,
                    url: "https://www.gbif.org/"
                },
                {
                    id: 15,
                    name: "WorldClim",
                    shortName:"",
                    introduction: "WorldClim is a set of global climate data layers that can be used for ecological and biogeographical modeling. The data includes monthly climate data for temperature and precipitation, as well as derived variables such as water balance and frost days.",
                    place: "Global",
                    latitude: 43.4748,
                    longitude: 11.8839,
                    url: "https://www.worldclim.org/"
                },
                {
                    id: 16,
                    name: "MODIS Land Rapid Response System",
                    shortName:"M L R R S",
                    introduction: "The MODIS Land Rapid Response System provides access to satellite imagery from NASA's Moderate Resolution Imaging Spectroradiometer (MODIS). Users can view and download images of the Earth's land surface, including vegetation, fires, and ice cover.",
                    place: "Global",
                    latitude: 38.8895,
                    longitude: -77.0353,
                    url: "https://earthdata.nasa.gov/learn/toolkits/modis-lrrs"
                },
                {
                    id: 17,
                    name: "OpenStreetMap",
                    shortName:"",
                    introduction: "OpenStreetMap is a free and open-source map of the world that is created and maintained by a community of volunteers. The data includes information on roads, buildings, parks, and other features, and can be used for a variety of applications, including navigation, urban planning, and disaster response.",
                    place: "Global",
                    latitude: 51.5074,
                    longitude: -0.1278,
                    url: "https://www.openstreetmap.org/"
                },
                {
                    id: 18,
                    name: "Copernicus Open Access Hub",
                    shortName:"C O A H ",
                    introduction: "The Copernicus Open Access Hub provides access to data from the European Union's Copernicus program, which includes satellite data for a variety of applications, including land, ocean, and atmosphere monitoring.Users can search, view, and download data through the Hub's user-friendly interface.",
                    place: "Europe",
                    latitude: 41.9050,
                    longitude: 12.4951,
                    url: "https://scihub.copernicus.eu/"
                },
                {
                    id: 19,
                    name: "Earthdata Search",
                    shortName:"",
                    introduction: "Earthdata Search is NASA's tool for discovering, previewing, and accessing Earth science data from a variety of sources, including satellite and airborne sensors. Users can search for data based on location, time, and data type, and preview and download data through the intuitive interface.",
                    place: "United States",
                    latitude: 38.8895,
                    longitude: -77.0353,
                    url: "https://search.earthdata.nasa.gov/search"
                },
                {
                    id: 20,
                    name: "Geoscience Australia",
                    shortName:"",
                    introduction: "Geoscience Australia is the national geological survey of Australia and provides geoscientific information and services to the Australian Government and the public. The data includes information on geology, minerals, energy, natural hazards, and spatial data.",
                    place: "Australia",
                    latitude: -35.3082,
                    longitude: 149.1244,
                    url: "https://www.ga.gov.au/"
                },
                {
                    id: 21,
                    name: "CIESIN - Center for International Earth Science Information Network",
                    shortName:" C-CFIESIN",
                    introduction: "The Center for International Earth Science Information Network (CIESIN) is a research center that specializes in the use of geospatial data and tools for sustainable development. CIESIN provides access to a variety of data related to human interactions with the environment, including population, climate, and land use data.",
                    place: "United States",
                    latitude: 41.2587,
                    longitude: -73.7899,
                    url: "https://ciesin.columbia.edu/"
                },
                {
                    id: 22,
                    name: "Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center",
                    shortName:"JAEAEORC",
                    introduction: "The Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center (EORC) provides satellite data and products for monitoring the Earth's environment. The data includes information on land, oceans, and atmosphere, and can be used for a variety of applications, including disaster management, climate change, and agriculture.",
                    place: "Japan",
                    latitude: 35.6528,
                    longitude: 139.8395,
                    url: "https://www.eorc.jaxa.jp/en/"
                },
                {
                    id: 23,
                    name: "South African Environmental Observation Network (SAEON)",
                    shortName:"S A E O N ",
                    introduction: "The South African Environmental Observation Network (SAEON) is a network of people and organizations that collects and shares environmental data in South Africa. The data includes information on climate, biodiversity, and ecosystems, and can be used for a variety of applications, including conservation, natural resource management, and policy making.",
                    place: "South Africa",
                    latitude: -33.9249,
                    longitude: 18.4241,
                    url: "http://www.saeon.ac.za/"
                },
                {
                    id: 24,
                    name: "Brazil Data Cube",
                    shortName:"",
                    introduction: "The Brazil Data Cube is a platform for processing, analyzing, and visualizing satellite data in Brazil. The platform includes a variety of data sources, including Landsat, Sentinel, and MODIS, and can be used for a variety of applications, including land use and land cover monitoring, forest management, and disaster response.",
                    place: "Brazil",
                    latitude: -15.7801,
                    longitude: -47.9292,
                    url: "https://brazildatacube.org/"
                },
                {
                    id: 25,
                    name: "中国地球科学数据共享网",
                    shortName:"",
                    introduction: "中国地球科学数据共享网是中国地球科学数据共享网络的主要平台之一，提供地球科学数据的共享、存储、管理和服务。用户可以在平台上搜索、浏览和下载地球科学数据。",
                    place: "China",
                    latitude: 39.9087,
                    longitude: 116.3975,
                    url: "http://www.geodata.cn/"
                },
                {
                    id: 26,
                    name: "中国国家卫星气象中心",
                    shortName:"",
                    introduction: "中国国家卫星气象中心是中国气象局的附属机构，负责卫星气象遥感技术研究和应用服务。它提供了中国境内的气象卫星图像和其他遥感数据，以及相应的数据处理和分析服务。",
                    place: "中国",
                    latitude: 39.9042,
                    longitude: 116.4074,
                    url: "http://www.nsmc.cma.gov.cn/"
                },
                {
                    id: 27,
                    name: "国家地球系统科学数据共享服务平台",
                    shortName:"",
                    introduction: "国家地球系统科学数据共享服务平台提供了来自中国各地的地球系统科学数据，包括大气、海洋和陆地等方面的数据。平台旨在促进地球系统科学的研究和应用，支持各种学术和工业应用。",
                    place: "中国",
                    latitude: 39.9042,
                    longitude: 116.4074,
                    url: "http://www.geodata.cn/"
                },
            ],
            treeData: [
                {
                    id: 1,
                    label: "NASA EOSDIS",
                    latitude: 38.9917,
                    longitude: -77.0259,
                    children: [
                        {
                            id: 1,
                            label: '地形',
                            children: [
                                {
                                    id: 11,
                                    label: '地形数据集1',
                                },
                                {
                                    id: 12,
                                    label: '地形数据集2',
                                },
                                {
                                    id: 13,
                                    label: '地形数据集3',
                                },
                            ],
                        },
                        {
                            id: 2,
                            label: '地质',
                            children: [
                                {
                                    id: 21,
                                    label: '地质数据集1',
                                },
                                {
                                    id: 22,
                                    label: '地质数据集2',
                                },
                                {
                                    id: 23,
                                    label: '地质数据集3',
                                },
                            ],
                        },
                        {
                            id: 3,
                            label: '水文',
                            children: [
                                {
                                    id: 31,
                                    label: '水文数据集1',
                                },
                                {
                                    id: 32,
                                    label: '水文数据集2',
                                },
                                {
                                    id: 33,
                                    label: '水文数据集3',
                                },
                            ],
                        },
                        {
                            id: 4,
                            label: '气象',
                            children: [
                                {
                                    id: 41,
                                    label: '气象数据集1',
                                },
                                {
                                    id: 42,
                                    label: '气象数据集2',
                                },
                                {
                                    id: 43,
                                    label: '气象数据集3',
                                },
                            ],
                        },
                        {
                            id: 5,
                            label: '生态',
                            children: [
                                {
                                    id: 51,
                                    label: '生态数据集1',
                                },
                                {
                                    id: 52,
                                    label: '生态数据集2',
                                },
                                {
                                    id: 53,
                                    label: '生态数据集3',
                                },
                            ],
                        },
                        // 更多分类...
                    ]
                },
                {
                    id: 2,
                    label: "USGS EarthExplorer",
                    latitude: 39.0222,
                    longitude: -77.0519,
                    children: [
                        {
                            id: 1,
                            label: '地形',
                            children: [
                                {
                                    id: 11,
                                    label: '地形数据集1',
                                },
                                {
                                    id: 12,
                                    label: '地形数据集2',
                                },
                                {
                                    id: 13,
                                    label: '地形数据集3',
                                },
                            ],
                        },
                        {
                            id: 2,
                            label: '地质',
                            children: [
                                {
                                    id: 21,
                                    label: '地质数据集1',
                                },
                                {
                                    id: 22,
                                    label: '地质数据集2',
                                },
                                {
                                    id: 23,
                                    label: '地质数据集3',
                                },
                            ],
                        },
                        {
                            id: 3,
                            label: '水文',
                            children: [
                                {
                                    id: 31,
                                    label: '水文数据集1',
                                },
                                {
                                    id: 32,
                                    label: '水文数据集2',
                                },
                                {
                                    id: 33,
                                    label: '水文数据集3',
                                },
                            ],
                        },
                        {
                            id: 4,
                            label: '气象',
                            children: [
                                {
                                    id: 41,
                                    label: '气象数据集1',
                                },
                                {
                                    id: 42,
                                    label: '气象数据集2',
                                },
                                {
                                    id: 43,
                                    label: '气象数据集3',
                                },
                            ],
                        },
                        {
                            id: 5,
                            label: '生态',
                            children: [
                                {
                                    id: 51,
                                    label: '生态数据集1',
                                },
                                {
                                    id: 52,
                                    label: '生态数据集2',
                                },
                                {
                                    id: 53,
                                    label: '生态数据集3',
                                },
                            ],
                        },
                        // 更多分类...
                    ]
                },
                {
                    id: 3,
                    label: "ESA Earth Online",
                    latitude: 52.2370,
                    longitude: 0.0968
                },
                {
                    id: 4,
                    label: "NOAA NCEI",
                    latitude: 35.7886,
                    longitude: -78.6417
                },
                {
                    id: 5,
                    label: "GBIF",
                    latitude: 55.7062,
                    longitude: 12.5729
                },
                {
                    id: 6,
                    label: "WorldClim",
                    latitude: 43.4748,
                    longitude: 11.8839
                },
                {
                    id: 7,
                    label: "MODIS Land Rapid Response System",
                    latitude: 38.8895,
                    longitude: -77.0353
                },
                {
                    id: 8,
                    label: "OpenStreetMap",
                    latitude: 51.5074,
                    longitude: -0.1278
                },
                {
                    id: 9,
                    label: "Copernicus Open Access Hub",
                    latitude: 41.9050,
                    longitude: 12.4951
                },
                {
                    id: 10,
                    label: "Geoscience Australia",
                    latitude: -35.3082,
                    longitude: 149.1244
                },
                {
                    id: 11,
                    label: "CIESIN - Center for International Earth Science Information Network",
                    latitude: 41.2587,
                    longitude: -73.7899
                },
                {
                    id: 12,
                    label: "Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center",
                    latitude: 35.6528,
                    longitude: 139.8395
                },
                {
                    id: 13,
                    label: "South African Environmental Observation Network (SAEON)",
                    latitude: -33.9249,
                    longitude: 18.4241
                },
                {
                    id: 14,
                    label: "Brazil Data Cube",
                    latitude: -15.7801,
                    longitude: -47.9292
                },
                {
                    id: 15,
                    label: "中国地球科学数据共享网",
                    latitude: 39.9087,
                    longitude: 116.3975
                },
                {
                    id: 16,
                    label: "中国国家卫星气象中心",
                    latitude: 39.9922,
                    longitude: 116.3338
                }
            ],
            treeVisible: false,
            searchVisible: false,
            features: undefined,
            Tablefeatures: undefined,
            tableMarkData: [],
            popup: null,
            shopPopup: false,
            tableDataDetail: {},
            clusterShowFlag: false,
            hotShowFlag: false,

        }
    },
    components: {
        tableModel,
        catalogTree,
        dataChart,
        nodeSvg

    },
    mounted() {
        this.initMap()
        this.features = [];
        this.Tablefeatures = [];
        this.singleclick();
    },
    methods: {

        initMap() {
            // 创建地图容器和视图
            const mapContainer = document.getElementById('map')
            // const view = new View({
            //     center: olProj.transform([103.23, 35.33], 'EPSG:4326', 'EPSG:3857'),
            //     zoom: 3,
            //     enableRotation: true, // 启用地图旋转
            //     rotation: 0, // 初始旋转角度
            //     pitch: 45, // 设置倾斜角度，以度为单位
            // })
            const view = new View({
                center: fromLonLat([103.23, 35.33]),
                zoom: 3,
                enableRotation: true, // 启用地图旋转
                rotation: 0, // 初始旋转角度
                tilt: 45, // 设置倾斜角度，以度为单位
                layers: [
                    new TileLayer({
                        source: new XYZ({
                            url: 'https://t0.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk=6bf83bd1a699540d61936a68711eb096',

                        }),
                    }),
                    new TileLayer({
                        source: new XYZ({
                            url: "https://t0.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk=6bf83bd1a699540d61936a68711eb096",
                        }),
                        isGroup: true,
                        name: "天地图文字标注",
                    }),
                ],
            });


            // 创建瓦片图层
            const tileLayer = new TileLayer({
                // source: new OSM()
                source: new XYZ({
                    url: 'https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
                })
            })
            // 创建自定义控件
            const directoryControl = new Control({
                element: document.getElementById('control1')
            })
            const overviewMapControl = new OverviewMap({
                layers: [new TileLayer({
                    source: new OSM()
                })],
            });

            // 创建地图实例
            window.map = new Map({
                target: mapContainer,
                layers: [
                    new TileLayer({
                        source: new XYZ({
                            url: 'https://t0.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk=6bf83bd1a699540d61936a68711eb096',
                        }),
                    }),
                    new TileLayer({
                        source: new XYZ({
                            url: "https://t0.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk=6bf83bd1a699540d61936a68711eb096",
                        }),
                        isGroup: true,
                        name: "天地图文字标注",
                    }),
                    // tileLayer
                ],
                //在此设置地图控件
                controls: defaultControls().extend([
                    new ScaleLine(),// 缩放控件
                    directoryControl,
                    overviewMapControl
                ]),
                //开启交互时加载瓦片
                loadTilesWhileInteracting: true,
                //地图显示中心
                view: view
            })
            this.pointermove()
            this.addOverlay()
            this.setWebSiteMarker()
        },

        pointermove() {
            window.map.on("pointermove", (e) => {
                if (window.map.hasFeatureAtPixel(e.pixel)) {
                    window.map.getViewport().style.cursor = "pointer";
                } else {
                    window.map.getViewport().style.cursor = "inherit";
                }
            });
        },
        //设置(数据网站)点位  
        setWebSiteMarker() {
            //获取数据网站列表
            // 添加标点
            let features = []
            this.dataWebsites.forEach(item => {
                if (item.longitude) {

                    let name = item.name;
                    if(item.name.length>20){
                        debugger
                        name = item.shortName
                    }
                    let feature = new Feature({
                        name: name,
                        geometry: new Point(olProj.fromLonLat([item.longitude, item.latitude])),
                    });
                    feature.setProperties({
                        feature_type: "webData",
                        detail: item
                    })
                    let style = new Style({
                        image: new Icon({
                            src: require("../../image/website.png")
                        }),
                        // 标点的文字
                        text: new Text({
                            // 文字
                            text: name,
                            // 文字样式
                            fill: new Fill({
                                color: '#00FF00'
                            }),
                            font: '16px Calibri bolder',
                            // 偏移量
                            offsetY: -20
                        })
                    })
                    feature.setStyle(style);
                    features.push(feature)
                }
            })
            var clusterLayer = new VectorLayer({
                source: new VectorSource({
                    features: features,
                }),
                name: 'webMarkerCluster',
            });
            window.map.addLayer(clusterLayer)
        },
        // 表格数据标注
        setTableDataMarker(data) {
            this.tableMarkData = data
            this.Tablefeatures = []
            // 添加标点
            data.forEach(item => {
                if (item.coordinate) {
                    let style = new Style({
                        image: new Icon({
                            src: require("../../image/dataEntity.png")
                        }),
                        // 标点的文字
                        text: new Text({
                            // 文字
                            text: item.name,
                            // 文字样式
                            fill: new Fill({
                                color: 'blue'
                            }),
                            font: '8px Calibri',
                            // 偏移量
                            offsetY: 10
                        })
                    })
                    let Array = item.coordinate.split(",")
                    let feature = new Feature({
                        geometry: new Point(olProj.fromLonLat([Array[0], Array[1]])),
                    });
                    feature.setProperties({
                        feature_type: "tableData",
                        detail: item
                    })
                    feature.setStyle(style);
                    this.Tablefeatures.push(feature)
                }
            })
            const layer = this.getLayerByName("tableDataMarker");
            if (!layer) {
                // 创建点位位图层
                const marker = new VectorLayer({
                    name: 'tableDataMarker',
                    source: new VectorSource({
                        features: this.Tablefeatures,
                    }),
                });
                window.map.addLayer(marker)
            } else {
                layer.setSource(new VectorSource({
                    features: this.Tablefeatures,
                }))
            }
        },
        // 创建Overlay
        addOverlay() {
            let elPopup = this.$refs.popup;
            this.popup = new Overlay({
                element: elPopup,
                positioning: "bottom-center",
                stopEvent: false,
                offset: [0, -20],
            });
            window.map.addOverlay(this.popup);
        },
        //取消数据标注点位
        concelTableDataMarker() {
            const layer = this.getLayerByName("tableDataMarker");
            layer.setSource(new VectorSource({
                features: [],
            }))
            this.tableMarkData = []
        },
        singleclick() {
            window.map.on("singleclick", (e) => {
                // 判断是否点击在点上
                let feature = window.map.forEachFeatureAtPixel(
                    e.pixel,
                    (feature) => feature
                );
                console.log(feature)
                // 如果点击的是数据网站节点，则可以打开数据表格
                if (feature) {
                    if (feature.values_.feature_type == 'webData') {
                        const zoomLevel = 4; // 缩放级别，可以根据需要进行调整
                        const latitude = feature.values_.detail.latitude + 10; // 替换为实际的纬度值
                        const longitude = feature.values_.detail.longitude; // 替换为实际的经度值
                        window.map.getView().animate({ // 只设置需要的属性即可
                            center: olProj.fromLonLat([longitude, latitude]), // 中心点
                            zoom: zoomLevel, // 缩放级别
                            rotation: undefined, // 缩放完成view视图旋转弧度
                        })
                        this.shopPopup = true
                        const coordinates = feature.getGeometry().getCoordinates()
                        this.tableDataDetail = feature.values_.detail
                        this.popup.setPosition(coordinates);
                    }
                    // 如果是数据目录元数据，则打开详细信息
                    // if (feature.values_.feature_type == 'tableData') {
                    //     this.shopPopup = true
                    //     let coordinates = feature.getGeometry().getCoordinates();
                    //     this.tableDataDetail = feature.values_.detail
                    //     this.popup.setPosition(coordinates);
                    // }
                }
            });
        },
        checktable() {
            let params = {}
            params.name = this.tableDataDetail.name;
            this.$refs.tableModel.openDialog(params);
        },
        closePopup() {
            this.shopPopup = false;
            this.tableDataDetail = {};
        },
        openCatalogTree() {
            this.treeVisible = !this.treeVisible
            if (this.searchVisible) {
                this.searchVisible = false
            }
        },
        openDataStatistics() {
            // 直接打开大屏
            let routeUrl = this.$router.resolve({
                path: "/bigScreenIndex",
            });
            window.open(routeUrl.href, "_blank");
            // this.$refs.dataChart.openDialog();
        },
        openSearch() {
            if (this.treeVisible) {
                this.treeVisible = false
            }
            this.searchVisible = !this.searchVisible
        },
        openTable() {
            let params = {}
            params.name = "all"
            params.data = this.tableMarkData
            params.options = this.dataWebsites
            this.$refs.tableModel.openDialog(params);

        },
        // 点击网站点位，移动视角
        handleNodeClick(data) {
            if (data.latitude) {
                // this.setWebSiteMarker(data, this)
                const latitude = data.latitude; // 替换为实际的纬度值
                const longitude = data.longitude; // 替换为实际的经度值
                const zoomLevel = 10; // 缩放级别，可以根据需要进行调整
                window.map.getView().animate({ // 只设置需要的属性即可
                    center: olProj.fromLonLat([longitude, latitude]), // 中心点
                    zoom: zoomLevel, // 缩放级别
                    rotation: undefined, // 缩放完成view视图旋转弧度
                })
            }
        },
        // 通过名称获取地图图层
        getLayerByName(layername) {
            let layers = window.map.getLayers().getArray();
            for (const layer of layers) {
                if (layer.get("name") == layername) {
                    return layer;
                }
            }
        },
        // 返回到中心视角
        revertToMainPerspective() {
            window.map.getView().animate({ // 只设置需要的属性即可
                center: olProj.transform([103.23, 35.33], 'EPSG:4326', 'EPSG:3857'), // 中心点
                zoom: 3, // 缩放级别
            })
        },
        // 目录数据聚合显示图层方法
        async clusterShow() {
            const layer = this.getLayerByName("cluster");
            if (this.clusterShowFlag) {
                layer.setSource(new VectorSource({
                    features: [],
                }))
                this.clusterShowFlag = false
            } else {
                this.clusterShowFlag = true
                let features = []
                let data = []
                await getDataCatalogAll().then(response => {
                    data = response;
                })
                if (data.size == 0) {
                    this.$message.warning("暂无数据");
                }
                data.forEach(item => {
                    if (item.coordinate) {
                        let Array = item.coordinate.split(",")
                        let feature = new Feature({
                            name: item.name,
                            geometry: new Point(olProj.fromLonLat([Array[0], Array[1]])),
                        });
                        features.push(feature)
                    }
                })
                if (layer) {
                    window.map.removeLayer(layer);
                }
                // 聚合图层数据源
                var clusterSource = new Cluster({
                    distance: 100, // 要素将被聚合在一起的像素距离，默认为20
                    minDistance: 50, // 聚合块之间的最小像素距离，默认为零
                    source: new VectorSource({
                        features: features,
                    }),
                })
                var clusterLayer = new VectorLayer({
                    source: clusterSource,
                    name: 'cluster',
                    style: function (feature) {
                        debugger
                        var size = feature.get('features').length;
                        if (size == 1) {
                            var features = feature.get('features');
                            return new Style({
                                image: new Icon({
                                    src: require("../../image/dataEntity.png")
                                }),
                                // 标点的文字
                                text: new Text({
                                    // 文字
                                    text: features[0].values_.name,
                                    // 文字样式
                                    fill: new Fill({
                                        color: 'blue'
                                    }),
                                    font: '12px Calibri',
                                    // 偏移量
                                    offsetY: 10
                                })
                            })
                        } else {
                            return new Style({
                                image: new Circle({
                                    radius: 20,
                                    stroke: new Stroke({
                                        color: 'white'
                                    }),
                                    fill: new Fill({
                                        color: size < 50 ? '#444693' : '#f47920'

                                    })
                                }),
                                text: new Text({
                                    text: size.toString(),
                                    fill: new Fill({
                                        color: 'white'
                                    })
                                })
                            });
                        }
                    }
                });
                window.map.addLayer(clusterLayer)
            }
        },
        // 热力图显示
        async hotShow() {
            const layer = this.getLayerByName("hot");
            debugger
            if (this.hotShowFlag) {
                debugger
                window.map.removeLayer(layer);
                this.hotShowFlag = false
            } else {
                this.hotShowFlag = true
                let features = []
                let data = []
                await getDataCatalogAll().then(response => {
                    data = response;
                })
                if (data.size == 0) {
                    this.$message.warning("暂无数据");
                }
                data.forEach(item => {
                    if (item.coordinate) {
                        let Array = item.coordinate.split(",")
                        let feature = new Feature({
                            name: item.name,
                            geometry: new Point(olProj.fromLonLat([Array[0], Array[1]])),
                        });
                        features.push(feature)
                    }
                })
                if (layer) {
                    window.map.removeLayer(layer);
                }

                var sourceHeat = new VectorSource({
                    features: features
                })
                var heatmapLayer = new HeatmapLayer({
                    name: 'hot',
                    source: sourceHeat,//热力图资源
                    opacity: 1,//透明度，默认1
                    visible: true,//是否显示，默认trur
                    zIndex: 1,//图层渲染的Z索引,默认按图层加载顺序叠加
                    gradient: ['#00f', '#0ff', '#0f0', '#ff0', '#f00'],//热图的颜色渐变
                    blur: 15,//模糊大小(像素为单位)
                    radius: 8,//半径大小默认为8(像素为单位)
                    extent: [100, 30, 104, 40],//渲染范围，可选值，默认渲染全部
                });
                // 热力图层
                window.map.addLayer(heatmapLayer)
            }
        }
    }
}
</script>
  
<style scoped>
.map {
    width: 100%;
    height: calc(100vh - 50px);
}

.control1 {
    z-index: 1;
    position: absolute;
    left: 0.5em;
    top: 6em;
    width: 50px;
    height: 40px;
}

.control1 div:nth-child(2) {
    margin-top: 2em;
}

.control1 div:nth-child(3) {
    margin-top: 4em;
}

.tree-container {
    position: absolute;
    top: 100px;
    /* 初始位置 */
    left: 60px;
    /* 初始位置 */
    width: 200px;
    /* 调整宽度 */
    height: 300px;
    /* 调整高度 */
    background-color: rgba(255, 255, 255, 0.8) !important;
    /* 背景颜色，略微透明 */
    border: 1px solid #ccc;
    /* 边框样式 */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    /* 阴影效果 */
    overflow: auto;
}

.search-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 260px;
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid #ccc;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.statistics-row {
    width: 100%;
    display: flex;
    justify-content: center;
}

.statistics-card {
    text-align: center;
    width: 100%;
    height: 100%;
}

.statistics-title {
    font-size: 20px;
    color: #333;
    margin-bottom: 10px;
}

.eye-catching-number {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
    color: #fff;
    font-size: 32px;
}

.total {
    background-color: #ff0000;
}

.YAZHOU {
    background-color: #6699ff;
}

.OUZHOU {
    background-color: #6699ff;
}

.MEIZHOU {
    background-color: #6699ff;
}

.search-section {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.search-input {
    width: 200px;
    margin-right: 10px;
}

.website-select {
    width: 150px;
    margin-right: 10px;
}

.search-button,
.show-map-button {
    padding: 5px 10px;
    cursor: pointer;
}

.website-select {
    width: 150px;
    padding: 5px;
    margin-right: 10px;
}

.search-button,
.show-map-button {
    padding: 5px 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
}

.search-button:hover,
.show-map-button:hover {
    background-color: #0056b3;
}


.search-button,
.show-map-button {
    padding: 10px 20px;
    background-color: #ccc;
    color: #fff;
    border: none;
    margin-right: 10px;
    cursor: pointer;
}

.search-button:hover,
.show-map-button:hover {
    background-color: #999;
}


.popup {
    width: 400px;
    background-color: white;
    padding: 2px;
    border-radius: 10px;
    box-shadow: 0 0 15px rgb(177, 177, 177);
}

.close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 18px;
    cursor: pointer;
}

.popup-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 4px;
}

h3 {
    margin-top: 0;
}

.info {
    margin-top: 10px;
}

p {
    margin-bottom: 5px;
}

strong {
    font-weight: bold;
}

.image-container {
    flex: 1;
    text-align: center;
}

.data-image {
    max-width: 100%;
    height: 250px;
    object-fit: contain;
}
</style>
  