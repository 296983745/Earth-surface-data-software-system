import xml.etree.ElementTree as ET
import pymysql
import os

# 连接到数据库
db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="earthdata")
cursor = db.cursor()

folder_path = 'D:\\01重要文件\earthdataTest'
xml_files = [f for f in os.listdir(folder_path) if f.endswith('.dif10')]
# xml_files.sort()  # 按照文件名的字母顺序对文件列表进行排序
for xml_file in xml_files:
    xml_path = os.path.join(folder_path, xml_file)
    print(xml_file)
    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 命名空间映射
    namespace = {'dif': 'http://gcmd.gsfc.nasa.gov/Aboutus/xml/dif/'}

    # 获取所有的Science_Keywords元素
    science_keywords_elements = root.findall('dif:Science_Keywords', namespace)

    entry_title_element = root.find('dif:Entry_Title', namespace)

    Southernmost_Latitude_element = ""
    Northernmost_Latitude_element = ""
    Westernmost_Longitude_element = ""
    Easternmost_Longitude_element = ""
    Spatial_Coverage = root.find("dif:Spatial_Coverage", namespace)
    if Spatial_Coverage is not None:
        Geometry = Spatial_Coverage.find("dif:Geometry", namespace)
        if Geometry is not None:
            Bounding_Rectangle = Geometry.find("dif:Bounding_Rectangle", namespace)
            if Bounding_Rectangle is not None:
                Southernmost_Latitude = Bounding_Rectangle.find("dif:Southernmost_Latitude", namespace)
                if Southernmost_Latitude is not None:
                    Southernmost_Latitude_element = Southernmost_Latitude.text

                Northernmost_Latitude = Bounding_Rectangle.find("dif:Northernmost_Latitude", namespace)
                if Northernmost_Latitude is not None:
                    Northernmost_Latitude_element = Northernmost_Latitude.text

                Westernmost_Longitude = Bounding_Rectangle.find("dif:Westernmost_Longitude", namespace)
                if Westernmost_Longitude is not None:
                    Westernmost_Longitude_element = Westernmost_Longitude.text

                Easternmost_Longitude = Bounding_Rectangle.find("dif:Easternmost_Longitude", namespace)
                if Easternmost_Longitude is not None:
                    Easternmost_Longitude_element = Easternmost_Longitude.text

            else:
                Point = Geometry.find("dif:Point", namespace)
                if Point is not None:
                    Easternmost_Longitude_element = Point.find("dif:Point_Longitude", namespace).text
                    Westernmost_Longitude_element = Easternmost_Longitude_element
                    Northernmost_Latitude_element = Point.find("dif:Point_Latitude", namespace).text
                    Southernmost_Latitude_element = Northernmost_Latitude_element

    # print(Southernmost_Latitude_element)
    # print(Northernmost_Latitude_element)
    # print(Westernmost_Longitude_element)
    # print(Easternmost_Longitude_element)

    Temporal_Coverage = root.find("dif:Temporal_Coverage", namespace)
    if Temporal_Coverage is not None:
        Range_DateTime = Temporal_Coverage.find("dif:Range_DateTime", namespace)
        if Range_DateTime is not None:
            Single_DateTime_element = Range_DateTime.find("dif:Single_DateTime", namespace)
            if Single_DateTime_element is None:
                Beginning_Date_Time = Range_DateTime.find("dif:Beginning_Date_Time", namespace).text
                Ending_Date_Time = Range_DateTime.find("dif:Ending_Date_Time", namespace)
                if Ending_Date_Time is None:
                    Ending_Date_Time = Beginning_Date_Time
                else:
                    Ending_Date_Time=Ending_Date_Time.text
            else:
                Beginning_Date_Time = Single_DateTime_element.text
                Ending_Date_Time = Single_DateTime_element.text

    # print(Beginning_Date_Time)
    # print(Ending_Date_Time)
    # 获取时间信息

    # Single_DateTime_element = root.find("dif:Single_DateTime", namespace).text
    # if Single_DateTime_element is None:
    #     Beginning_Date_Time = root.find("dif:Beginning_Date_Time", namespace).text
    #     Ending_Date_Time = root.find("dif:Ending_Date_Time", namespace).text
    # else:
    #     Beginning_Date_Time=Single_DateTime_element
    #     Ending_Date_Time=Single_DateTime_element

    # 获取Entry_Title的文本内容
    entry_title = entry_title_element.text

    # print(entry_title)
    # 用于存储关键字的集合
    category_set = set()
    topic_set = set()
    term_set = set()
    variable_level_1_set = set()

    # 遍历每个Science_Keywords元素
    for science_keywords_element in science_keywords_elements:
        # 获取子元素的文本内容
        category = science_keywords_element.find('dif:Category', namespace).text
        topic = science_keywords_element.find('dif:Topic', namespace).text
        term = science_keywords_element.find('dif:Term', namespace).text
        variable_level_1_element = science_keywords_element.find('dif:Variable_Level_1', namespace)
        if variable_level_1_element is not None:
            variable_level_1 = variable_level_1_element.text
        else:
            variable_level_1 = None

        # 将关键字添加到相应的集合中
        category_set.add(category)
        topic_set.add(topic)
        term_set.add(term)
        if variable_level_1 is not None:
            variable_level_1_set.add(variable_level_1)

    # 数据库连接与操作
    # 插入去重后的关键字
    insert_query = "INSERT INTO nasa1 (Entry_Title, Category, Topic, Term, Variable_Level_1, Southernmost_Latitude, Northernmost_Latitude, Westernmost_Longitude, Easternmost_Longitude, Beginning_Date_Time, Ending_Date_Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Category = VALUES(Category), Topic = VALUES(Topic), Term = VALUES(Term), Variable_Level_1 = VALUES(Variable_Level_1), Southernmost_Latitude = VALUES(Southernmost_Latitude), Northernmost_Latitude = VALUES(Northernmost_Latitude), Westernmost_Longitude = VALUES(Westernmost_Longitude), Easternmost_Longitude = VALUES(Easternmost_Longitude), Beginning_Date_Time = VALUES(Beginning_Date_Time), Ending_Date_Time = VALUES(Ending_Date_Time)"
    # insert_query = "INSERT INTO nasa1 (Entry_Title, Category, Topic, Term, Variable_Level_1) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Category = VALUES(Category), Topic = VALUES(Topic), Term = VALUES(Term), Variable_Level_1 = VALUES(Variable_Level_1)"

    # 检查数据长度并截断超过长度限制的字符串
    entry_title = entry_title[:255]  # Entry_Title 列长度限制为 255
    category_data = ', '.join(category_set)[:500]  # Category 列长度限制为 500
    topic_data = ', '.join(topic_set)[:500]  # Topic 列长度限制为 500
    term_data = ', '.join(term_set)[:500]  # Term 列长度限制为 500
    variable_level_1_data = ', '.join(variable_level_1_set)[:500]  # Variable_Level_1 列长度限制为 500

    data = (entry_title, category_data, topic_data, term_data, variable_level_1_data,
            Southernmost_Latitude_element, Northernmost_Latitude_element, Westernmost_Longitude_element,
            Easternmost_Longitude_element, Beginning_Date_Time, Ending_Date_Time)
    cursor.execute(insert_query, data)
    # 提交更改
    db.commit()

# 关闭数据库连接
db.close()
