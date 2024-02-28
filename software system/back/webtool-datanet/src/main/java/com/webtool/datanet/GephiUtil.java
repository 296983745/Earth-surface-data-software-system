package com.webtool.datanet;

import com.webtool.datanet.domain.DataNetNode;
import com.webtool.datanet.domain.DataNetRelationship;
import org.gephi.graph.api.*;
import org.gephi.layout.plugin.AutoLayout;
import org.gephi.layout.plugin.force.StepDisplacement;
import org.gephi.layout.plugin.force.yifanHu.YifanHuLayout;
import org.gephi.layout.plugin.forceAtlas.ForceAtlasLayout;
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2;
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2Builder;
import org.gephi.layout.plugin.fruchterman.FruchtermanReingold;
import org.gephi.layout.plugin.fruchterman.FruchtermanReingoldBuilder;
import org.gephi.layout.plugin.openord.OpenOrdLayout;
import org.gephi.layout.spi.Layout;
import org.gephi.layout.spi.LayoutBuilder;
import org.gephi.project.api.ProjectController;
import org.openide.util.Lookup;

import java.util.List;
import java.util.concurrent.TimeUnit;

public class GephiUtil {


    public static GraphModel createGraphModel(List<DataNetNode> netNodeList, List<DataNetRelationship> relationships) {
        ProjectController projectController = Lookup.getDefault().lookup(ProjectController.class);
        projectController.newProject();
        GraphController graphController = Lookup.getDefault().lookup(GraphController.class);
        GraphModel graphModel = graphController.getGraphModel();
        UndirectedGraph undirectedGraph = graphModel.getUndirectedGraph();

        for (DataNetNode dataNetNode : netNodeList) {
            Node node = graphModel.factory().newNode(dataNetNode.getId().toString());
            node.setLabel(dataNetNode.getDataName());
            node.setSize(dataNetNode.getId());
            undirectedGraph.addNode(node);
        }

        for (DataNetRelationship dataNetRelationship : relationships) {
            Node startNode = undirectedGraph.getNode(dataNetRelationship.getStartNodeId().toString());
            Node endNode = undirectedGraph.getNode(dataNetRelationship.getEndNodeId().toString());
            Edge edge = graphModel.factory().newEdge(startNode, endNode, 1, false);
            undirectedGraph.addEdge(edge);
        }

        return graphModel;
    }


    /**
     * 导入节点数据
     *
     * @param list
     * @param graphModel
     */
    public static void importNodes(List<DataNetNode> list, GraphModel graphModel) {
        for (DataNetNode dataNetNode : list) {
            Graph nodeTable = graphModel.getGraph();
            // 将节点添加到图模型中
            Node graphNode = graphModel.factory().newNode();
            // 设置节点标签
            graphNode.setLabel(dataNetNode.getDataName());
            graphNode.setSize(dataNetNode.getId());
            nodeTable.addNode(graphNode);
        }
    }

    /**
     * 导入边数据
     */
    public static void importEdges(List<DataNetRelationship> list, GraphModel graphModel) {
        Node[] nodes = graphModel.getGraph().getNodes().toArray();
        for (DataNetRelationship dataNetRelation : list) {
            Node startNode = null;
            Node endNode = null;
            // 查找起始节点和结束节点
            for (Node node : nodes) {
                if (node.getLabel().equals(dataNetRelation.getStartNode().getDataName())) {
                    startNode = node;
                } else if (node.getLabel().equals(dataNetRelation.getEndNode().getDataName())) {
                    endNode = node;
                }
                if (startNode != null && endNode != null) {
                    break;
                }
            }
            // 如果起始节点或结束节点为空，跳过该边
            if (startNode == null || endNode == null) {
                continue;
            }
            // 将边添加到图模型中
            Edge edge = graphModel.factory().newEdge(startNode, endNode);
            edge.setLabel(dataNetRelation.getRelationName());
            graphModel.getGraph().addEdge(edge);
        }
    }

    /**
     * 运行布局算法
     *
     * @param graphModel
     */

    public static void runLayoutAlgorithm(GraphModel graphModel) {
        method1(graphModel);
    }

    public static void method1(GraphModel graphModel) {
        try {
            AutoLayout autoLayout = new AutoLayout(10, TimeUnit.SECONDS);
            autoLayout.setGraphModel(graphModel);

            // 创建第一个布局算法实例：YifanHuLayout
            YifanHuLayout firstLayout = new YifanHuLayout(null, new StepDisplacement(1f));
            // 设置节点之间的最优距离
            int nodes = graphModel.getGraph().getNodes().toArray().length;
            //客观距离
            firstLayout.setOptimalDistance(600f);
            // 设置初始步长
            firstLayout.setInitialStep(100f);
            // 设置步长缩放比例
            firstLayout.setStepRatio(0.9f);
            // 设置收敛阈值
            firstLayout.setConvergenceThreshold(0.5f);

            // 创建第二个布局算法实例：ForceAtlasLayout
            ForceAtlasLayout secondLayout = new ForceAtlasLayout(null);
            secondLayout.resetPropertiesValues();

            // 将第一个布局算法添加到自动布局中，权重为 0.5
            autoLayout.addLayout(firstLayout, 0.6f);

            // 将第二个布局算法添加到自动布局中，权重为 0.5，并应用动态属性
            autoLayout.addLayout(secondLayout, 0.4f);

            // 执行自动布局
            autoLayout.execute();
        } catch (Exception e) {
            // 异常处理
            e.printStackTrace();
        }
    }

