import request from '@/utils/request'


// 查询当前账户的评价记录
export function getLatestEvaluation(query) {
    return request({
      url: '/latestEvaluation/list',
      method: 'get',
      params: query
    })
}
  

// 新增记录
export function addEvaluation(data) {
    return request({
      url: '/latestEvaluation/add',
      method: 'post',
      data: data
    })
  }
  