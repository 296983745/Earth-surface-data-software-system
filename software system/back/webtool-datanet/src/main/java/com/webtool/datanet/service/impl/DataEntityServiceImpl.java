package com.webtool.datanet.service.impl;

import com.webtool.common.annotation.DataScope;
import com.webtool.common.constant.UserConstants;
import com.webtool.common.core.domain.TreeSelect;
import com.webtool.common.utils.StringUtils;
import com.webtool.common.utils.spring.SpringUtils;
import com.webtool.datanet.domain.DataEntity;
import com.webtool.datanet.domain.DataEntityTreeSelect;
import com.webtool.datanet.mapper.DataEntityMapper;
import com.webtool.datanet.service.IDataEntityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 部门管理 服务实现
 * 
 * @author webtool
 */
@Service
public class DataEntityServiceImpl implements IDataEntityService
{
    @Autowired
    private DataEntityMapper dataEntityMapper;


    /**
     * 查询部门管理数据
     * 
     * @param dataEntity 部门信息
     * @return 部门信息集合
     */
    @Override
    @DataScope(deptAlias = "d")
    public List<DataEntity> selectDataEntityList(DataEntity dataEntity)
    {
        return dataEntityMapper.selectDataEntityList(dataEntity);
    }

    /**
     * 查询结构信息
     * 
     * @param dataEntity 信息
     * @return 树信息集合
     */
    @Override
    public List<DataEntityTreeSelect> selectDataEntityTreeList(DataEntity dataEntity)
    {
        List<DataEntity> dataList = SpringUtils.getAopProxy(this).selectDataEntityList(dataEntity);
        return buildDeptTreeSelect(dataList);
    }

    /**
     * 构建前端所需要树结构
     * 
     * @param dataEntities 部门列表
     * @return 树结构列表
     */
    @Override
    public List<DataEntity> buildDataEntityTree(List<DataEntity> dataEntities)
    {
        List<DataEntity> returnList = new ArrayList<DataEntity>();
        List<Long> tempList = dataEntities.stream().map(DataEntity::getEntityId).collect(Collectors.toList());
        for (DataEntity dataEntity : dataEntities)
        {
            // 如果是顶级节点, 遍历该父节点的所有子节点
            if (!tempList.contains(dataEntity.getParentId()))
            {
                recursionFn(dataEntities, dataEntity);
                returnList.add(dataEntity);
            }
        }
        if (returnList.isEmpty())
        {
            returnList = dataEntities;
        }
        return returnList;
    }

    /**
     * 构建前端所需要下拉树结构
     *
     * @param DataEntities 部门列表
     * @return 下拉树结构列表
     */
    @Override
    public List<DataEntityTreeSelect> buildDeptTreeSelect(List<DataEntity> DataEntities)
    {
        List<DataEntity> dataEntityTree = buildDataEntityTree(DataEntities);
        return dataEntityTree.stream().map(DataEntityTreeSelect::new).collect(Collectors.toList());
    }


    /**
     * 根据ID查询信息
     * 
     * @param dataEntityId ID
     * @return 信息
     */
    @Override
    public DataEntity selectDataEntityById(Long dataEntityId)
    {
        return dataEntityMapper.selectDataEntityById(dataEntityId);
    }

    /**
     * 是否存在子节点
     * 
     * @param deptId 部门ID
     * @return 结果
     */
    @Override
    public boolean hasChildByEntityId(Long deptId)
    {
        int result = dataEntityMapper.hasChildByEntityId(deptId);
        return result > 0;
    }


    /**
     * 校验部门名称是否唯一
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    @Override
    public boolean checkDataEntityNameUnique(DataEntity dataEntity)
    {
        Long entityId = StringUtils.isNull(dataEntity.getEntityId()) ? -1L : dataEntity.getEntityId();
        DataEntity info = dataEntityMapper.checkDataEntityNameUnique(dataEntity.getName(), dataEntity.getParentId());
        if (StringUtils.isNotNull(info) && info.getEntityId().longValue() != entityId.longValue())
        {
            return UserConstants.NOT_UNIQUE;
        }
        return UserConstants.UNIQUE;
    }


    /**
     * 新增保存部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    @Override
    public int insertDataEntity(DataEntity dataEntity)
    {
        DataEntity info = dataEntityMapper.selectDataEntityById(dataEntity.getParentId());
        dataEntity.setAncestors(info.getAncestors() + "," + dataEntity.getParentId());
        return dataEntityMapper.insertDataEntity(dataEntity);
    }

    /**
     * 修改保存部门信息
     * 
     * @param dataEntity 部门信息
     * @return 结果
     */
    @Override
    public int updateDataEntity(DataEntity dataEntity)
    {
        DataEntity newParentDataEntity = dataEntityMapper.selectDataEntityById(dataEntity.getParentId());
        DataEntity oldDataEntity = dataEntityMapper.selectDataEntityById(dataEntity.getEntityId());
        if (StringUtils.isNotNull(newParentDataEntity) && StringUtils.isNotNull(oldDataEntity))
        {
            String newAncestors = newParentDataEntity.getAncestors() + "," + newParentDataEntity.getEntityId();
            String oldAncestors = oldDataEntity.getAncestors();
            dataEntity.setAncestors(newAncestors);
            updateDataEntityChildren(dataEntity.getEntityId(), newAncestors, oldAncestors);
        }
        int result = dataEntityMapper.updateDataEntity(dataEntity);
        return result;
    }


    /**
     * 修改子元素关系
     * 
     * @param entityId 被修改的部门ID
     * @param newAncestors 新的父ID集合
     * @param oldAncestors 旧的父ID集合
     */
    public void updateDataEntityChildren(Long entityId, String newAncestors, String oldAncestors)
    {
        List<DataEntity> children = dataEntityMapper.selectChildrenDataEntityById(entityId);
        for (DataEntity child : children)
        {
            child.setAncestors(child.getAncestors().replaceFirst(oldAncestors, newAncestors));
        }
        if (children.size() > 0)
        {
            dataEntityMapper.updateDataEntityChildren(children);
        }
    }

    /**
     * 删除部门管理信息
     * 
     * @param entityId 部门ID
     * @return 结果
     */
    @Override
    public int deleteById(Long entityId)
    {
        return dataEntityMapper.deleteById(entityId);
    }

    /**
     * 递归列表
     */
    private void recursionFn(List<DataEntity> list, DataEntity t)
    {
        // 得到子节点列表
        List<DataEntity> childList = getChildList(list, t);
        t.setChildren(childList);
        for (DataEntity tChild : childList)
        {
            if (hasChild(list, tChild))
            {
                recursionFn(list, tChild);
            }
        }
    }

    /**
     * 得到子节点列表
     */
    private List<DataEntity> getChildList(List<DataEntity> list, DataEntity t)
    {
        List<DataEntity> tlist = new ArrayList<DataEntity>();
        Iterator<DataEntity> it = list.iterator();
        while (it.hasNext())
        {
            DataEntity n = (DataEntity) it.next();
            if (StringUtils.isNotNull(n.getParentId()) && n.getParentId().longValue() == t.getEntityId().longValue())
            {
                tlist.add(n);
            }
        }
        return tlist;
    }

    /**
     * 判断是否有子节点
     */
    private boolean hasChild(List<DataEntity> list, DataEntity t)
    {
        return getChildList(list, t).size() > 0;
    }
}
