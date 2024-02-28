package com.webtool.quartz.task;

import com.webtool.common.core.redis.RedisCache;
import com.webtool.datanet.service.DataNetService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.webtool.common.utils.StringUtils;

import java.util.Map;

/**
 * 定时任务调度测试
 *
 * @author webtool
 */
@Component("ryTask")
public class RyTask {
    @Autowired
    private DataNetService dataNetService;
    @Autowired
    private RedisCache redisCache;

    public void ryMultipleParams(String s, Boolean b, Long l, Double d, Integer i) {
        System.out.println(StringUtils.format("执行多参方法： 字符串类型{}，布尔类型{}，长整型{}，浮点型{}，整形{}", s, b, l, d, i));
    }

    public void ryParams(String params) {
        System.out.println("执行有参方法：" + params);
    }

    public  void ryNoParams() {
        System.out.println("执行无参方法");
        Map<String, Object> all = dataNetService.getAll("", 1000);
        redisCache.setCacheObject("dataNet-task", all);
    }
}
