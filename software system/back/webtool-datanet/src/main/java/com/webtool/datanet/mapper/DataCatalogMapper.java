package com.webtool.datanet.mapper;

import java.util.List;
import java.util.Map;

import com.webtool.datanet.domain.DataCatalog;
import com.webtool.datanet.domain.DataCatalogStatistics;
import org.apache.ibatis.annotations.MapKey;

/**
 * 【数据目录】Mapper接口
 *
 * @author webtool
 * @date 2023-05-31
 */
public interface DataCatalogMapper {
    /**
     * 查询【数据目录】
     *
     * @param id 【数据目录】主键
     * @return 【数据目录】
     */
    public DataCatalog selectDataCatalogById(Long id);

    /**
     * 通过名称查询【数据目录】
     * @param name
     * @return
     */
    public List<DataCatalog> selectDataCatalogByName(String name);

    /**
     * 根据来源进行数据统计
     * @return
     */

    List<DataCatalogStatistics> statistics();


    List<Map<String,Integer>>monthStatistics();

    List<Map<String,Integer>>subjectStatistics();

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
     * 删除【数据目录】
     *
     * @param id 【数据目录】主键
     * @return 结果
     */
    public int deleteDataCatalogById(Long id);

    /**
     * 批量删除【数据目录】
     *
     * @param ids 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteDataCatalogByIds(Long[] ids);



    List<Map> getTestData();

    List<Map> getedges();
}
