package com.webtool.datanet.service;

import java.util.List;
import java.util.Map;

import com.webtool.datanet.domain.DataCatalog;
import com.webtool.datanet.domain.DataCatalogStatistics;

/**
 * 【数据目录】Service接口
 *
 * @author webtool
 * @date 2023-05-31
 */
public interface IDataCatalogService {
    /**
     * 查询【数据目录】
     *
     * @param id 【数据目录】主键
     * @return 【数据目录】
     */
    public DataCatalog selectDataCatalogById(Long id);

    Map selectDataCatalogByName(String name);

    /**
     * 根据来源进行数据统计
     *
     * @return
     */
    List<DataCatalogStatistics> statistics();

    /**
     * 统计分析-根据最近一年的数据新增和更新进行数据统计
     *
     * @return
     */
    List<Map<String, Integer>> monthStatistics();

    /**
     * 【数据目录】统计分析-根据学科进行数据统计
     *
     * @return
     */
    List<Map<String, Integer>> subjectStatistics();


    /**
     * 查询【数据目录】列表
     *
     * @param dataCatalog 【数据目录】
     * @return 【数据目录】集合
     */
    public List<DataCatalog> selectDataCatalogList(DataCatalog dataCatalog);

    /**
     * 新增【数据目录】
     *
     * @param dataCatalog 【数据目录】
     * @return 结果
     */
    public int insertDataCatalog(DataCatalog dataCatalog);

    /**
     * 修改【数据目录】
     *
     * @param dataCatalog 【数据目录】
     * @return 结果
     */
    public int updateDataCatalog(DataCatalog dataCatalog);

    /**
     * 批量删除【数据目录】
     *
     * @param ids 需要删除的【数据目录】主键集合
     * @return 结果
     */
    public int deleteDataCatalogByIds(Long[] ids);

    /**
     * 删除【数据目录】信息
     *
     * @param id 【数据目录】主键
     * @return 结果
     */
    public int deleteDataCatalogById(Long id);

    void addTestData();


}
