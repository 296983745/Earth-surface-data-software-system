package com.webtool.datanet.service.impl;

import com.webtool.datanet.domain.DataNetNode;
import com.webtool.datanet.domain.DataNetRelationship;
import com.webtool.datanet.mapper.DataNetRelationshipRepository;
import com.webtool.datanet.service.DataNetRelationshipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @Author liujiandong
 * @Date 2023/5/12&16:33
 * @Description
 */
@Service
public class DataNetRelationshipServiceImpl implements DataNetRelationshipService {

    @Autowired
    DataNetRelationshipRepository dataNetRelationshipRepository;

    @Override
    public DataNetRelationship addRelationship(DataNetNode startNode, DataNetNode toNode, String space,String time,String topic) {
        DataNetRelationship dataNetRelationship = new DataNetRelationship();
        //添加属性
        dataNetRelationship.setStartNode(startNode);
        dataNetRelationship.setStartNodeId(startNode.getId());
        dataNetRelationship.setEndNode(toNode);
        dataNetRelationship.setEndNodeId(toNode.getId());
        dataNetRelationship.setTypeName(startNode.getMainOfKind());
        dataNetRelationship.setRelationName(startNode.getSubject());
        dataNetRelationship.setSpace(space);
        dataNetRelationship.setTime(time);
        dataNetRelationship.setTopic(topic);
        return  dataNetRelationship;
    }

}
