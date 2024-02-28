package com.webtool.datanet.domain;

import java.io.Serializable;
import java.util.List;
import java.util.stream.Collectors;
import com.fasterxml.jackson.annotation.JsonInclude;

/**
 * Treeselect树结构实体类
 * 
 * @author webtool
 */
public class DataEntityTreeSelect implements Serializable
{
    private static final long serialVersionUID = 1L;

    /** 节点ID */
    private Long id;

    /** 节点名称 */
    private String label;

    /** 子节点 */
    @JsonInclude(JsonInclude.Include.NON_EMPTY)
    private List<DataEntityTreeSelect> children;

    public DataEntityTreeSelect()
    {

    }

    public DataEntityTreeSelect(DataEntity dataEntity)
    {
        this.id = dataEntity.getEntityId();
        this.label = dataEntity.getName();
        this.children = dataEntity.getChildren().stream().map(DataEntityTreeSelect::new).collect(Collectors.toList());
    }


    public Long getId()
    {
        return id;
    }

    public void setId(Long id)
    {
        this.id = id;
    }

    public String getLabel()
    {
        return label;
    }

    public void setLabel(String label)
    {
        this.label = label;
    }

    public List<DataEntityTreeSelect> getChildren()
    {
        return children;
    }

    public void setChildren(List<DataEntityTreeSelect> children)
    {
        this.children = children;
    }
}
