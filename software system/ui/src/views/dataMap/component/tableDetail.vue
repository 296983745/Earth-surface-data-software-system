<template>
  <!-- <el-dialog :visible="visible"
             title="数据详情"
             append-to-body
             :before-close="handleClose"
             width="50%"> -->
  <el-dialog :visible="visible"
             title="Data Details"
             append-to-body
             :before-close="handleClose"
             width="50%">
    <div class="data-details-popup">
      <div class="image-container">
        <img v-show="data.image"
             class="data-image"
             :src="data.image" />
        <img v-show="!data.image"
             class="data-image"
             src="../../../image/noImage.jpg" />
      </div>
      <div class="data-info-container">
        <p class="data-theme"><span class="text">Name：</span>{{ data.name }}</p>
        <p class="data-theme"><span class="text">Time：</span>{{ data.dateTime }}</p>
        <p class="data-theme"><span class="text">Theme：</span>{{ data.subject }}</p>
        <p class="data-coordinates"><span class="text">Coordinates：</span>{{ data.coordinate }}</p>
        <p class="data-keywords"><span class="text">Keywords：</span>{{ data.mainWord }}</p>
        <p class="data-theme"><span class="text">Data Centres：</span>{{ data.origin }}</p>
        <p class="data-links">
          <span class="text">Related Links：</span><a :href="data.url"
             target="_blank">{{ data.url }}</a>
        </p>
      </div>
    </div>
    <div class="recommendations"
         v-if="recommendations">
      <h3>Related Data</h3>
      <div class="recommendation-item"
           v-for="recommendation in recommendations"
           :key="recommendation.id">
        <a :href="recommendation.url"
           target="_blank"><img class="recommendation-image"
               :src="recommendation.image" /></a>
        <p class="recommendation-name">{{ recommendation.name }}</p>
      </div>
    </div>
    <div slot="footer">
      <el-button @click="handleEvalute">Evaluation of the level of sharing</el-button>
      <el-button @click="handleClose">close</el-button>
    </div>
  </el-dialog>
</template>
  
<script>
export default {
  name: "DataDetailsPopup",
  data () {
    return {
    }
  },
  props: {
    visible: {
      type: Boolean,
      required: true,
    },
    data: {
      type: Object,
      required: true,
    },
    recommendations: {
      type: Array,
      required: false,
    },
  },
  methods: {
    handleClose () {
      this.$emit("closeDetail");
    },
    handleEvalute () {
      let url = this.data.url;
      this.$router.push({ path: "/evaluate", query: { url: url } });
    }
  },
};
</script>
  
<style scoped>
.data-details-popup {
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-container {
  flex: 1 1 100%;
  text-align: center;
}

.data-image {
  max-width: 100%;
  height: 320px;
  object-fit: contain;
}

.data-info-container {
  flex: 100%;
  display: flex;
  flex-direction: column;
  align-items: left;
  margin-top: 20px;
}

.data-theme,
.data-coordinates,
.data-keywords,
.data-links {
  margin-bottom: 10px;
  font-size: 16px;
}

.data-links a {
  color: #409eff;
  text-decoration: none;
}

.data-links a:hover {
  text-decoration: underline;
}

.text {
  font-weight: bold;
}

.recommendations {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
}

.recommendations h3 {
  font-size: 18px;
  font-weight: bold;
  width: 100%;
}

.recommendation-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
  width: 20%;
  text-align: center;
}

.recommendation-image {
  width: 120px;
  height: 120px;
  object-fit: cover;
  margin-bottom: 10px;
}

.recommendation-name {
  font-size: 14px;
}
</style>