package com.webtool.web.controller.datanet;

import java.util.List;
import javax.servlet.http.HttpServletResponse;

import com.webtool.common.utils.SecurityUtils;
import com.webtool.common.utils.poi.ExcelUtil;
import com.webtool.datanet.domain.LatestEvalution;
import com.webtool.datanet.service.ILatestEvalutionService;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.webtool.common.annotation.Log;
import com.webtool.common.core.controller.BaseController;
import com.webtool.common.core.domain.AjaxResult;
import com.webtool.common.enums.BusinessType;
import com.webtool.common.core.page.TableDataInfo;

/**
 * 最新评价记录Controller
 *
 * @author webtool
 * @date 2023-06-29
 */
@RestController
@RequestMapping("/latestEvaluation/")
public class LatestEvaluationController extends BaseController {
    @Autowired
    private ILatestEvalutionService latestEvaluationService;

    /**
     * 查询最新评价记录列表
     */
    @GetMapping("/list")
    @Log(title = "【最新评价记录获取】", businessType = BusinessType.OTHER)
    public TableDataInfo list(LatestEvalution latestEvalution) {
        startPage();
        latestEvalution.setUserId(SecurityUtils.getUserId());
        List<LatestEvalution> list = latestEvaluationService.selectLatestEvalutionList(latestEvalution);
        return getDataTable(list);
    }

    /**
     * 导出最新评价记录列表
     */
    @PreAuthorize("@ss.hasPermi('latestEvalution:evalution:export')")
    @Log(title = "最新评价记录", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, LatestEvalution latestEvalution) {
        List<LatestEvalution> list = latestEvaluationService.selectLatestEvalutionList(latestEvalution);
        ExcelUtil<LatestEvalution> util = new ExcelUtil<LatestEvalution>(LatestEvalution.class);
        util.exportExcel(response, list, "最新评价记录数据");
    }

    /**
     * 获取最新评价记录详细信息
     */
    @PreAuthorize("@ss.hasPermi('latestEvalution:evalution:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id) {
        return success(latestEvaluationService.selectLatestEvalutionById(id));
    }

    /**
     * 新增最新评价记录模块，
     */
    @Log(title = "最新评价记录", businessType = BusinessType.INSERT)
    @PostMapping("/add")
    public AjaxResult add(@RequestBody LatestEvalution latestEvalution) {
        latestEvalution.setUserId(SecurityUtils.getUserId());
        return success(latestEvaluationService.insertLatestEvalution(latestEvalution));
    }

    /**
     * 修改最新评价记录
     */
    @PreAuthorize("@ss.hasPermi('latestEvalution:evalution:edit')")
    @Log(title = "最新评价记录", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody LatestEvalution latestEvalution) {
        return toAjax(latestEvaluationService.updateLatestEvalution(latestEvalution));
    }

    /**
     * 删除最新评价记录
     */
    @PreAuthorize("@ss.hasPermi('latestEvalution:evalution:remove')")
    @Log(title = "最新评价记录", businessType = BusinessType.DELETE)
    @DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids) {
        return toAjax(latestEvaluationService.deleteLatestEvalutionByIds(ids));
    }
}
