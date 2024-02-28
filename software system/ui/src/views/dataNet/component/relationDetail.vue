<template>
  <!-- <el-dialog :visible="visible"
             title="关系详情"
             append-to-body
             :before-close="handleClose"
             width="50%"> -->
  <el-dialog :visible="visible"
             title="Relationship Details"
             append-to-body
             :before-close="handleClose"
             width="50%">
    <el-row>
      <el-col :span="8">
        <div class="image-container">
          <img v-show="data.image"
               class="data-image"
               :src="data.image" />
          <img v-show="!data.image"
               class="data-image"
               src="../../../image/relation/data.jpg" />
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
      </el-col>
      <el-col :span="8">
        <div class="image-container">
          <img class="data-image1"
               src="../../../image/relation.jpg" />
        </div>
        <p class="data-theme"
           style="text-align: center;"><span class="text">Relationship Name：</span>{{ relate.name }}</p>
        <p class="data-theme"
           style="text-align: center;"><img class="relation-image"
               src="../../../image/time.png" /><span class="text">Time：</span>{{ relate.time }}</p>
        <p class="data-theme"
           style="text-align: center;"><img class="relation-image"
               src="../../../image/topic.png" /><span class="text">Theme：</span>{{ relate.topic }}</p>
        <p class="data-coordinates"
           style="text-align: center;"><img class="relation-image"
               src="../../../image/space.png" /><span class="text">Space：</span>{{ relate.space }}
        </p>
      </el-col>
      <el-col :span="8">
        <div class="image-container">
          <img v-show="data.image"
               class="data-image"
               :src="data.image" />
          <img v-show="!data.image"
               class="data-image"
               src="../../../image/relation/data1.jpg" />
        </div>
        <div class="data-info-container">
          <p class="data-theme"><span class="text">Name：</span>{{ data1.name }}</p>
          <p class="data-theme"><span class="text">Time：</span>{{ data1.dateTime }}</p>
          <p class="data-theme"><span class="text">Theme：</span>{{ data1.subject }}</p>
          <p class="data-coordinates"><span class="text">Coordinates：</span>{{ data1.coordinate }}</p>
          <p class="data-keywords"><span class="text">Keywords：</span>{{ data1.mainWord }}</p>
          <p class="data-theme"><span class="text">Data Centres：</span>{{ data1.origin }}</p>
          <p class="data-links">
            <span class="text">Related Links：</span><a :href="data1.url"
               target="_blank">{{ data1.url }}</a>
          </p>
        </div>
      </el-col>
    </el-row>

    <div slot="footer">
      <el-button @click="handleClose">close</el-button>
    </div>
  </el-dialog>
</template>
  
<script>
export default {
  data () {
    return {
      data: {
        name: "Notes and observations made of Antarctic Petrels and Silver Grey Fulmars in the Windmill Islands, 1972",
        dateTime: "1972-9-20 08:00:00",
        subject: "ANIMALS/VERTEBRATES BIRDS",
        coordinate: "Antarctica",
        mainWord: "Birds",
        origin: "SystemNature",
        url: "https://data.gov.au/dataset/ds-aodn-cdf322b2-08bc-480d-a410-665ebff75362?q="
      },
      data1: {
        name: "PIROP Northwest Atlantic",
        dateTime: "2021-3-24 08:00:00",
        subject: "ANIMALS/VERTEBRATES BIRDS, MAMMALS",
        coordinate: "Antarctica",
        mainWord: "Waterfowl, Waterbirds, Songbirds",
        origin: "Canadian Wildlife Service",
        url: "https://www.gbif.org/dataset/b49a165b-6022-4b09-a443-1551c8eb0535#description"
      },
      relate: {
        name: "Birds",
        space: "Equals-1",
        time: "Before-0.083",
        topic: "0.969"
      }
    }
  },
  props: {
    visible: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    handleClose () {
      this.$emit("closeRelationDetail");
    },
  },
};
</script>
  
<style scoped>
.image-container {
  flex: 1 1 100%;
  text-align: center;
}

.data-image {
  max-width: 100%;
  height: 200px;
  object-fit: contain;
}

.data-image1 {
  max-width: 50%;
  height: 200px;
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

.relation-image {
  width: 50px;
  height: 50px;
  object-fit: cover;
}
</style>