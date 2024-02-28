package com.webtool.datanet.service;


import com.webtool.datanet.domain.DataNetNode;

import java.util.List;
import java.util.Map;

/**
 * @Author liujiandong
 * @Date 2023/5/12&15:45
 * @Description
 */
public interface DataNetService {
    /**
     * 数据关联网络获取
     * @param keyWord
     * @param limit
     * @return
     */
    Map<String,Object> getAll(String keyWord,Integer limit);

    /**
     * 名称获取
     * @param name
     * @return
     */

    List<DataNetNode> getByName(String name);


}
