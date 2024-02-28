package com.webtool.datanet.service;

import com.webtool.datanet.domain.DataNetNode;
import com.webtool.datanet.domain.DataNetRelationship;

/**
 * @Author liujiandong
 * @Date 2023/5/12&16:32
 * @Description
 */
public interface DataNetRelationshipService {
    DataNetRelationship addRelationship(DataNetNode startNode, DataNetNode toNode, String space,String time,String topic);
}
