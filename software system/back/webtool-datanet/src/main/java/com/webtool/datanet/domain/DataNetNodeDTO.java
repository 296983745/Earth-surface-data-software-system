package com.webtool.datanet.domain;

import lombok.Data;
import org.springframework.data.neo4j.core.schema.GeneratedValue;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Property;

/**
 * @author Administrator
 */
@Data
public class DataNetNodeDTO {

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

    private String x;
    private String y;
    private Float size;

}
