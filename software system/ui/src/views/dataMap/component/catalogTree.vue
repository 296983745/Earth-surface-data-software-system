<template>
    <div>
        <el-tree :data="data" :props="defaultProps" node-key="id" :expand-on-click-node="false"
            @node-click="handleNodeClick"></el-tree>
    </div>
</template>
  
<script>
export default {
    name: 'TreeComponent',
    props: {
        data: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            defaultProps: {
                children: 'children',
                label: 'label',
            },
        };
    },
    methods: {
        handleNodeClick(data) {
            // 处理节点点击事件
            console.log('点击了节点:', data);
            this.$emit('handleNodeClick', data);
        },
        close() {
            this.$emit('closeTree');
        },
    },
};
</script>
  