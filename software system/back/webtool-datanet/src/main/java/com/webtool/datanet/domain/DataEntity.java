package com.webtool.datanet.domain;

import com.webtool.common.core.domain.BaseEntity;
import com.webtool.common.core.domain.entity.SysDept;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.Data;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Administrator
 */
public class DataEntity extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** ID */
    private Long entityId;

    /** 父ID */
    private Long parentId;

    /** 祖级列表 */
    private String ancestors;

    /** 部门名称 */
    private String name;

    /** 显示顺序 */
    private Integer orderNum;

    /** 部门状态:0正常,1停用 */
    private String dataOrigin;

    /** 删除标志（0代表存在 2代表删除） */
    private String delFlag;

    /** 父部门名称 */
    private String parentName;

    /** 子部门 */
    private List<DataEntity> children = new ArrayList<DataEntity>();

    public Long getEntityId()
    {
        return entityId;
    }

    public void setEntityId(Long entityId)
    {
        this.entityId = entityId;
    }

    public Long getParentId()
    {
        return parentId;
    }

    public void setParentId(Long parentId)
    {
        this.parentId = parentId;
    }

    public String getAncestors()
    {
        return ancestors;
    }

    public void setAncestors(String ancestors)
    {
        this.ancestors = ancestors;
    }

    @NotBlank(message = "本体名称不能为空")
    @Size(min = 0, max = 30, message = "本体名称长度不能超过30个字符")
    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    @NotNull(message = "显示顺序不能为空")
    public Integer getOrderNum()
    {
        return orderNum;
    }

    public void setOrderNum(Integer orderNum)
    {
        this.orderNum = orderNum;
    }


    public String getDataOrigin()
    {
        return dataOrigin;
    }

    public void setDataOrigin(String dataOrigin)
    {
        this.dataOrigin = dataOrigin;
    }

    public String getDelFlag()
    {
        return delFlag;
    }

    public void setDelFlag(String delFlag)
    {
        this.delFlag = delFlag;
    }

    public String getParentName()
    {
        return parentName;
    }

    public void setParentName(String parentName)
    {
        this.parentName = parentName;
    }

    public List<DataEntity> getChildren()
    {
        return children;
    }

    public void setChildren(List<DataEntity> children)
    {
        this.children = children;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE)
                .append("entityId", getEntityId())
                .append("parentId", getParentId())
                .append("ancestors", getAncestors())
                .append("name", getName())
                .append("orderNum", getOrderNum())
                .append("dataOrigin", getDataOrigin())
                .append("delFlag", getDelFlag())
                .append("createBy", getCreateBy())
                .append("createTime", getCreateTime())
                .append("updateBy", getUpdateBy())
                .append("updateTime", getUpdateTime())
                .toString();
    }
}
