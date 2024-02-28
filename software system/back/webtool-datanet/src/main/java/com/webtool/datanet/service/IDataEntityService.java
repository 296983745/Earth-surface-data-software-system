package com.webtool.datanet.service;

import com.webtool.common.core.domain.TreeSelect;
import com.webtool.datanet.domain.DataEntity;
import com.webtool.datanet.domain.DataEntityTreeSelect;

import java.util.List;

/**
 * 实体管理 服务层
 * 
 * @author webtool
 */
public interface IDataEntityService
{
    /**
     * 查询实体管理数据
     * 
     * @param dataEntity 部门信息
     * @return 信息集合
     */
    public List<DataEntity> selectDataEntityList(DataEntity dataEntity);

    /**
     * 查询部门树结构信息
     * 
     * @param dataEntity 部门信息
     * @return 部门树信息集合
     */
    public List<DataEntityTreeSelect> selectDataEntityTreeList(DataEntity dataEntity);

    /**
     * 构建前端所需要树结构
     * 
     * @param dataEntities 部门列表
     * @return 树结构列表
     */
    public List<DataEntity> buildDataEntityTree(List<DataEntity> dataEntities);

    /**
     * 构建前端所需要下拉树结构
     *
     * @param dataEntities 部门列表
     * @return 下拉树结构列表
     */
    public List<DataEntityTreeSelect> buildDeptTreeSelect(List<DataEntity> dataEntities);


    /**
     * 根据ID查询信息
     * 
     * @param deptId ID
     * @return 信息
     */
    public DataEntity selectDataEntityById(Long deptId);


    /**
     * 是否存在部门子节点
     * 
     * @param entityId 部门ID
     * @return 结果
     */
    public boolean hasChildByEntityId(Long entityId);


    /**
     * 校验名称是否唯一
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    public boolean checkDataEntityNameUnique(DataEntity dataEntity);

    /**
     * 新增保存部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    public int insertDataEntity(DataEntity dataEntity);

    /**
     * 修改保存部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    public int updateDataEntity(DataEntity dataEntity);

    /**
     * 删除部门管理信息
     * 
     * @param entityId ID
     * @return 结果
     */
    public int deleteById(Long entityId);
}
