package com.webtool.datanet.domain;

import lombok.Data;
import org.neo4j.ogm.annotation.NodeEntity;
import org.springframework.data.neo4j.core.schema.GeneratedValue;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Property;

/**
 * @Author liujiandong
 * @Date 2023/5/12&14:56
 * @Description
 */
@Data
@NodeEntity(label = "DataNetNode")
public class DataNetNode {
    @Id
    @GeneratedValue
    private Long id;

    @Property(name = "DataName")
    private String dataName;

    @Property(name = "DateTime")
    private String dateTime;

    @Property(name = "SpacePlc")
    private String spacePlc;

    @Property(name = "MainWord")
    private String mainWord;

    @Property(name = "Subject")
    private String subject;

    @Property(name = "MainOfKind")
    private String mainOfKind;

    @Property(name = "PlayIn")
    private String playIn;

}
