<template>
    <div class="container">
        <svg style="background-color: #409EFF; border-radius: 50%;" :width="width" :height="height" ref="test"
            @mousemove="listener($event)">
            <a class="fontA" :href="tag.href" v-for="(tag, index) in tags" :key="tag.id" @mouseenter="mouseenter($event)"
                @mouseleave="mouseleave($event)">
                <text :x="tag.x" :y="tag.y" :fill="colors[index]" :font-size="tag.size" :fill-opacity="(400 + tag.z) / 600">
                    {{ tag.label }}
                </text>
            </a>
        </svg>
    </div>
</template>
<script>
export default {
    name: "word-cloud",
    //数据，宽，高，半径，半径一般位宽高的一半。
    data() {
        return {
            data: [
                { label: "地球大数据", value: "10", weight: 100 },
                { label: "科学研究", value: "10", weight: 11 },
                { label: "地球科学", value: "10", weight: 22 },
                { label: "数据分析", value: "10", weight: 33 },
                { label: "环境监测", value: "10", weight: 44 },
                { label: "地理信息", value: "10", weight: 55 },
                { label: "遥感技术", value: "10", weight: 66 },
                { label: "气候变化", value: "10", weight: 77 },
                { label: "地震预警", value: "10", weight: 88 },
                { label: "海洋科学", value: "10", weight: 99 },
                { label: "遥感数据", value: "10", weight: 56 },
                { label: "空间数据", value: "10", weight: 66 },
                { label: "数据安全", value: "10", weight: 77 },
                { label: "数据治理", value: "10", weight: 1 },
                { label: "数据可视化", value: "10", weight: 122 },
                { label: "数据挖掘", value: "10", weight: 33 },
                { label: "人工智能", value: "10", weight: 44 },
                { label: "地球观测", value: "10", weight: 55 },
                { label: "地球教育", value: "10", weight: 66 },
                { label: "环境保护", value: "10", weight: 77 },
                { label: "可持续发展", value: "10", weight: 88 },
                { label: "地球资源", value: "10", weight: 99 },
            ]
            ,
            width: 500, //svg宽度
            height: 380, //svg高度
            tagsNum: 0, //标签数量
            RADIUS: 250, //球的半径
            speedX: Math.PI / 360 / 1.5, //球一帧绕x轴旋转的角度
            speedY: Math.PI / 360 / 1.5, //球-帧绕y轴旋转的角度
            tags: [],
            timer: null,
            minSize: 14,
            maxSize: 44,
            colors: [], //存储颜色
        };
    },
    computed: {
        CX() {
            //球心x坐标
            return this.width / 2;
        },
        CY() {
            //球心y坐标
            return this.height / 2;
        },
    },
    created() {
        //初始化标签位置
        this.changeColors();
        let tags = [];
        this.tagsNum = this.data.length;
        for (let i = 0; i < this.data.length; i++) {
            let tag = {};
            let k = -1 + (2 * (i + 1) - 1) / this.tagsNum;
            let a = Math.acos(k);
            let b = a * Math.sqrt(this.tagsNum * Math.PI); //计算标签相对于球心的角度

            tag.label = this.data[i].label;
            tag.value = this.data[i].value;
            let size = this.minSize + parseInt((this.data[i].weight / 100) * 20)
            tag.size = size > this.maxSize ? this.maxSize : size;
            // tag.href = "";

            tag.x = this.CX + this.RADIUS * Math.sin(a) * Math.cos(b); //根据标签角度求出标签的x,y,z坐标
            tag.y = this.CY + this.RADIUS * Math.sin(a) * Math.sin(b);
            tag.z = this.RADIUS * Math.cos(a);
            tags.push(tag);
        }
        this.tags = tags;
    },

    mounted() {
        this.timer = setInterval(() => {
            this.rotateX(this.speedX);
            this.rotateY(this.speedY);
        }, 17);
    },
    methods: {
        // 纵向
        rotateX(angleX) {
            var cos = Math.cos(angleX);
            var sin = Math.sin(angleX);
            for (let tag of this.tags) {
                var y1 = (tag.y - this.CY) * cos - tag.z * sin + this.CY;
                var z1 = tag.z * cos + (tag.y - this.CY) * sin;
                tag.y = y1;
                tag.z = z1;
            }
        },

        // 横向
        rotateY(angleY) {
            var cos = Math.cos(angleY);
            var sin = Math.sin(angleY);
            for (let tag of this.tags) {
                var x1 = (tag.x - this.CX) * cos - tag.z * sin + this.CX;
                var z1 = tag.z * cos + (tag.x - this.CX) * sin;
                tag.x = x1;
                tag.z = z1;
            }
        },

        // 监听鼠标方向
        listener(e) {
            var x = e.clientX - this.CX;
            var y = e.clientY - this.CY;
            if (x * 0.0001 > 0 && y * 0.0001 > 0) {
                this.speedX = -Math.min(this.RADIUS * 0.00002, x * 0.0002);
                this.speedY = -Math.min(this.RADIUS * 0.00002, y * 0.0002);
            } else if (x * 0.0001 < 0 && y * 0.0001 < 0) {
                this.speedX = -Math.max(-this.RADIUS * 0.00002, x * 0.0002);
                this.speedY = -Math.max(-this.RADIUS * 0.00002, y * 0.0002);
            } else {
                this.speedX =
                    x * 0.0001 > 0
                        ? Math.min(this.RADIUS * 0.00002, x * 0.0001)
                        : Math.max(-this.RADIUS * 0.00002, x * 0.0001);
                this.speedY =
                    y * 0.0001 > 0
                        ? Math.min(this.RADIUS * 0.00002, y * 0.0001)
                        : Math.max(-this.RADIUS * 0.00002, y * 0.0001);
            }
        },

        // 鼠标进入文字
        mouseenter(e) {
            // 修改透明度
            let doms = document.getElementsByClassName('fontA');
            for (let i = 0; i < doms.length; i++) {
                doms[i].childNodes[0].style.fillOpacity = '0.3';
            }
            e.target.childNodes[0].style.fillOpacity = 1;

            // 停止动画
            clearInterval(this.timer);
            this.timer = null;
        },

        // 鼠标离开文字
        mouseleave() {
            // 修改透明度
            let doms = document.getElementsByClassName('fontA');
            for (let i = 0; i < doms.length; i++) {
                doms[i].childNodes[0].style.fillOpacity = '';
            }

            // 开始动画
            if (this.timer) {
                clearInterval(this.timer);
                this.timer = null;
            }
            this.timer = setInterval(() => {
                this.rotateX(this.speedX);
                this.rotateY(this.speedY);
            }, 17);
        },

        // 颜色
        changeColors() {
            //随机变色
            for (var i = 0; i < 22; i++) {
                var r = Math.floor(Math.random() * 256);
                var g = Math.floor(Math.random() * 256);
                var b = Math.floor(Math.random() * 256);
                this.colors[i] = "rgb(" + r + "," + g + "," + b + ")";
            }
        },
    }
};
</script>
  
  
<style lang="scss" scoped>
.container {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
}

.fontA {
    font-weight: bold;
    font-family: Apple LiGothic Medium;
    fill: #333;
    /* Set the desired text color */
}
</style>
  