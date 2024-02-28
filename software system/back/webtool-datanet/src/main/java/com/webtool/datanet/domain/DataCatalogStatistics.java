package com.webtool.datanet.domain;

import com.webtool.common.annotation.Excel;
import com.webtool.common.core.domain.BaseEntity;
import lombok.Data;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

/**
 * 【数据目录】对象 data_catalog 统计
 *
 * @author webtool
 * @date 2023-05-31
 */
@Data
public class DataCatalogStatistics  {

    private String origin;

    private Integer count;

}
