package com.webtool.datanet.mapper;

import com.webtool.datanet.domain.DataEntity;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * 部门管理 数据层
 * 
 * @author webtool
 */
public interface DataEntityMapper
{
    /**
     * 查询部门管理数据
     * 
     * @param dataEntity 部门信息
     * @return 部门信息集合
     */
    public List<DataEntity> selectDataEntityList(DataEntity dataEntity);

    /**
     * 根据ID查询信息
     * 
     * @param dataEntityId ID
     * @return 信息
     */
    public DataEntity selectDataEntityById(Long dataEntityId);

    /**
     * 根据ID查询所有子部门
     * 
     * @param entityId 部门ID
     * @return 部门列表
     */
    public List<DataEntity> selectChildrenDataEntityById(Long entityId);


    /**
     * 是否存在子节点
     * 
     * @param entityId 部门ID
     * @return 结果
     */
    public int hasChildByEntityId(Long entityId);



    /**
     * 校验部门名称是否唯一
     * 
     * @param name 部门名称
     * @param parentId 父部门ID
     * @return 结果
     */
    public DataEntity checkDataEntityNameUnique(@Param("name") String name, @Param("parentId") Long parentId);

    /**
     * 新增部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    public int insertDataEntity(DataEntity dataEntity);

    /**
     * 修改部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    public int updateDataEntity(DataEntity dataEntity);

    /**
     * 修改子元素关系
     * 
     * @param dataEntities 子元素
     * @return 结果
     */
    public int updateDataEntityChildren(@Param("dataEntities") List<DataEntity> dataEntities);

    /**
     * 删除部门管理信息
     * 
     * @param entityId 部门ID
     * @return 结果
     */
    public int deleteById(Long entityId);
}