    public static void method2(GraphModel graphModel) {
        // ForceAtlas2布局算法
        ForceAtlas2 layout = new ForceAtlas2(null);
        layout.setGraphModel(graphModel);
        layout.resetPropertiesValues();
        layout.setAdjustSizes(true);   // 缩放
        layout.setScalingRatio(2.0d);  // 缩放比例
        layout.setEdgeWeightInfluence(0.8d);  // 边的权重的影响（你给多少影响到边的权重。0"没有影响”，1是“正常”）
        layout.setGravity(0.1d);  // 重力（吸引到中心节点。防止岛屿渐行渐远）
        layout.setLinLogMode(true); // LinLog模式（切换ForceAtlas模型的线性-线性坐标系到线性-对数坐标系，使团块更紧凑）
        layout.setStrongGravityMode(false); // 更强的重力（一个强有力的万有引力定律）
        layout.setThreadsCount(256);  // 线程数（如果你的内核可以处理更多的线程意味着更快的速度）
        layout.initAlgo();
        for (int i = 0; i < 30000 && layout.canAlgo(); i++) {
            layout.goAlgo();
        }
        layout.endAlgo();
    }

    public static void method3(GraphModel graphModel) {
        // Fruchterman Reingold布局算法
        System.out.println("开始进行布局--------------------------------");
        FruchtermanReingold layout = new FruchtermanReingold(null);
        layout.setGraphModel(graphModel);
        layout.resetPropertiesValues();
        layout.setArea(100000.0f);  // 区域（图形大小面积）
        layout.setGravity(1.0d); // 重力（这种力量吸引了所有节点的中心，以避免失连接部件的分散）
        layout.setSpeed(1.0d); // 速度（以精度损失为代价，提高收敛速度）
        layout.initAlgo();
        for (int i = 0; i < 20000; i++) {
            layout.goAlgo();
        }
        System.out.println("布局结束--------------------------------");
    }
    public static void method4(GraphModel graphModel) {
        // Fruchterman Reingold布局算法
        System.out.println("开始进行布局--------------------------------");
        // YifanHuLayout布局算法
        YifanHuLayout layout = new YifanHuLayout(null, new StepDisplacement(1f));
        layout.setGraphModel(graphModel);
        layout.resetPropertiesValues();
        layout.setOptimalDistance(500.0f);  // 设置最佳距离(弹簧自然长度，更大的值意味着节点将相距较远)
        layout.setStep(10.0f);  // 设置初始步长（在整合阶段的初始步长。将此值设置为一个有意义的大小，相比于最佳距离，10%是一个很好的起点）
        layout.setStepRatio(0.95f); // 设置步比率（该比率用于更新各次迭代的步长）
        layout.setAdaptiveCooling(true); // 设置自适应冷却（控制自适应冷却的使用。它是用来帮助布局算法以避免能量局部极小）
        layout.initAlgo();
        for (int i = 0; i < 10000 && layout.canAlgo(); i++) {
            layout.goAlgo();
        }
        System.out.println("布局结束--------------------------------");
    }

    public static void method5(GraphModel graphModel){
        ForceAtlasLayout forceatLayout = new ForceAtlasLayout(null);
        forceatLayout.setGraphModel(graphModel);
        forceatLayout.initAlgo();
        forceatLayout.resetPropertiesValues();
        forceatLayout.setInertia(0.1);
        forceatLayout.setRepulsionStrength(15000.0);
        forceatLayout.setAttractionStrength(2.0);
        forceatLayout.setMaxDisplacement(20.0);
        forceatLayout.setFreezeBalance(true);
        forceatLayout.setFreezeStrength(80.0);
        forceatLayout.setFreezeInertia(0.2);
        forceatLayout.setGravity(35.0);
        forceatLayout.setSpeed(1.0);
        forceatLayout.setAdjustSizes(true);
        forceatLayout.setOutboundAttractionDistribution(false);
        for (int i = 0; i <= 1000 && forceatLayout.canAlgo(); i++) {
            if(i!=0 && i%10==0){
                System.out.println("已迭代"+i+"次...");
            }
            forceatLayout.goAlgo();
        }
        forceatLayout.endAlgo();
    }

}

