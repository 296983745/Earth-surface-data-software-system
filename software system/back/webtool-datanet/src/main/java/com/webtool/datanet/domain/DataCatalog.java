package com.webtool.datanet.domain;

import com.webtool.common.annotation.Excel;
import com.webtool.common.core.domain.BaseEntity;
import lombok.Data;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

/**
 * 【数据目录】对象 data_catalog
 *
 * @author webtool
 * @date 2023-05-31
 */
@Data
public class DataCatalog extends BaseEntity {
    private static final long serialVersionUID = 1L;

    /**
     * 主键
     */
    private Integer id;

    /**
     * 数据目录名称
     */
    @Excel(name = "数据目录名称")
    private String name;

    /**
     * 摘要
     */
    @Excel(name = "摘要")
    private String abstractText;

    /**
     * 主题
     */
    @Excel(name = "主题")
    private String subject;

    /**
     * 关键字
     */
    @Excel(name = "关键字")
    private String mainWord;

    /**
     * 来源
     */
    @Excel(name = "来源")
    private String origin;

    /**
     * 坐标
     */
    @Excel(name = "坐标")
    private String coordinate;

    private String dateTime;

    private String url;

    private String image;
    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setAbstractText(String abstractText) {
        this.abstractText = abstractText;
    }

    public String getAbstractText() {
        return abstractText;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getSubject() {
        return subject;
    }

    public void setMainWord(String mainWord) {
        this.mainWord = mainWord;
    }

    public String getMainWord() {
        return mainWord;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }

    public String getOrigin() {
        return origin;
    }

    public void setCoordinate(String coordinate) {
        this.coordinate = coordinate;
    }

    public String getCoordinate() {
        return coordinate;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE)
                .append("id", getId())
                .append("name", getName())
                .append("abstractText", getAbstractText())
                .append("subject", getSubject())
                .append("mainWord", getMainWord())
                .append("origin", getOrigin())
                .append("coordinate", getCoordinate())
                .append("url", getUrl())
                .append("createBy", getCreateBy())
                .append("createTime", getCreateTime())
                .append("updateBy", getUpdateBy())
                .append("updateTime", getUpdateTime())
                .toString();
    }
}
