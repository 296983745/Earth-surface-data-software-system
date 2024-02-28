# 空间关联度计算
import pandas as pd
import requests
# 根据地理位置获取经纬度，用他们之间的距离表示相似度，（有些空间关键词无法获取经纬度）
from geopy.distance import distance
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut

from content.content_yuyi.simi_hownet import get_mysql_list

# 地理位置标准化函数
from geopy.geocoders import ArcGIS


def translate_location(location):
    geolocator = ArcGIS(user_agent="my-app")

    # 定义需要转换的地理位置词汇
    # 获取地理位置的详细信息
    location_info = geolocator.geocode(location)
    try:
        location_info = geolocator.geocode(location)
        standard_location = location_info.address
    except (AttributeError, GeocoderTimedOut, GeocoderUnavailable):
        standard_location = location

    return standard_location


def get_address(address):  # 获取经纬度

    # 在百度地图开放平台申请的AK，需要替换成你自己的AK
    ak = '8AdMXpDmeA0EcuMX3dlQ3Qjk1e7i4cNw'

    # 构造请求URL
    url = f'http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak={ak}'

    # 发送HTTP请求，获取响应结果
    response = requests.get(url).json()
    # 解析响应结果，获取经纬度信息
    if 'result' in response:
        location = response['result']['location']
        longitude, latitude = location['lng'], location['lat']
        return [longitude, latitude]
    else:
        return 0
    # # 发送请求到高德地图Geocoding API
    # response = requests.get(
    #     f'https://restapi.amap.com/v3/geocode/geo?address={address}&key=6b8d8d51cd4c203867cc546cf9f4439b')
    #
    # # 获取响应中的经纬度坐标
    # result = response.json()
    # ak = "8AdMXpDmeA0EcuMX3dlQ3Qjk1e7i4cNw"  # 将your_access_key替换为自己的AK
    #
    # url = f"http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak={ak}"
    # response = requests.get(url)
    # result = response.json()
    # print(result)
    # if result['status'] == '0' and len(result['geocodes']) > 0:
    #     # 如果成功获取到经纬度，则返回经纬度
    #     location = result['geocodes'][0]['location']
    #     return tuple(map(float, location.split(',')))
    # else:
    #     # 如果地名不存在，则返回0
    #     return 0
    # 打印经纬度坐标
    # print('Latitude:', location[1])
    # print('Longitude:', location[0])
    # locations=[location[1],location[0]]
    # return locations


def get_simi(location1, location2):
    if location1 == 0 or location2 == 0:
        return 0
    # 计算两个位置之间的地理距离
    dist_km = distance((location1[1], location1[0]), (location2[1], location1[0])).km

    # 将距离归一化到0-1区间
    max_dist = 4000  # 假设最大距离为5000公里
    min_dist = 0  # 假设最小距离为0公里
    normalized_dist = (dist_km - min_dist) / (max_dist - min_dist)

    # 打印归一化后的距离
    return normalized_dist


if __name__ == '__main__':

    # s1=get_address('北京')
    # s2=get_address('广州')
    # print(s1)
    # simi=1-get_simi(s1,s2)
    # print(simi)
    # # 调用数据库
    x = get_mysql_list('earthdata', 'data_copy', 'SpacePlc')
    print(x)
    # 整理格式
    y = []
    for i in range(len(x)):
        stand_location = translate_location(x[i])
        # print(stand_location)
        tmp = get_address(stand_location)
        print(tmp)
        y.append(tmp)
    print(y)
    #先获取经纬度
    semtime=[]
    for i in range(len(x)):
        line = []
        for j in range(len(x)):
            simi = get_simi(y[i],y[j])
            line.append(simi)
        semtime.append(line)
    print(semtime)
    data_df = pd.DataFrame(semtime)
    # 将文件写入excel表格中
    writer = pd.ExcelWriter('SpaceSimi.xlsx')  # 关键2，创建excel表格
    data_df.to_excel(writer, 'page_1')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    writer.save()  # 关键4
