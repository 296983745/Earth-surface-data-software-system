package com.webtool.web.controller.datanet;

import com.webtool.common.annotation.Log;
import com.webtool.common.core.domain.AjaxResult;
import com.webtool.common.core.redis.RedisCache;
import com.webtool.common.enums.BusinessType;
import com.webtool.common.utils.StringUtils;
import com.webtool.datanet.service.DataNetService;
import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.security.PermitAll;
import java.util.Map;

import static com.webtool.common.core.domain.AjaxResult.error;
import static com.webtool.common.core.domain.AjaxResult.success;

/**
 * @Author liujiandong
 * @Date 2023/5/12&15:04
 * @Description
 */
@RestController
@Api("数据关联网络管理")
@RequestMapping("/dataNet")
public class DataNetController {
    @Autowired
    private DataNetService dataNetService;
    @Autowired
    private RedisCache redisCache;

    @GetMapping(value = "/getAll")
    @Log(title = "【数据关联网络获取】", businessType = BusinessType.OTHER)
    public AjaxResult getAll(
            @RequestParam(name = "keyWord", required = false) String keyWord,
            @RequestParam(name = "limit", defaultValue = "1000") Integer limit
    ) {
        AjaxResult result = new AjaxResult();
        Map<String, Object> all = redisCache.getCacheObject("dataNet");
        try {
            if (all == null || StringUtils.isNotBlank(keyWord) || limit != 1000) {
                all = dataNetService.getAll(keyWord,limit);
                redisCache.setCacheObject("dataNet", all);
            }
            result = success(all);
        } catch (Exception e) {
            result = error(e.getMessage());
        }
        return result;
    }

}
