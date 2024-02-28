package com.webtool.datanet.domain;

import java.util.Date;
import com.fasterxml.jackson.annotation.JsonFormat;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.webtool.common.annotation.Excel;
import com.webtool.common.core.domain.BaseEntity;

/**
 * 最新评价记录对象 latest_evalution
 * 
 * @author webtool
 * @date 2023-06-29
 */
public class LatestEvalution extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 主键 */
    private Long id;

    /** 用户id */
    @Excel(name = "用户id")
    private Long userId;

    /** 评价时间 */
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Excel(name = "评价时间", width = 30, dateFormat = "yyyy-MM-dd HH:mm:ss")
    private Date evaluateTime;

    /** 数据url */
    @Excel(name = "数据url")
    private String url;

    /** 评价指标 */
    @Excel(name = "评价指标")
    private String indicators;

    /** 评价结果 */
    @Excel(name = "评价结果")
    private String result;

    /** 得分 */
    @Excel(name = "得分")
    private String score;

    public void setId(Long id) 
    {
        this.id = id;
    }

    public Long getId() 
    {
        return id;
    }
    public void setUserId(Long userId) 
    {
        this.userId = userId;
    }

    public Long getUserId() 
    {
        return userId;
    }
    public void setEvaluateTime(Date evaluateTime) 
    {
        this.evaluateTime = evaluateTime;
    }

    public Date getEvaluateTime() 
    {
        return evaluateTime;
    }
    public void setUrl(String url) 
    {
        this.url = url;
    }

    public String getUrl() 
    {
        return url;
    }
    public void setIndicators(String Indicators) 
    {
        this.indicators = Indicators;
    }

    public String getIndicators() 
    {
        return indicators;
    }
    public void setResult(String result) 
    {
        this.result = result;
    }

    public String getResult() 
    {
        return result;
    }
    public void setScore(String score) 
    {
        this.score = score;
    }

    public String getScore() 
    {
        return score;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("id", getId())
            .append("userId", getUserId())
            .append("evaluateTime", getEvaluateTime())
            .append("url", getUrl())
            .append("Indicators", getIndicators())
            .append("result", getResult())
            .append("score", getScore())
            .append("createBy", getCreateBy())
            .append("createTime", getCreateTime())
            .append("updateBy", getUpdateBy())
            .append("updateTime", getUpdateTime())
            .toString();
    }
}
