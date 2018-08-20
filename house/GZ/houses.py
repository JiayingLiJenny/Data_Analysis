# -*- coding:utf-8 -*-
from lxml import etree
import requests
import time
# import pandas as pd

def get_info(header, start_url, n):
    for i in range(1, n):
        url = start_url + str(i)
        html = requests.get(url, headers=header)
        time.sleep(1)
        selector = etree.HTML(html.text)
        houses = selector.xpath('//*[@id="cycleListings"]/ul/li')
        info_list = []
        for house in houses:
            title = house.xpath('div[1]/p[1]/a/text()')[0]
            room = house.xpath('div[1]/p[2]/span[2]/text()')[0]
            area = house.xpath('div[1]/p[2]/span[4]/text()')[0].strip('平米')
            decoration = house.xpath('div[1]/p[2]/span[6]/text()')[0].strip('装修')
            # 精，普通，豪华，毛坯
            layer = house.xpath('div[1]/p[2]/span[8]/text()')[0].strip('\r\n\t')
            orientation = house.xpath('div[1]/p[2]/span[10]/text()')[0]
            # 东，南，西，北，东北，东南，西北，西南
            location = house.xpath('div[1]/p[3]/span[2]/a[1]/text()')[0]
            #location_02 = house.xpath('div[1]/p[3]/span[2]/a[2]/text()')[0]
            unit_price = house.xpath('div[2]/p/text()')[0].strip('元/平米')
            price = house.xpath('div[2]/span[1]/text()')[0]+'0000'
            print('正在抓取：', title)
            info = {'名称': title, '户型': room, '建筑面积(平方米)': area, '装修情况': decoration, '楼层': layer, '朝向': orientation, '位置': location, '每平米售价（元）': unit_price, '总价（元）': price}
            info_list.append(info)

    return info_list




header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.23 Mobile Safari/537.36'
}
start_url = 'https://guangzhou.qfang.com/sale/f'
n = 84 # 页数
try:
    info_list = get_info(header, start_url, n)
    #df = pd.DataFrame(info_list)
except Exception as e:
    print('Exception: ',e)            