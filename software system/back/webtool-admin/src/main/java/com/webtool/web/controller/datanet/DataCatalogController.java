package com.webtool.web.controller.datanet;

import java.util.List;
import javax.servlet.http.HttpServletResponse;

import com.webtool.datanet.domain.DataCatalog;
import com.webtool.datanet.service.IDataCatalogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.webtool.common.annotation.Log;
import com.webtool.common.core.controller.BaseController;
import com.webtool.common.core.domain.AjaxResult;
import com.webtool.common.enums.BusinessType;
import com.webtool.common.utils.poi.ExcelUtil;
import com.webtool.common.core.page.TableDataInfo;

/**
 * 【数据目录】Controller
 *
 * @author webtool
 * @date 2023-05-31
 */
@RestController
@RequestMapping("/dataNet/catalog")
public class DataCatalogController extends BaseController {
    @Autowired
    private IDataCatalogService dataCatalogService;

    /**
     * 查询【数据目录】列表
     */
    @Log(title = "获取数据目录列表", businessType = BusinessType.EXPORT)
    @GetMapping("/list")
    public TableDataInfo list(DataCatalog dataCatalog) {
        startPage();
        List<DataCatalog> list = dataCatalogService.selectDataCatalogList(dataCatalog);
        return getDataTable(list);
    }

    @Log(title = "获取数据目录列表", businessType = BusinessType.EXPORT)
    @GetMapping("/listAll")
    public List<DataCatalog> listAll(DataCatalog dataCatalog) {
        List<DataCatalog> list = dataCatalogService.selectDataCatalogList(dataCatalog);
        return list;
    }

    /**
     * 【数据目录】统计分析-根据来源进行数据统计
     */
    @GetMapping(value = "/statistics")
    @Log(title = "【数据目录】统计分析-根据来源进行数据统计", businessType = BusinessType.SELECT)
    public AjaxResult statistics() {
        return success(dataCatalogService.statistics());
    }

    /**
     * 【数据目录】统计分析-根据最近一年的数据新增和更新进行数据统计
     */
    @GetMapping(value = "/monthStatistics")
    @Log(title = "【数据目录】统计分析-根据最近一年的数据新增和更新进行数据统计", businessType = BusinessType.SELECT)
    public AjaxResult monthStatistics() {
        return success(dataCatalogService.monthStatistics());
    }

    /**
     * 【数据目录】统计分析-根据学科进行数据统计
     */
    @GetMapping(value = "/subjectStatistics")
    @Log(title = "【数据目录】统计分析-根据学科进行数据统计", businessType = BusinessType.SELECT)
    public AjaxResult subjectStatistics() {
        return success(dataCatalogService.subjectStatistics());
    }


    /**
     * 导出【数据目录】列表
     */
    @Log(title = "【数据目录】", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, DataCatalog dataCatalog) {
        List<DataCatalog> list = dataCatalogService.selectDataCatalogList(dataCatalog);
        ExcelUtil<DataCatalog> util = new ExcelUtil<DataCatalog>(DataCatalog.class);
        util.exportExcel(response, list, "【数据目录】数据");
    }

    /**
     * 获取【数据目录】详细信息
     */
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id) {
        return success(dataCatalogService.selectDataCatalogById(id));
    }

    /**
     * 获取【数据目录】详细信息
     */
    @GetMapping(value = "/selectDataCatalogByName")
    public AjaxResult getInfoByName(@RequestParam(name = "name") String name) {
        return success(dataCatalogService.selectDataCatalogByName(name));
    }

    /**
     * 新增【数据目录】
     */
    @Log(title = "【数据目录】", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody DataCatalog dataCatalog) {
        return toAjax(dataCatalogService.insertDataCatalog(dataCatalog));
    }

    /**
     * 修改【数据目录】
     */
    @Log(title = "【数据目录】", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody DataCatalog dataCatalog) {
        return toAjax(dataCatalogService.updateDataCatalog(dataCatalog));
    }

    /**
     * 删除【数据目录】
     */
    @Log(title = "【数据目录】", businessType = BusinessType.DELETE)
    @DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids) {
        return toAjax(dataCatalogService.deleteDataCatalogByIds(ids));
    }

    @Log(title = "【数据目录】", businessType = BusinessType.INSERT)
    @PostMapping("/addAll")
    public void addTestData() {
        dataCatalogService.addTestData();
    }

}
