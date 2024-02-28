import request from '@/utils/request'
import { parseStrEmpty } from "@/utils/webtool";

// 查询关联网络
export function getDataNet(query) {
    return request({
      url: '/dataNet/getAll',
      method: 'get',
      params: query
    })
}
  
export function getDataCatalogByName(query) {
    return request({
        url: '/dataNet/catalog/selectDataCatalogByName',
        method: 'get',
        params: query
    })
}