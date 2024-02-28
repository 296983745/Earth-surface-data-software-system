package com.webtool.web.controller.datanet;

import com.webtool.common.annotation.Log;
import com.webtool.common.constant.UserConstants;
import com.webtool.common.core.controller.BaseController;
import com.webtool.common.core.domain.AjaxResult;
import com.webtool.common.core.domain.entity.SysDept;
import com.webtool.common.enums.BusinessType;
import com.webtool.common.utils.StringUtils;
import com.webtool.datanet.domain.DataEntity;
import com.webtool.datanet.service.IDataEntityService;
import org.apache.commons.lang3.ArrayUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 数据本体信息
 * 
 * @author webtool
 */
@RestController
@RequestMapping("/data/entity")
public class DataEntityController extends BaseController
{
    @Autowired
    private IDataEntityService dataEntityService;

    /**
     * 获取数据本体列表
     */
    @GetMapping("/list")
    public AjaxResult list(DataEntity dataEntity)
    {
        List<DataEntity> dataList = dataEntityService.selectDataEntityList(dataEntity);
        return success(dataList);
    }

    /**
     * 查询列表（排除节点）
     */
    @GetMapping("/list/exclude/{entityId}")
    public AjaxResult excludeChild(@PathVariable(value = "entityId", required = false) Long entityId)
    {
        List<DataEntity> depts = dataEntityService.selectDataEntityList(new DataEntity());
        depts.removeIf(d -> d.getEntityId().intValue() == entityId || ArrayUtils.contains(StringUtils.split(d.getAncestors(), ","), entityId + ""));
        return success(depts);
    }

    /**
     * 根据编号获取详细信息
     */
    public AjaxResult getInfo(@PathVariable Long entityId)
    {
        return success(dataEntityService.selectDataEntityById(entityId));
    }

    /**
     * 新增
     */
    @Log(title = "管理", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@Validated @RequestBody DataEntity dataEntity)
    {
        if (!dataEntityService.checkDataEntityNameUnique(dataEntity))
        {
            return error("新增本体'" + dataEntity.getName() + "'失败，本体名称已存在");
        }
        dataEntity.setCreateBy(getUsername());
        return toAjax(dataEntityService.insertDataEntity(dataEntity));
    }

    /**
     * 修改部门
     */
    @PreAuthorize("@ss.hasPermi('system:dept:edit')")
    @Log(title = "部门管理", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@Validated @RequestBody DataEntity dataEntity)
    {
        Long entityId = dataEntity.getEntityId();
        if (!dataEntityService.checkDataEntityNameUnique(dataEntity))
        {
            return error("修改本体'" + dataEntity.getName() + "'失败，本体名称已存在");
        }
        else if (dataEntity.getParentId().equals(entityId))
        {
            return error("修改本体'" + dataEntity.getName() + "'失败，上级不能是自己");
        }
        dataEntity.setUpdateBy(getUsername());
        return toAjax(dataEntityService.updateDataEntity(dataEntity));
    }

    /**
     * 删除
     */
    @Log(title = "管理", businessType = BusinessType.DELETE)
    @DeleteMapping("/{entityId}")
    public AjaxResult remove(@PathVariable Long entityId)
    {
        if (dataEntityService.hasChildByEntityId(entityId))
        {
            return warn("存在下级,不允许删除");
        }

        return toAjax(dataEntityService.deleteById(entityId));
    }
    /**
     * 获取树列表
     */
    @GetMapping("/tree")
    public AjaxResult deptTree(DataEntity dataEntity)
    {
        return success(dataEntityService.selectDataEntityTreeList(dataEntity));
    }
}
