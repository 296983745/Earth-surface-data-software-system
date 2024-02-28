package com.webtool;


import com.alibaba.fastjson.JSONObject;
import com.webtool.common.core.redis.RedisCache;
import com.webtool.datanet.domain.DataCatalog;
import com.webtool.datanet.domain.DataNetNode;
import com.webtool.datanet.domain.DataNetRelationship;
import com.webtool.datanet.mapper.DataCatalogMapper;
import com.webtool.datanet.mapper.DataNetRelationshipRepository;
import com.webtool.datanet.mapper.DataNetRepository;
import com.webtool.datanet.service.DataNetRelationshipService;
import com.webtool.datanet.service.DataNetService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.text.ParseException;
import java.util.*;


@SpringBootTest
public class test {

    @Autowired
    DataNetRepository dataNetRepository;
    @Autowired
    DataNetRelationshipService dataNetRelationshipService;
    @Autowired
    DataNetRelationshipRepository dataNetRelationshipRepository;
    @Autowired
    private DataNetService dataNetService;
    @Autowired
    private RedisCache redisCache;

    @Autowired
    DataCatalogMapper dataCatalogMapper;


    @Test
    void contextLoads() {
        List<Map> list = dataCatalogMapper.getTestData();
        List<Map> edges = dataCatalogMapper.getedges();
        List<DataNetNode> dataNetNodes = new ArrayList<>();
        Map<String, DataNetNode> netNodeHashMap = new HashMap<>();
        for (Map map : list) {
            DataNetNode dataNetNode = JSONObject.parseObject(JSONObject.toJSONString(map), DataNetNode.class);
            dataNetNode.setDataName(String.valueOf(map.get("name")));
            dataNetNodes.add(dataNetNode);
            netNodeHashMap.put(String.valueOf(dataNetNode.getId()),dataNetNode);
            dataNetRepository.save(dataNetNode);
        }
        for (Map map: edges) {
            DataNetRelationship dataNetRelationship = dataNetRelationshipService.addRelationship(netNodeHashMap.get(String.valueOf(map.get("start"))), netNodeHashMap.get(String.valueOf(map.get("end"))),map.get("space_value").toString(),map.get("time_value").toString(),map.get("content_value").toString());
            dataNetRelationshipRepository.save(dataNetRelationship);
        }


    }

    @Test
    void test() throws ParseException {
        Map<String, Object> all = dataNetService.getAll("", 1000);
        redisCache.setCacheObject("dataNet", all);
    }

    private static double generateRandomCoordinate(double min, double max) {
        Random random = new Random();
        return min + (max - min) * random.nextDouble();
    }

    /**
     * 在[beginStr,endStr]生成随机日期+时间
     *
     * @param beginStr
     * @param endStr
     * @return
     */

    /**
     * 随机生成时间
     * 使用Math.random()方法---返回一个在介于(0,1)的随机数
     *
     * @param begin
     * @param end
     * @return
     */
    private static long random(long begin, long end) {
        long rand = begin + (long) (Math.random() * (end - begin));
        if (rand == begin || rand == end) {
            return random(begin, end);
        }
        return rand;
    }
}
