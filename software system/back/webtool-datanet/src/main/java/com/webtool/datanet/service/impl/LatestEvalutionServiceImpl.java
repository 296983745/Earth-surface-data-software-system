package com.webtool.datanet.service.impl;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.webtool.common.utils.DateUtils;
import com.webtool.datanet.domain.LatestEvalution;
import com.webtool.datanet.mapper.LatestEvalutionMapper;
import com.webtool.datanet.service.ILatestEvalutionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * 最新评价记录Service业务层处理
 *
 * @author webtool
 * @date 2023-06-29
 */
@Service
public class LatestEvalutionServiceImpl implements ILatestEvalutionService {
    @Autowired
    private LatestEvalutionMapper latestEvalutionMapper;

    /**
     * 查询最新评价记录
     *
     * @param id 最新评价记录主键
     * @return 最新评价记录
     */
    @Override
    public LatestEvalution selectLatestEvalutionById(Long id) {
        return latestEvalutionMapper.selectLatestEvalutionById(id);
    }

    /**
     * 查询最新评价记录列表
     *
     * @param latestEvalution 最新评价记录
     * @return 最新评价记录
     */
    @Override
    public List<LatestEvalution> selectLatestEvalutionList(LatestEvalution latestEvalution) {
        return latestEvalutionMapper.selectLatestEvalutionList(latestEvalution);
    }

    /**
     * 新增最新评价记录
     *
     * @param latestEvalution 最新评价记录
     * @return 结果
     */
    @Override
    public LatestEvalution insertLatestEvalution(LatestEvalution latestEvalution) {
        latestEvalution.setCreateTime(DateUtils.getNowDate());
        latestEvalution.setEvaluateTime(DateUtils.getNowDate());
        //  数据评价 逻辑！


        int[] findable = new int[4];
        int[] accessible = new int[4];
        int[] interoperable = new int[4];
        int[] reusable = new int[4];
        Random random = new Random();
        for (int i = 0; i < findable.length; i++) {
            findable[i] = random.nextInt(2); // 生成0或1的随机数
            accessible[i] = random.nextInt(2); // 生成0或1的随机数
            interoperable[i] = random.nextInt(2); // 生成0或1的随机数
            reusable[i] = random.nextInt(2); // 生成0或1的随机数
        }
        Map<String, Object> result = new HashMap<>(4);
        result.put("findable", findable);
        result.put("accessible", accessible);
        result.put("interoperable", interoperable);
        result.put("reusable", reusable);
        ObjectMapper objectMapper = new ObjectMapper();
        String resultStr = "";
        int count1 = 0;
        try {
            resultStr = objectMapper.writeValueAsString(result);

            for (int i = 0; i < resultStr.length(); i++) {
                char c = resultStr.charAt(i);
                if (c == '1') {
                    count1++;
                }

            }

        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        latestEvalution.setScore(count1 + "/16");
        latestEvalution.setResult(resultStr);
        latestEvalutionMapper.insertLatestEvalution(latestEvalution);
        return latestEvalution;
    }

    /**
     * 修改最新评价记录
     *
     * @param latestEvalution 最新评价记录
     * @return 结果
     */
    @Override
    public int updateLatestEvalution(LatestEvalution latestEvalution) {
        latestEvalution.setUpdateTime(DateUtils.getNowDate());
        return latestEvalutionMapper.updateLatestEvalution(latestEvalution);
    }

    /**
     * 批量删除最新评价记录
     *
     * @param ids 需要删除的最新评价记录主键
     * @return 结果
     */
    @Override
    public int deleteLatestEvalutionByIds(Long[] ids) {
        return latestEvalutionMapper.deleteLatestEvalutionByIds(ids);
    }

    /**
     * 删除最新评价记录信息
     *
     * @param id 最新评价记录主键
     * @return 结果
     */
    @Override
    public int deleteLatestEvalutionById(Long id) {
        return latestEvalutionMapper.deleteLatestEvalutionById(id);
    }
}
