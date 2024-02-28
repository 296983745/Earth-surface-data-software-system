package com.webtool.datanet.service.impl;

import com.webtool.datanet.GephiUtil;
import com.webtool.datanet.domain.DataNetNode;
import com.webtool.datanet.domain.DataNetNodeDTO;
import com.webtool.datanet.domain.DataNetRelationship;
import com.webtool.datanet.mapper.DataNetRelationshipRepository;
import com.webtool.datanet.mapper.DataNetRepository;
import com.webtool.datanet.service.DataNetService;
import org.gephi.graph.api.GraphModel;
import org.gephi.graph.api.Node;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Author liujiandong
 * @Date 2023/5/12&15:46
 * @Description
 */
@Service
public class DataNetServiceImpl implements DataNetService {

    @Autowired
    DataNetRepository dataNetRepository;

    @Autowired
    DataNetRelationshipRepository dataNetRelationshipRepository;

    /**
     *  查询关联网络
     * @param nodeName
     * @param limit
     * @return
     */
    @Override
    public Map<String, Object> getAll(String nodeName, Integer limit) {
        List<DataNetNode> nodeList;
        if (StringUtils.isEmpty(nodeName)) {
            nodeList = dataNetRepository.findNodesWithLimit(limit);
        } else {
            nodeList = dataNetRepository.findByDataNameContainingIgnoreCase(nodeName);
        }
        // 查出所有的关系，进行过滤
        List<DataNetRelationship> all = dataNetRelationshipRepository.findAll();
        //  通过id进行映射
        Map<Integer, DataNetNode> nodeMap = new HashMap<>(nodeList.size());
        Map<Integer, DataNetRelationship> startRelationshipHashMap = new HashMap<>();
        Map<Integer, DataNetRelationship> endRelationshipHashMap = new HashMap<>();
        // 创建节点映射，便于根据节点 ID 进行查找
        for (DataNetNode node : nodeList) {
            nodeMap.put(Math.toIntExact(node.getId()), node);
        }
        List<DataNetRelationship> filterRelationships = new ArrayList<>();
        List<DataNetNode> filterDataNetNodeList = new ArrayList();
        //过滤节点不存在的关系
        Integer startNodeId;
        Integer endNodeId;
        for (DataNetRelationship nodeRelationship : all) {
            startNodeId = Math.toIntExact(nodeRelationship.getStartNodeId());
            endNodeId = Math.toIntExact(nodeRelationship.getEndNodeId());
            if (nodeMap.get(startNodeId) != null && nodeMap.get(endNodeId) != null) {
                filterRelationships.add(nodeRelationship);
                startRelationshipHashMap.put(startNodeId, nodeRelationship);
                endRelationshipHashMap.put(endNodeId, nodeRelationship);
            }
        }
        //过滤掉没有关系的节点
//        for (DataNetNode node : nodeList) {
//            if (startRelationshipHashMap.get(Math.toIntExact(node.getId())) != null || endRelationshipHashMap.get(Math.toIntExact(node.getId())) != null) {
//                filterDataNetNodeList.add(node);
//            }
//        }
        try {
            return layoutAlgorithm(nodeList, filterRelationships);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    @Override
    public List<DataNetNode> getByName(String name) {
        return dataNetRepository.findByDataNameContainingIgnoreCase(name);
    }


    public Map<String, Object> layoutAlgorithm(List<DataNetNode> netNodeList, List<DataNetRelationship> relationships) throws Exception {
        Map<String, Object> result = new HashMap<>(2);
        //统计每个节点作为边初始节点的初始节点的条数
        Map<Long, Integer> occurrences = new HashMap<>(relationships.size());

        for (DataNetRelationship dataNetRelationship : relationships) {
            if (occurrences.containsKey(dataNetRelationship.getStartNodeId())) {
                occurrences.put(dataNetRelationship.getStartNodeId(), occurrences.get(dataNetRelationship.getStartNodeId()) + 1);
            } else {
                occurrences.put(dataNetRelationship.getStartNodeId(), 1);
            }
        }
        // 创建图模型 导入边，点
        GraphModel graphModel = GephiUtil.createGraphModel(netNodeList, relationships);
        // 运行布局算法
        GephiUtil.runLayoutAlgorithm(graphModel);
        Node[] nodes = graphModel.getGraph().getNodes().toArray();
        Map<Integer, Node> nodeMap = new HashMap<>();
        // 找出节点中坐标x , y 的最大最小值
        float maxX = 0, minX = 0;
        float maxY = 0, minY = 0;
        for (Node node : nodes) {
            if (node.x() < minX) {
                // 更新x最小值
                minX = node.x();
            }
            if (node.y() < minY) {
                // 更新y最小值
                minY = node.y();
            }
            if (node.x() > maxX) {
                // 更新x最大值
                maxX = node.x();
            }
            if (node.y() > maxY) {
                // 更新y最大值
                maxY = node.y();
            }
            nodeMap.put((int) node.size(), node);
        }
        Integer canvasX = 1920, canvasY = 950;
        Float x = maxX - minX, y = maxY - minY;
        Float xRatio = x / canvasX, yRation = y / canvasY;
        System.out.println(xRatio + yRation);
        List<DataNetNodeDTO> nodeList = new ArrayList<>();
        DataNetNodeDTO dataNetNodeDTO = null;
        Node node = null;
        int netNodeSize = netNodeList.size();
        for (DataNetNode dataNetNode : netNodeList) {
            dataNetNodeDTO = new DataNetNodeDTO();
            BeanUtils.copyProperties(dataNetNode, dataNetNodeDTO);
            node = nodeMap.get(Integer.valueOf(dataNetNode.getId().toString()));
            dataNetNodeDTO.setX(String.valueOf(node.x() / xRatio));
            dataNetNodeDTO.setY(String.valueOf(node.y() / yRation));
            if (netNodeSize > 100) {
                dataNetNodeDTO.setSize(Float.valueOf(occurrences.get(dataNetNode.getId()) == null ? 3 : occurrences.get(dataNetNode.getId()) < 20 ? occurrences.get(dataNetNode.getId()) : 20));
            } else {
                dataNetNodeDTO.setSize(Float.valueOf(occurrences.get(dataNetNode.getId()) == null ? 5 : occurrences.get(dataNetNode.getId()) < 20 ? 10 : 20));
            }
//            dataNetNodeDTO.setSize(occurrences.get(dataNetNode.getId()) == null ? 1 : occurrences.get(dataNetNode.getId()));
            nodeList.add(dataNetNodeDTO);
        }
        result.put("netNodeList", nodeList);
        result.put("relationships", relationships);
        return result;

    }
}
