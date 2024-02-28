<template>
    <div id="app">
        <header>
            <nav>
                <ul>
                    <li><a href="/">首页</a></li>
                    <li><a href="#">数据</a></li>
                    <li><a href="#">新闻</a></li>
                    <li><a href="#">关于</a></li>
                    <li><a href="#">联系我们</a></li>
                </ul>
            </nav>
            <div class="search">
                <input type="text" placeholder="搜索内容">
                <el-button>Search</el-button>
            </div>
        </header>
        <main>
            <div class="carousel">
                <el-carousel type="card" :interval="5000">
                    <el-carousel-item v-for="(item, index) in carouselItems" :key="index">
                        <img :src="item.imgUrl" alt="图片" style="width:100%;height:100%;">
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="content">
                <div v-for="(item, index) in content" :key="index" class="card">
                    <img :src="item.imgUrl" alt="卡片图片">
                    <div class="card-content">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.content }}</p>
                    </div>
                </div>
            </div>
        </main>
        <footer>
            <div class="footer-links">
                <div>
                    <h4>关于我们</h4>
                    <ul>
                        <li><a href="#">公司简介</a></li>
                        <li><a href="#">团队介绍</a></li>
                        <li><a href="#">联系我们</a></li>
                    </ul>
                </div>
                <div>
                    <h4>服务支持</h4>
                    <ul>
                        <li><a href="#">帮助中心</a></li>
                        <li><a href="#">客户服务</a></li>
                        <li><a href="#">在线咨询</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-info">
                <p>版权所有 &copy; 2023 大多数据</p>
                <p>地址：北京市朝阳区xx街道xx号xx大厦xx层</p>
                <p>联系电话：010-12345678</p>
            </div>
        </footer>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            carouselItems: [
                { imgUrl: require("../image/image1.jpg") },
                { imgUrl: require("../image/image2.jpg") },
                { imgUrl: require("../image/image3.jpg") },
            ],
            content: [
                { imgUrl: require("../image/image1.jpg"), title: "标题1", content: "内容1" },
                { imgUrl: require("../image/image2.jpg"), title: "标题2", content: "内容2" },
                { imgUrl: require("../image/image3.jpg"), title: "标题3", content: "内容3" },
                // 更多内容卡片
            ],

        };
    },


};
</script>
  
<style scoped>
/* Reset styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Global styles */
body {
    font-family: "Microsoft YaHei", sans-serif;
    /* background-color: #f1f1f1; */
    color: #333;
}

#app {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f1f1f1;
}

/* Header styles */
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
}

nav ul {
    list-style: none;
    display: flex;
}

nav ul li {
    margin-right: 20px;
}

nav ul li a {
    color: #333;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
}

.search input[type="text"] {
    padding: 10px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    width: 200px;
}

.search button {
    padding: 10px 20px;
    /* background-color: #fff; */
    border: none;
    border-radius: 5px;
    font-size: 16px;
    margin-left: 10px;
}

/* Main styles */
main {
    display: flex;
    flex-wrap: wrap;
}

.carousel {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    margin-bottom: 10px;
}

.content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.card {
    flex-basis: calc(33.33% - 20px);
    margin-bottom: 20px;
    background-color: #fff;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.card img {
    width: 100%;
    height: auto;
    object-fit: cover;
}

.card-content {
    padding: 20px;
}

.card-content h3 {
    margin-bottom: 10px;
    font-size: 20px;
    font-weight: bold;
}

/* Footer styles */
footer {
    background-color: #0e294e;
    color: #fff;
    padding: 40px;
    text-align: center;
}

.footer-links {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.footer-links div {
    margin-right: 40px;
}

.footer-links h4 {
    margin-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
}

.footer-links ul {
    list-style-type: none;
}

.footer-links ul li {
    margin-bottom: 10px;
}

.footer-links ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 16px;
}

.footer-info p {
    margin-bottom: 10px;
    font-size: 14px;
}

.el-carousel {
    width: 100%;
}
</style>
  