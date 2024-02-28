import request from '@/utils/request'

// 查询关联网络



export function getDataCatalog(query) {
    return request({
      url: '/dataNet/catalog/list',
      method: 'get',
      params: query
    })
}



export function getDataCatalogAll(query) {
    return request({
      url: '/dataNet/catalog/listAll',
      method: 'get',
      params: query
    })
}
    

export function getDataCatalogStatistics() {
    return request({
      url: '/dataNet/catalog/statistics',
      method: 'get',
    })
}
  
export function getDataCatalogMonthStatistics() {
    return request({
      url: '/dataNet/catalog/monthStatistics',
      method: 'get',
    })
}
  
export function getDataCatalogSubjectStatistics() {
    return request({
      url: '/dataNet/catalog/subjectStatistics',
      method: 'get',
    })
}