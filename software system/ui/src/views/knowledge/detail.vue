<template>
    <el-dialog :visible.sync="dialogVisible" width="70%" :before-close="handleClose">
        <video style="width: 100%;" ref="videoPlayer" :src="videoUrl" controls></video>
    </el-dialog>
</template>
  
<script>
export default {
    data() {
        return {
            dialogVisible: false,
            videoUrl: "",
        };
    },
    methods: {
        openDialog(url) {
            this.videoUrl = url;
            this.dialogVisible = true;
        },
        handleClose(done) {
            this.$refs.videoPlayer.pause();
            done();
        },
    },
};
</script>