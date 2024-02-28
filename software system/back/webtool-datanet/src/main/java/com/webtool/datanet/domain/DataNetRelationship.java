package com.webtool.datanet.domain;

import lombok.Data;
import org.neo4j.ogm.annotation.EndNode;
import org.neo4j.ogm.annotation.RelationshipEntity;
import org.neo4j.ogm.annotation.StartNode;
import org.springframework.data.neo4j.core.schema.*;

/**
 * @Author liujiandong
 * @Date 2023/5/12&14:59
 * @Description
 */

/**
 * @Property 注解用于定义单个属性，通常用于标注在实体类的字段上，指定该字段映射到节点或关系的一个属性
 * @Properties 注解用于定义多个属性，通常用于标注在实体类的方法上，指定该方法返回一个 Map<String, Object>
 * 使用@Property注解时，如果属性名与注解的值相同，则可以省略注解的值
 */
@Data
@RelationshipEntity(type = "related_to")
public class DataNetRelationship {

    @Id
    @GeneratedValue
    private Long id;

    @StartNode
    private DataNetNode startNode;

    @EndNode
    private DataNetNode endNode;

    @Property(name = "startNodeId")
    private Long startNodeId;

    @Property(name = "endNodeId")
    private Long endNodeId;

    @Property(name = "relationName")
    private String relationName;

    @Property(name = "typeName")
    private String typeName;

    @Property(name = "time")
    private String time;

    @Property(name = "space")
    private String space;

    @Property(name = "topic")
    private String topic;

}
