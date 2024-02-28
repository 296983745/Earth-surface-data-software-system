package com.webtool.datanet.service.impl;

import java.util.*;

import com.alibaba.fastjson2.JSONObject;
import com.webtool.common.utils.DateUtils;
import com.webtool.datanet.domain.DataCatalog;
import com.webtool.datanet.domain.DataCatalogStatistics;
import com.webtool.datanet.domain.DataNetRelationship;
import com.webtool.datanet.mapper.DataCatalogMapper;
import com.webtool.datanet.mapper.DataNetRelationshipRepository;
import com.webtool.datanet.service.IDataCatalogService;
import org.jfree.chart.LegendItemSource;
import org.neo4j.ogm.json.JSONException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.listener.Topic;
import org.springframework.stereotype.Service;

/**
 * 【数据目录】Service业务层处理
 *
 * @author webtool
 * @date 2023-05-31
 */
@Service
public class DataCatalogServiceImpl implements IDataCatalogService {
    @Autowired
    private DataCatalogMapper dataCatalogMapper;

    @Autowired
    private DataNetRelationshipRepository dataNetRelationshipRepository;

    /**
     * 查询【数据目录】
     *
     * @param id 【数据目录】主键
     * @return 【数据目录】
     */
    @Override
    public DataCatalog selectDataCatalogById(Long id) {
        return dataCatalogMapper.selectDataCatalogById(id);
    }

    @Override
    public Map<String, Object> selectDataCatalogByName(String name) {
        DataCatalog dataCatalog = dataCatalogMapper.selectDataCatalogByName(name).get(0);
        List<DataNetRelationship> dataArray = dataNetRelationshipRepository.findAllByStartNodeId(Long.valueOf(dataCatalog.getId()));
        //将获取到的关系进行处理
        //1.按照主题相关度进行排序
        Collections.sort(dataArray, new TopicComparator());
        List<DataNetRelationship> relate = dataArray.subList(0, Math.min(5, dataArray.size()));
        List<JSONObject> jsonObjects = new ArrayList<>();
        for (int i = 0; i < relate.size(); i++) {
            DataCatalog dataCatalog1 = dataCatalogMapper.selectDataCatalogById(relate.get(i).getEndNodeId());
            JSONObject jsonObject = new JSONObject();
            if (dataCatalog1 != null) {
                jsonObject.put("name", dataCatalog1.getName());
                jsonObject.put("image", dataCatalog1.getImage());
                jsonObject.put("url", dataCatalog1.getUrl());
                jsonObject.put("time", relate.get(i).getTime());
                jsonObject.put("space", relate.get(i).getSpace());
                jsonObject.put("topic", relate.get(i).getTopic());
                jsonObjects.add(jsonObject);
            }
        }
        Map<String, Object> result = new HashMap<>();
        result.put("detail", dataCatalog);
        result.put("relate", jsonObjects);
        return result;
    }

    class TopicComparator implements Comparator<DataNetRelationship> {
        @Override
        public int compare(DataNetRelationship p1, DataNetRelationship p2) {
            // 按照年龄升序排列
            return Double.compare(Double.parseDouble(p2.getTopic()), Double.parseDouble(p1.getTopic()));
        }
    }

    /**
     * 根据来源进行数据统计
     */
    @Override
    public List<DataCatalogStatistics> statistics() {
        List<DataCatalogStatistics> result = dataCatalogMapper.statistics();
        return result;
    }

    @Override
    public List<Map<String, Integer>> monthStatistics() {
        return dataCatalogMapper.monthStatistics();
    }

    @Override
    public List<Map<String, Integer>> subjectStatistics() {
        return dataCatalogMapper.subjectStatistics();
    }

    /**
     * 查询【数据目录】列表
     *
     * @param dataCatalog 【数据目录】
     * @return 【数据目录】
     */
    @Override
    public List<DataCatalog> selectDataCatalogList(DataCatalog dataCatalog) {
        return dataCatalogMapper.selectDataCatalogList(dataCatalog);
    }

    /**
     * 新增【数据目录】
     *
     * @param dataCatalog 【数据目录】
     * @return 结果
     */
    @Override
    public int insertDataCatalog(DataCatalog dataCatalog) {
        dataCatalog.setCreateTime(DateUtils.getNowDate());
        return dataCatalogMapper.insertDataCatalog(dataCatalog);
    }

    /**
     * 修改【数据目录】
     *
     * @param dataCatalog 【数据目录】
     * @return 结果
     */
    @Override
    public int updateDataCatalog(DataCatalog dataCatalog) {
        dataCatalog.setUpdateTime(DateUtils.getNowDate());
        return dataCatalogMapper.updateDataCatalog(dataCatalog);
    }

    /**
     * 批量删除【数据目录】
     *
     * @param ids 需要删除的【数据目录】主键
     * @return 结果
     */
    @Override
    public int deleteDataCatalogByIds(Long[] ids) {
        return dataCatalogMapper.deleteDataCatalogByIds(ids);
    }

    /**
     * 删除【数据目录】信息
     *
     * @param id 【数据目录】主键
     * @return 结果
     */
    @Override
    public int deleteDataCatalogById(Long id) {
        return dataCatalogMapper.deleteDataCatalogById(id);
    }

    @Override
    public void addTestData() {
        int numRecords = 1000;
        String[] str = new String[]{
                "NASA EOSDIS",
                "USGS EarthExplorer",
                "ESA Earth Online",
                "NOAA NCEI",
                "GBIF",
                "WorldClim",
                "MODIS Land Rapid Response System",
                "OpenStreetMap",
                "Copernicus Open Access Hub",
                "Earthdata Search",
                "Geoscience Australia",
                "CIESIN - Center for International Earth Science Information Network",
                "Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center",
                "South African Environmental Observation Network (SAEON)",
                "Brazil Data Cube",
                "中国地球科学数据共享网",
                "中国国家卫星气象中心",
                "中国科学院地理科学与资源研究所",
                "中国环境监测总站",
                "中国地震局"};
        for (int i = 1; i < numRecords; i++) {
            DataCatalog dataCatalog = new DataCatalog();
            dataCatalog.setId(i);
            Random random = new Random();
            dataCatalog.setOrigin(str[random.nextInt(20)]);
            dataCatalogMapper.updateDataCatalog(dataCatalog);
        }

    }
}
