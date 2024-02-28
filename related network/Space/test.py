#测试两个地理位置得到管理度（坐标表示）

"""
测试两个地理位置得到管理度（坐标表示）



"""

from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import affinity

from content.content_yuyi.simi_hownet import get_mysql_list


# 计算两个地理区域的相似度
def simicoordinate(coords1, coords2):
    # 将坐标点转换为 shapely.geometry.Polygon 对象
    poly1 = Polygon(coords1)
    poly2 = Polygon(coords2)
    relation = None
    # 判断两个地理区域之间的四交模型拓扑关系

    if poly1==poly2 or poly1.equals(poly2):
        similarity = 1.0
        relation = "equals"
    elif poly1.contains(poly2):
        # 计算被包含者占包含者的比例
        ratio = poly2.area / poly1.area
        similarity = ratio*0.4+0.333
        relation = "contains"# 1包含2 0.5 最多加0.167 包含要边界不相接
    elif poly2.contains(poly1):
        # 交换两个地理区域的顺序，保证第一个地理区域是包含者
        poly1, poly2 = poly2, poly1
        # 计算被包含者占包含者的比例
        ratio = poly2.area / poly1.area
        similarity = ratio*0.5+0.333
        relation = "containsed" #被包含
    elif poly1.intersects(poly2):
        # 计算两个地理区域的重叠面积和总面积
        intersection = poly1.intersection(poly2)
        union = unary_union([poly1, poly2])
        # 计算重叠面积占总面积的比例
        overlap_ratio = intersection.area / union.area
        similarity = overlap_ratio*0.667+0.333  #重叠基础相似度是0.5，根据重叠程度加，最多加0.167
        relation = "overlap"
    elif poly1.disjoint(poly2):
        # 计算两个地理区域的距离
        distance = poly1.distance(poly2)
        # 计算相似度，距离越远，相似度越低
        similarity = 1 / (1 + distance)*0.333 #相离 最多0.333
        relation = "disjoint"

    return similarity , relation

# henan=[(31.23,112.42),(35.05,112.42),(35.05,116.12),(31.23,116.12)]
# # henan2=[(31.23,112.42),(35.05,112.42),(35.05,116.12),(31.23,116.12)]
# quanguo=[(39.4420784301, 115.41682667), (41.0589642496, 115.41682667), (41.0589642496, 117.50825136), (39.4420784301, 117.50825136)]
# # quanguo2=[(18.1, 73.4), (53.34, 73.4), (53.34, 135.05), (18.1, 135.05)]
# spacerela = simicoordinate(henan, quanguo)
# print(spacerela)



