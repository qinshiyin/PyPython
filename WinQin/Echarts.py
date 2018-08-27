#!/usr/bin/env python


import pyecharts as pca


style = pca.Style(
    title_top='#fff',
    title_pos='center',
    width=1200,
    height=600,
    background_color='#404a59'
)
'''
data_gz = [
    ['广州', '上海'],
    ['广州', '北京'],
    ['广州', '南京'],
    ['广州', '重庆'],
    ['广州', '兰州'],
    ['广州', '杭州']
]
'''
data_gz = [
    ['广州', '上海'],
    ['广州', '杭州'],
    ['广州', '南京'],
    ['广州', '西安'],
    ['广州', '北京'],
    ['广州', '长沙'],
    ['广州', '重庆'],
    ['广州', '成都'],
    ['广州', '南昌'],
    ['广州', '贵阳'],
    ['广州', '昆明'],
    ['广州', '哈尔滨'],
    ['广州', '武汉'],
    ['广州', '兰州'],
    ['广州', '拉萨'],
    ['广州', '乌鲁木齐'],
    ['广州', '呼和浩特'],
    ['广州', '台北'],
    ['广州', '天津'],
    ['广州', '福州'],
    ['广州', '郑州'],
    ['广州', '太原'],
    ['广州', '长春'],
    ['广州', '济南'],
    ['广州', '银川'],
    ['广州', '南宁'],
    ['广州', '海口'],
    ['广州', '合肥'],
    ['广州', '石家庄'],
    ['广州', '沈阳']
]

geo = pca.Geo('GeoLines示例', **style.init_style)


geo_lines = pca.GeoLines('GeoLines示例', **style.init_style)
geo_lines.add('从广州出发', data_gz, is_legend_show=False)
geo_lines.render(r'd:\render.html')

from pyecharts import Geo
import pyecharts as pca
style = pca.Style(
    title_top='#fff',
    title_pos='center',
    width=1200,
    height=600,
    background_color='#404a59'
)
data = [('广州', 45), ('漳州', 35), ('A市', 43)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
attr, value = geo.cast(data)
geo.add_coordinate('A市', 119.3, 26.08) # 添加 pyecharts 未提供的城市地理坐标
geo.add(
    "全国主要城市空气质量",
    attr,
    value,
    type="effectScatter",
    is_random=True,
    is_visualmap=True,
    is_piecewise=True,
    visual_text_color="#fff",
    pieces=[
        {"min": 0, "max": 13, "label": "0 < x < 13"},
        {"min": 14, "max": 16, "label": "14 < x < 16"},
    ],
    effect_scale=5,
)
geo.render(r'd:\render.html')

