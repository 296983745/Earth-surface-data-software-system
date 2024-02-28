package com.webtool.datanet.mapper;

import com.webtool.datanet.domain.DataNetRelationship;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Author liujiandong
 * @Date 2023/5/12&16:30
 * @Description
 */
@Repository
public interface DataNetRelationshipRepository extends Neo4jRepository<DataNetRelationship, Long> {

    List<DataNetRelationship> findAllByStartNodeId(Long nodeId);

    List<DataNetRelationship> findAllByEndNodeId(Long nodeId);
}
