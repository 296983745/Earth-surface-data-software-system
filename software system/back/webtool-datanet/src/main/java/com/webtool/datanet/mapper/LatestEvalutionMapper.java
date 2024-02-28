package com.webtool.datanet.mapper;

import com.webtool.datanet.domain.LatestEvalution;

import java.util.List;

/**
 * 最新评价记录Mapper接口
 * 
 * @author webtool
 * @date 2023-06-29
 */
public interface LatestEvalutionMapper
{
    /**
     * 查询最新评价记录
     * 
     * @param id 最新评价记录主键
     * @return 最新评价记录
     */
    public LatestEvalution selectLatestEvalutionById(Long id);

    /**
     * 查询最新评价记录列表
     * 
     * @param latestEvalution 最新评价记录
     * @return 最新评价记录集合
     */
    public List<LatestEvalution> selectLatestEvalutionList(LatestEvalution latestEvalution);

    /**
     * 新增最新评价记录
     * 
     * @param latestEvalution 最新评价记录
     * @return 结果
     */
    public int insertLatestEvalution(LatestEvalution latestEvalution);

    /**
     * 修改最新评价记录
     * 
     * @param latestEvalution 最新评价记录
     * @return 结果
     */
    public int updateLatestEvalution(LatestEvalution latestEvalution);

    /**
     * 删除最新评价记录
     * 
     * @param id 最新评价记录主键
     * @return 结果
     */
    public int deleteLatestEvalutionById(Long id);

    /**
     * 批量删除最新评价记录
     * 
     * @param ids 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteLatestEvalutionByIds(Long[] ids);
}
