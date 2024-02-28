package com.webtool.datanet.mapper;

import com.webtool.datanet.domain.DataNetNode;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Author liujiandong
 * @Date 2023/5/12&15:44
 * @Description
 */
@Repository
public interface DataNetRepository extends Neo4jRepository<DataNetNode, Long> {

    List<DataNetNode> findByDataNameContainingIgnoreCase(@Param("DataName") String DataName);

    @Query("MATCH (n:DataNetNode) RETURN n LIMIT ($limit)")
    List<DataNetNode> findNodesWithLimit(@Param("limit") int limit);

    @Query("match (n:DataNetNode) where n.DataName Contains ($keyWord) return n")
    List<DataNetNode> findByKeyWord(@Param("keyWord") String keyWord);




}
