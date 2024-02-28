import request from '@/utils/request'

// 查询部门列表
export function listDataEntity(query) {
  return request({
    url: '/data/entity/list',
    method: 'get',
    params: query
  })
}

// 查询部门列表（排除节点）
export function listDataEntityExcludeChild(entityId) {
  return request({
    url: '/data/entity/list/exclude/' + entityId,
    method: 'get'
  })
}

// 查询部门详细
export function getDataEntity(entityId) {
  return request({
    url: '/data/entity' + entityId,
    method: 'get'
  })
}

// 新增部门
export function addDataEntity(data) {
  return request({
    url: '/data/entity',
    method: 'post',
    data: data
  })
}

// 修改部门
export function updateDataEntity(data) {
  return request({
    url: '/data/entity',
    method: 'put',
    data: data
  })
}

// 删除部门
export function delDataEntity(entityId) {
  return request({
    url: '/data/entity/' + entityId,
    method: 'delete'
  })
}

// 查询部门下拉树结构
export function dataEntityTreeSelect() {
    return request({
      url: '/data/entity/tree',
      method: 'get'
    })
  }