import requests

def get_henan_polygon_coordinates(api_key):
    address = "河南省"
    url = f"http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak={api_key}"
    response = requests.get(url)
    data = response.json()

    # 提取边界坐标
    henan_boundary = data['result']['location']

    return henan_boundary

# 百度地图API密钥
api_key = "8AdMXpDmeA0EcuMX3dlQ3Qjk1e7i4cNw"

# 获取河南省边界坐标
henan_polygon_coordinates = get_henan_polygon_coordinates(api_key)

# 打印河南省边界坐标
print(henan_polygon_coordinates)
