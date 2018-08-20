
## 数据爬取


```python
from lxml import etree
import requests
import time
import pandas as pd
```


```python
def get_info(header, start_url, n):
    info_list = []
    for i in range(1, n):
        url = start_url + str(i)
        html = requests.get(url, headers=header)
        time.sleep(1)
        selector = etree.HTML(html.text)
        houses = selector.xpath('//*[@id="cycleListings"]/ul/li')        
        for house in houses:
            title = house.xpath('div[1]/p[1]/a/text()')[0]
            room = house.xpath('div[1]/p[2]/span[2]/text()')[0]
            area = house.xpath('div[1]/p[2]/span[4]/text()')[0].strip('平米')
            decoration = house.xpath('div[1]/p[2]/span[6]/text()')[0].strip('装修')
            # 精，普通，豪华，毛坯
            layer = house.xpath('div[1]/p[2]/span[8]/text()')[0].strip('\r\n\t')
            # 低，中，高，别墅
            orientation = house.xpath('div[1]/p[2]/span[10]/text()')[0]
            # 东，南，西，北，东北，东南，西北，西南
            location = house.xpath('div[1]/p[3]/span[2]/a[1]/text()')[0]
            #location_02 = house.xpath('div[1]/p[3]/span[2]/a[2]/text()')[0]
            unit_price = house.xpath('div[2]/p/text()')[0].strip('元/平米')
            price = house.xpath('div[2]/span[1]/text()')[0]+'0000'
             # print('正在抓取：', title)
            info = {'名称': title, '户型': room, '建筑面积(平方米)': area, '装修情况': decoration, '楼层': layer, '朝向': orientation, '位置': location, '每平米售价（元）': unit_price, '总价（元）': price}
            info_list.append(info)
    return info_list
        
```


```python
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.23 Mobile Safari/537.36'
}
start_url = 'https://guangzhou.qfang.com/sale/f' # 广州
n = 84 # 页数
try:
    info_list = get_info(header, start_url, n)
    df = pd.DataFrame(info_list)
except Exception as e:
    print('Exception: ',e)
```


```python
print('当前在售房屋数：{}'.format(len(df)))
df.head(10)
```

    当前在售房屋数：2488





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
    </tr>
    <tr>
      <th>5</th>
      <td>天河</td>
      <td>碧海湾 珠江新城 大3房 方正实用 望江景小蛮腰</td>
      <td>178</td>
      <td>13000000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>低层/28层</td>
      <td>73034</td>
      <td>精</td>
    </tr>
    <tr>
      <th>6</th>
      <td>番禺</td>
      <td>锦绣半岛 全新装修 一线江景 南北通透  环境舒适</td>
      <td>139.54</td>
      <td>5600000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>高层/28层</td>
      <td>40132</td>
      <td>精</td>
    </tr>
    <tr>
      <th>7</th>
      <td>海珠</td>
      <td>南景园 中层电梯实用4房 东南靓向 采光通风好 看房方便</td>
      <td>116.77</td>
      <td>4800000</td>
      <td>4室2厅</td>
      <td>东南</td>
      <td>低层/12层</td>
      <td>41106</td>
      <td>普通</td>
    </tr>
    <tr>
      <th>8</th>
      <td>番禺</td>
      <td>洛湖居 地铁旁 精装修 南向两房 婚房之选 诚售 有匙看</td>
      <td>69.4</td>
      <td>2200000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>高层/6层</td>
      <td>31700</td>
      <td>精</td>
    </tr>
    <tr>
      <th>9</th>
      <td>番禺</td>
      <td>奥园养生广场 不一般价格优惠温馨公寓值得您拥有抢钱吧</td>
      <td>82</td>
      <td>1600000</td>
      <td>2室1厅</td>
      <td>东北</td>
      <td>中层/29层</td>
      <td>19512</td>
      <td>精</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 将爬取下来的数据放入houses.csv文件中
df.to_csv('houses.csv', encoding='utf-8')
```


```python
'''
也可以存储到数据库中：
from sqlalchemy import create_engine
yconnect = create_engine('nysql://root:root@localhost:3306/spider?charset=utf8')
保存到数据库中:
pd.io.sql.to_sql(df, 'house_price', yconnect, schema='spider', if_exists='append')
从数据库中取数:
df = pd.io.sql.read_sql(sql='select * from house_price', con=yconnect)
'''
```

## 数据加载


```python
import pandas as pd
import numpy as np
# 从csv中读取数据
data = pd.read_csv('houses.csv', encoding='utf-8', index_col=0) # index_col=0防止出现unnamed:0
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68.0</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115.0</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81.0</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60.0</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
    </tr>
  </tbody>
</table>
</div>



## 数据清洗

#### 清洗'楼层'数据


```python
layers = data['楼层'].str.split('/',expand=True)
layers.columns = ['楼层属性', '层数']
data = data.join(layers)
```


```python
data['层数'] = data['层数'].str.extract(r'(\d+)层', expand=True)
```


```python
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68.0</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
      <td>中层</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
      <td>低层</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115.0</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
      <td>中层</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81.0</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
      <td>中层</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60.0</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
      <td>低层</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#选择任意一行出现空值的数据
data[data['层数'].isnull().values]

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>番禺</td>
      <td>金业别墅花园金业西路 5房别墅  格局方正 少有放盘</td>
      <td>230.00</td>
      <td>8800000</td>
      <td>5室2厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>38261</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>385</th>
      <td>番禺</td>
      <td>A区第6街 祈福新村A区别墅 全新装修送家私 欧洲现代风格</td>
      <td>192.00</td>
      <td>5500000</td>
      <td>4室2厅</td>
      <td>北</td>
      <td>共1层</td>
      <td>28646</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>595</th>
      <td>番禺</td>
      <td>金业别墅花园倚翠路 小面积联排别墅，家电家私全送，过五，可入户，可按揭</td>
      <td>115.00</td>
      <td>4700000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>共1层</td>
      <td>40870</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>742</th>
      <td>番禺</td>
      <td>珠江花园 三层别墅  总价低  南向光线好 双阳台近江边</td>
      <td>180.00</td>
      <td>8000000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>44444</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>886</th>
      <td>番禺</td>
      <td>城市花园 精致2房 居家装修 业主工作调动换房急卖</td>
      <td>64.80</td>
      <td>2000000</td>
      <td>2室2厅</td>
      <td>南</td>
      <td>\t低层</td>
      <td>30864</td>
      <td>精</td>
      <td>\t低层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1067</th>
      <td>番禺</td>
      <td>丁香园 锦绣香江双拼别墅 大格局 成就人生</td>
      <td>163.00</td>
      <td>9500000</td>
      <td>5室2厅</td>
      <td>西南</td>
      <td>共1层</td>
      <td>58282</td>
      <td>普通</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>番禺</td>
      <td>城市花园 少有一楼单位</td>
      <td>64.80</td>
      <td>2230000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>\t低层</td>
      <td>34414</td>
      <td>精</td>
      <td>\t低层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1626</th>
      <td>番禺</td>
      <td>珠江花园 别墅  一线望江 南北通透 给您家的感觉！</td>
      <td>298.00</td>
      <td>20000000</td>
      <td>9室2厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>67114</td>
      <td>普通</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1648</th>
      <td>黄埔</td>
      <td>金碧领秀国际 4房3厅 168平 精装装修 南北</td>
      <td>168.00</td>
      <td>7000000</td>
      <td>5室3厅</td>
      <td>南北</td>
      <td>共3层</td>
      <td>41667</td>
      <td>精</td>
      <td>共3层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1658</th>
      <td>番禺</td>
      <td>汇景花园西北区 汇景花园别墅 6室2厅1厨3卫</td>
      <td>411.17</td>
      <td>6380000</td>
      <td>6室2厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>15517</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1666</th>
      <td>番禺</td>
      <td>金业别墅花园金业东路 正南向独栋别墅 采光十足 世外桃源 番中附小</td>
      <td>270.00</td>
      <td>8600000</td>
      <td>5室3厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>31852</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1785</th>
      <td>番禺</td>
      <td>金业别墅花园倚翠路 带花园 采光十足</td>
      <td>252.00</td>
      <td>9800000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>38889</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1800</th>
      <td>番禺</td>
      <td>金业别墅花园金业东路 业主急除名卖独栋别墅  采光十足 带200方花园</td>
      <td>333.60</td>
      <td>16800000</td>
      <td>6室3厅</td>
      <td>北</td>
      <td>共1层</td>
      <td>50360</td>
      <td>精</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2097</th>
      <td>番禺</td>
      <td>珠江花园 双拼别墅 精美装修 南北对流 清雅安静</td>
      <td>135.00</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>南北</td>
      <td>共1层</td>
      <td>55556</td>
      <td>豪华</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2208</th>
      <td>番禺</td>
      <td>雅居乐花园 清华坊 四大名园 官邸四合院住宅 极少出售</td>
      <td>600.00</td>
      <td>36000000</td>
      <td>7室3厅</td>
      <td>南</td>
      <td>共1层</td>
      <td>60000</td>
      <td>豪华</td>
      <td>共1层</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2469</th>
      <td>黄埔</td>
      <td>金碧领秀国际 4房3厅 167平 普通装修 南</td>
      <td>167.00</td>
      <td>7000000</td>
      <td>4室3厅</td>
      <td>南</td>
      <td>共3层</td>
      <td>41916</td>
      <td>普通</td>
      <td>共3层</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 处理不规则数据
def process_layers(layer):
    if '低' in layer:
        layer = '低'
    elif '中' in layer:
        layer = '中'
    elif '高' in layer:
        layer = '高'
    else:
        layer = '别墅'
    return layer 

data['楼层属性'] = data['楼层属性'].map(process_layers)
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68.00</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
      <td>中</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.70</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
      <td>低</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115.00</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
      <td>中</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81.00</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
      <td>中</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60.00</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
      <td>低</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>天河</td>
      <td>碧海湾 珠江新城 大3房 方正实用 望江景小蛮腰</td>
      <td>178.00</td>
      <td>13000000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>低层/28层</td>
      <td>73034</td>
      <td>精</td>
      <td>低</td>
      <td>28</td>
    </tr>
    <tr>
      <th>6</th>
      <td>番禺</td>
      <td>锦绣半岛 全新装修 一线江景 南北通透  环境舒适</td>
      <td>139.54</td>
      <td>5600000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>高层/28层</td>
      <td>40132</td>
      <td>精</td>
      <td>高</td>
      <td>28</td>
    </tr>
    <tr>
      <th>7</th>
      <td>海珠</td>
      <td>南景园 中层电梯实用4房 东南靓向 采光通风好 看房方便</td>
      <td>116.77</td>
      <td>4800000</td>
      <td>4室2厅</td>
      <td>东南</td>
      <td>低层/12层</td>
      <td>41106</td>
      <td>普通</td>
      <td>低</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>番禺</td>
      <td>洛湖居 地铁旁 精装修 南向两房 婚房之选 诚售 有匙看</td>
      <td>69.40</td>
      <td>2200000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>高层/6层</td>
      <td>31700</td>
      <td>精</td>
      <td>高</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>番禺</td>
      <td>奥园养生广场 不一般价格优惠温馨公寓值得您拥有抢钱吧</td>
      <td>82.00</td>
      <td>1600000</td>
      <td>2室1厅</td>
      <td>东北</td>
      <td>中层/29层</td>
      <td>19512</td>
      <td>精</td>
      <td>中</td>
      <td>29</td>
    </tr>
    <tr>
      <th>10</th>
      <td>黄埔</td>
      <td>怡园小区  四房 户型实用简洁、方便看房</td>
      <td>130.00</td>
      <td>5200000</td>
      <td>4室2厅</td>
      <td>北</td>
      <td>低层/8层</td>
      <td>40000</td>
      <td>精</td>
      <td>低</td>
      <td>8</td>
    </tr>
    <tr>
      <th>11</th>
      <td>天河</td>
      <td>盈彩美居 新推出高性价比3房 格局方正 业主置换 诚心出售</td>
      <td>92.50</td>
      <td>3800000</td>
      <td>3室2厅</td>
      <td>西</td>
      <td>高层/11层</td>
      <td>41081</td>
      <td>精</td>
      <td>高</td>
      <td>11</td>
    </tr>
    <tr>
      <th>12</th>
      <td>黄埔</td>
      <td>金碧世纪花园 一期南北通透大两房 目前出租 可看房</td>
      <td>69.00</td>
      <td>2700000</td>
      <td>2室2厅</td>
      <td>南</td>
      <td>高层/17层</td>
      <td>39130</td>
      <td>普通</td>
      <td>高</td>
      <td>17</td>
    </tr>
    <tr>
      <th>13</th>
      <td>番禺</td>
      <td>君华御府 新小区 复试大4房 中间位置  南向电梯高层视野好</td>
      <td>76.00</td>
      <td>3500000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>高层/33层</td>
      <td>46053</td>
      <td>毛坯</td>
      <td>高</td>
      <td>33</td>
    </tr>
    <tr>
      <th>14</th>
      <td>番禺</td>
      <td>东雅园 电梯快捷   交通方便</td>
      <td>102.00</td>
      <td>3000000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>中层/12层</td>
      <td>29412</td>
      <td>精</td>
      <td>中</td>
      <td>12</td>
    </tr>
    <tr>
      <th>15</th>
      <td>番禺</td>
      <td>广州雅居乐北苑 滟澜街精装三房</td>
      <td>102.00</td>
      <td>4600000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/26层</td>
      <td>45098</td>
      <td>精</td>
      <td>中</td>
      <td>26</td>
    </tr>
    <tr>
      <th>16</th>
      <td>番禺</td>
      <td>海怡花园 东南 三房两厅 清雅安静 三面环江 江边大道散步赞</td>
      <td>89.30</td>
      <td>3100000</td>
      <td>3室2厅</td>
      <td>东南</td>
      <td>低层/28层</td>
      <td>34714</td>
      <td>精</td>
      <td>低</td>
      <td>28</td>
    </tr>
    <tr>
      <th>17</th>
      <td>番禺</td>
      <td>雅居乐花园  十年小雅 精装三房 靠地铁</td>
      <td>90.10</td>
      <td>3600000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>低层/33层</td>
      <td>39956</td>
      <td>普通</td>
      <td>低</td>
      <td>33</td>
    </tr>
    <tr>
      <th>18</th>
      <td>天河</td>
      <td>盈彩美居 东南向三房 极少放盘 自住 保养好 地铁13号物业</td>
      <td>98.00</td>
      <td>4400000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>中层/11层</td>
      <td>44898</td>
      <td>普通</td>
      <td>中</td>
      <td>11</td>
    </tr>
    <tr>
      <th>19</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨两房  全新装修  南北对流  高层景观</td>
      <td>86.00</td>
      <td>2950000</td>
      <td>2室2厅</td>
      <td>南</td>
      <td>高层/25层</td>
      <td>34302</td>
      <td>精</td>
      <td>高</td>
      <td>25</td>
    </tr>
    <tr>
      <th>20</th>
      <td>番禺</td>
      <td>雅居乐花园 急售 业主自主保养好 过5年  税费低 看房提前</td>
      <td>158.20</td>
      <td>6000000</td>
      <td>4室2厅</td>
      <td>东</td>
      <td>低层/10层</td>
      <td>37927</td>
      <td>普通</td>
      <td>低</td>
      <td>10</td>
    </tr>
    <tr>
      <th>21</th>
      <td>天河</td>
      <td>五山花园一期 五山花园一套中等楼层的东南向的卖，下手要快</td>
      <td>84.00</td>
      <td>5400000</td>
      <td>2室2厅</td>
      <td>南</td>
      <td>高层/8层</td>
      <td>64286</td>
      <td>普通</td>
      <td>高</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>番禺</td>
      <td>锦绣半岛 一线江景  望江望花园  通风采光</td>
      <td>89.70</td>
      <td>3150000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/25层</td>
      <td>35117</td>
      <td>精</td>
      <td>中</td>
      <td>25</td>
    </tr>
    <tr>
      <th>23</th>
      <td>番禺</td>
      <td>丹桂园 近地铁 热卖中 大家族之选 独栋豪华别墅</td>
      <td>653.00</td>
      <td>12000000</td>
      <td>20室6厅</td>
      <td>西</td>
      <td>低层/3层</td>
      <td>18377</td>
      <td>精</td>
      <td>低</td>
      <td>3</td>
    </tr>
    <tr>
      <th>24</th>
      <td>天河</td>
      <td>中兴花园 精装修三房350万 东南向 安静 保养好 免装修</td>
      <td>90.00</td>
      <td>3400000</td>
      <td>3室1厅</td>
      <td>东</td>
      <td>低层/12层</td>
      <td>37778</td>
      <td>普通</td>
      <td>低</td>
      <td>12</td>
    </tr>
    <tr>
      <th>25</th>
      <td>番禺</td>
      <td>锦绣半岛 双证大三房 望花园安静舒适 带主套小阳台</td>
      <td>110.00</td>
      <td>3100000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>低层/19层</td>
      <td>28182</td>
      <td>精</td>
      <td>低</td>
      <td>19</td>
    </tr>
    <tr>
      <th>26</th>
      <td>番禺</td>
      <td>美心翠拥华庭  坐北朝南 3房2卫 近地铁站 业主急换房</td>
      <td>116.00</td>
      <td>2880000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>高层/6层</td>
      <td>24828</td>
      <td>精</td>
      <td>高</td>
      <td>6</td>
    </tr>
    <tr>
      <th>27</th>
      <td>番禺</td>
      <td>祈福新村E区 祈福新村E区 精装修 家私家电齐全</td>
      <td>91.00</td>
      <td>2350000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>中层/4层</td>
      <td>25824</td>
      <td>普通</td>
      <td>中</td>
      <td>4</td>
    </tr>
    <tr>
      <th>28</th>
      <td>番禺</td>
      <td>锦绣半岛 双证大三房 望花园安静舒适 带主套小阳台</td>
      <td>110.00</td>
      <td>3100000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>低层/19层</td>
      <td>28182</td>
      <td>精</td>
      <td>低</td>
      <td>19</td>
    </tr>
    <tr>
      <th>29</th>
      <td>海珠</td>
      <td>第三金碧花园  金碧花园三期 单价4万平方 南向望江 带装</td>
      <td>105.89</td>
      <td>4800000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>中层/32层</td>
      <td>45330</td>
      <td>普通</td>
      <td>中</td>
      <td>32</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2458</th>
      <td>番禺</td>
      <td>园丰小区 精装修温馨3房 安静不靠 大阳台</td>
      <td>106.00</td>
      <td>2180000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>高层/8层</td>
      <td>20566</td>
      <td>精</td>
      <td>高</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2459</th>
      <td>海珠</td>
      <td>天海庭 精装温馨大2房 采光通风好 厅出阳台 东南靓向</td>
      <td>86.00</td>
      <td>3800000</td>
      <td>2室2厅</td>
      <td>东南</td>
      <td>中层/12层</td>
      <td>44186</td>
      <td>精</td>
      <td>中</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2460</th>
      <td>天河</td>
      <td>富力新村 经典两室 业主自住 装修保养好 采光充足</td>
      <td>58.80</td>
      <td>1650000</td>
      <td>2室1厅</td>
      <td>东</td>
      <td>高层/9层</td>
      <td>28061</td>
      <td>精</td>
      <td>高</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2461</th>
      <td>番禺</td>
      <td>越秀可逸江畔 3房2厅136平南428万就读番中附小学校</td>
      <td>136.00</td>
      <td>4800000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>高层/13层</td>
      <td>35294</td>
      <td>毛坯</td>
      <td>高</td>
      <td>13</td>
    </tr>
    <tr>
      <th>2462</th>
      <td>番禺</td>
      <td>鸿禧华庭  精装三房   地铁物业    满5年税费低</td>
      <td>113.84</td>
      <td>4000000</td>
      <td>3室2厅</td>
      <td>南北</td>
      <td>低层/17层</td>
      <td>35137</td>
      <td>精</td>
      <td>低</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2463</th>
      <td>黄埔</td>
      <td>新世纪花园 2+1框架中层南向两房 省级怡园学·位 交通便利</td>
      <td>79.00</td>
      <td>2050000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>中层/9层</td>
      <td>25949</td>
      <td>普通</td>
      <td>中</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2464</th>
      <td>番禺</td>
      <td>奥园城市广场  精致装修 1室1厅1厨1卫</td>
      <td>40.00</td>
      <td>1600000</td>
      <td>1室1厅</td>
      <td>北</td>
      <td>高层/21层</td>
      <td>40000</td>
      <td>精</td>
      <td>高</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2465</th>
      <td>黄埔</td>
      <td>万科黄埔仓 精装单间 配套齐全 交通方便 业主好说话 看房方便</td>
      <td>21.00</td>
      <td>700000</td>
      <td>1室0厅</td>
      <td>北</td>
      <td>低层/22层</td>
      <td>33333</td>
      <td>精</td>
      <td>低</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2466</th>
      <td>白云</td>
      <td>金碧新城花园 五期小两房 户型方正 业主保养的非常好</td>
      <td>64.00</td>
      <td>2380000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>中层/27层</td>
      <td>37188</td>
      <td>普通</td>
      <td>中</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2467</th>
      <td>番禺</td>
      <td>奥园养生广场 精装大单间南向采光好商用自住都可以</td>
      <td>37.00</td>
      <td>600000</td>
      <td>1室1厅</td>
      <td>南</td>
      <td>中层/29层</td>
      <td>16216</td>
      <td>精</td>
      <td>中</td>
      <td>29</td>
    </tr>
    <tr>
      <th>2468</th>
      <td>天河</td>
      <td>棠雅苑 冬暖夏凉 阳光明媚  方正户型 阳台望花园</td>
      <td>47.00</td>
      <td>2400000</td>
      <td>2室1厅</td>
      <td>南北</td>
      <td>中层/9层</td>
      <td>51064</td>
      <td>普通</td>
      <td>中</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2469</th>
      <td>黄埔</td>
      <td>金碧领秀国际 4房3厅 167平 普通装修 南</td>
      <td>167.00</td>
      <td>7000000</td>
      <td>4室3厅</td>
      <td>南</td>
      <td>共3层</td>
      <td>41916</td>
      <td>普通</td>
      <td>别墅</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2470</th>
      <td>番禺</td>
      <td>德安新村 地铁物业，交通方便，生活配置完善</td>
      <td>117.00</td>
      <td>2930000</td>
      <td>4室2厅</td>
      <td>南</td>
      <td>低层/6层</td>
      <td>25043</td>
      <td>普通</td>
      <td>低</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2471</th>
      <td>黄埔</td>
      <td>金碧领秀国际 1房1厅 34平 精装装修 北</td>
      <td>34.00</td>
      <td>1700000</td>
      <td>1室1厅</td>
      <td>北</td>
      <td>低层/33层</td>
      <td>50000</td>
      <td>精</td>
      <td>低</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2472</th>
      <td>番禺</td>
      <td>万科欧泊 万博CBD板 精装大单间 交通便利  视野好</td>
      <td>45.11</td>
      <td>1050000</td>
      <td>1室0厅</td>
      <td>西</td>
      <td>高层/10层</td>
      <td>23276</td>
      <td>豪华</td>
      <td>高</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2473</th>
      <td>黄埔</td>
      <td>金碧领秀国际 南向2房  超好户型  采光好</td>
      <td>83.00</td>
      <td>3400000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>高层/33层</td>
      <td>40964</td>
      <td>普通</td>
      <td>高</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2474</th>
      <td>番禺</td>
      <td>禺丰园  实用二房 南北对流，光线好</td>
      <td>70.00</td>
      <td>1500000</td>
      <td>2室2厅</td>
      <td>南</td>
      <td>中层/9层</td>
      <td>21429</td>
      <td>精</td>
      <td>中</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2475</th>
      <td>天河</td>
      <td>华景里 48两房 精装装修复式楼 可个人交易 有意向可议</td>
      <td>48.25</td>
      <td>2700000</td>
      <td>2室1厅</td>
      <td>西</td>
      <td>高层/22层</td>
      <td>55959</td>
      <td>精</td>
      <td>高</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2476</th>
      <td>黄埔</td>
      <td>黄埔花园 精装2室 视野宽阔 空间超大</td>
      <td>80.00</td>
      <td>3300000</td>
      <td>2室2厅</td>
      <td>北</td>
      <td>中层/14层</td>
      <td>41250</td>
      <td>精</td>
      <td>中</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2477</th>
      <td>天河</td>
      <td>华景新城泽晖苑 西南向两房 厅出阳台望花园 业主诚心出售 价格可谈</td>
      <td>81.00</td>
      <td>4800000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>高层/9层</td>
      <td>59259</td>
      <td>普通</td>
      <td>高</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2478</th>
      <td>番禺</td>
      <td>雅居乐花园 过五年，税费低，保养好，业主好说话，看房提前约</td>
      <td>92.00</td>
      <td>3400000</td>
      <td>2室2厅</td>
      <td>东北</td>
      <td>低层/23层</td>
      <td>36957</td>
      <td>精</td>
      <td>低</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2479</th>
      <td>番禺</td>
      <td>雅居乐君域公馆 33平米全新精装修东向光线好</td>
      <td>33.00</td>
      <td>1100000</td>
      <td>1室0厅</td>
      <td>东</td>
      <td>低层/31层</td>
      <td>33333</td>
      <td>精</td>
      <td>低</td>
      <td>31</td>
    </tr>
    <tr>
      <th>2480</th>
      <td>白云</td>
      <td>富力阳光美居 黄石西路精致四房带车位急售</td>
      <td>118.00</td>
      <td>4500000</td>
      <td>4室1厅</td>
      <td>南</td>
      <td>高层/15层</td>
      <td>38136</td>
      <td>精</td>
      <td>高</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2481</th>
      <td>番禺</td>
      <td>招商城市主场 精装大单间，看上速联</td>
      <td>40.00</td>
      <td>1100000</td>
      <td>1室0厅</td>
      <td>东南</td>
      <td>中层/14层</td>
      <td>27500</td>
      <td>精</td>
      <td>中</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2482</th>
      <td>海珠</td>
      <td>晓燕湾 精装中层1房 采光通风好 格局方正 看房方便</td>
      <td>48.98</td>
      <td>1820000</td>
      <td>1室1厅</td>
      <td>南</td>
      <td>中层/9层</td>
      <td>37158</td>
      <td>豪华</td>
      <td>中</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2483</th>
      <td>黄埔</td>
      <td>金碧世纪花园  业主两年前装修 保养好现已搬出 看房有钥匙</td>
      <td>69.00</td>
      <td>2700000</td>
      <td>2室1厅</td>
      <td>东北</td>
      <td>中层/32层</td>
      <td>39130</td>
      <td>精</td>
      <td>中</td>
      <td>32</td>
    </tr>
    <tr>
      <th>2484</th>
      <td>天河</td>
      <td>誉峰 珠江新城业主需资金周转急售</td>
      <td>174.00</td>
      <td>16200000</td>
      <td>3室2厅</td>
      <td>南</td>
      <td>低层/41层</td>
      <td>93103</td>
      <td>普通</td>
      <td>低</td>
      <td>41</td>
    </tr>
    <tr>
      <th>2485</th>
      <td>海珠</td>
      <td>恒安雅苑 实用2房 厅出阳台 采光通风好 小区安静 看房方便</td>
      <td>61.10</td>
      <td>2200000</td>
      <td>2室2厅</td>
      <td>西南</td>
      <td>高层/6层</td>
      <td>36007</td>
      <td>普通</td>
      <td>高</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2486</th>
      <td>天河</td>
      <td>加拿大花园 大三房，周边配套齐全，环境好</td>
      <td>104.00</td>
      <td>4700000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/22层</td>
      <td>45192</td>
      <td>普通</td>
      <td>低</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2487</th>
      <td>番禺</td>
      <td>金口岸大厦 豪华四房</td>
      <td>139.00</td>
      <td>4000000</td>
      <td>3室2厅</td>
      <td>西</td>
      <td>中层/22层</td>
      <td>28777</td>
      <td>豪华</td>
      <td>中</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
<p>2488 rows × 11 columns</p>
</div>



#### 处理缺失值


```python
data['层数'] = data['层数'].astype(float)
layer_mean = np.floor(data['层数'].mean())
layer_mean
```




    18.0




```python
data = data.fillna(layer_mean)
data['层数'].isnull().sum()
```




    0



#### 清洗'户型'数据


```python
data[['室', '厅']] = data['户型'].str.extract(r'(\d+)室(\d+)厅', expand=True) # 正则匹配抽取

'''
expand : bool, default True
         If True, return DataFrame.
         If False, return Series/Index/DataFrame.
'''
data.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
      <th>室</th>
      <th>厅</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68.0</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
      <td>中</td>
      <td>33.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
      <td>低</td>
      <td>25.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115.0</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
      <td>中</td>
      <td>8.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81.0</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
      <td>中</td>
      <td>4.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60.0</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
      <td>低</td>
      <td>9.0</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### 转换格式


```python
data.info()
data['室'] = data['室'].astype(int)
data['厅'] = data['厅'].astype(int)
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 2488 entries, 0 to 2487
    Data columns (total 13 columns):
    位置           2488 non-null object
    名称           2488 non-null object
    建筑面积(平方米)    2488 non-null float64
    总价（元）        2488 non-null int64
    户型           2488 non-null object
    朝向           2488 non-null object
    楼层           2488 non-null object
    每平米售价（元）     2488 non-null int64
    装修情况         2488 non-null object
    楼层属性         2488 non-null object
    层数           2488 non-null float64
    室            2488 non-null object
    厅            2488 non-null object
    dtypes: float64(2), int64(2), object(9)
    memory usage: 352.1+ KB


#### 删除重复项


```python
data.duplicated().sum()
data = data.drop_duplicates()
data.duplicated().sum()
```




    0



## 数据探索

### 感兴趣的问题：

1. 哪个位置区域的均价最高/最低？
2. 哪个区域位置的二手房出售量最高？
3. 不同朝向的售价如何？
4. 建筑面积与销售数量以及总价的关系？
5. 楼层越高均价就越高吗？
6. 哪种户型的出售量最高？
7. 在所出售的房中，哪种装修的数量最多/最少？


```python
import matplotlib.pyplot as plt
from matplotlib.font_manager import *    
from IPython.display import display
%matplotlib inline
myfont = FontProperties(fname='/Users/jia/Library/Fonts/SimHei.ttf') 
matplotlib.rcParams['axes.unicode_minus']=False
```


```python
district_price = data.groupby('位置')['每平米售价（元）'].mean().reset_index()
district_price = district_price.sort_values('每平米售价（元）',ascending=False)

fig = plt.figure(figsize=(10,6))
labels = district_price['位置']
x = np.arange(len(district_price['位置']))
height = district_price['每平米售价（元）']

plt.bar(x, height, align='center', alpha=0.6, width=0.7)
plt.xticks(x, labels,fontproperties=myfont)
plt.xlabel('广 州',fontproperties=myfont)
plt.ylabel('每平米售价',fontproperties=myfont)
plt.title('各 区 域 售 价',fontproperties=myfont)

plt.show()
```


![png](output_28_0.png)


**1 哪个位置区域的均价最高/最低？**

从上面可以看出，天河区的均价最高；增城的均价最低。
__________________________________________________________________


```python
data.groupby('位置')['名称'].count().nlargest(8)
```




    位置
    番禺    1352
    天河     600
    黄埔     255
    海珠     190
    白云      79
    增城       3
    萝岗       3
    越秀       3
    Name: 名称, dtype: int64



** 2 哪个区域位置的二手房出售量最高？**

番禺区二手房出售量最高。增城，萝岗，越秀最少。
_____________________________________


```python
ori_price = data.groupby('朝向')['每平米售价（元）'].mean().reset_index().sort_values('每平米售价（元）', ascending=False)
ori_price
```


```python
fig = plt.figure(figsize=(10,6))
labels = ori_price['朝向']
x = np.arange(len(ori_price['朝向']))
height = ori_price['每平米售价（元）']

plt.bar(x, height, align='center', alpha=0.6, width=0.6)
plt.xticks(x, labels, fontproperties=myfont)
plt.xlabel('广 州',fontproperties=myfont)
plt.ylabel('每平米售价',fontproperties=myfont)
plt.title('各 朝 向 售 价',fontproperties=myfont)

plt.show()
```


![png](output_33_0.png)


** 3 不同朝向的售价如何？**

一般而言，朝向东西两面的房子每平米售价最高，接下来是东面的房子售价次高，此外其他朝向的房子售价差异不大。

由于房屋售价还受面积，地域等因素影响较大，所以不能片面的认为，所有东西朝向的房子每平米售价都比其他朝向的房子高。
____________________________________


```python
fig = plt.figure(figsize=(6,12))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
data_300 = data[data['建筑面积(平方米)'] <= 300]
ax1.scatter(data_300['建筑面积(平方米)'], data_300['总价（元）'], alpha=0.5)
ax1.set_xlabel('建筑面积(平方米)',fontproperties=myfont)
ax1.set_ylabel('总价（元）',fontproperties=myfont)
ax2.scatter(data_300['总价（元）'], data_300['建筑面积(平方米)'], alpha=0.5)
ax2.set_xlabel('总价（元）',fontproperties=myfont)
ax2.set_ylabel('建筑面积(平方米)',fontproperties=myfont)
plt.show()
```


![png](output_35_0.png)


** 4 建筑面积与总价的关系？**

由于普通住宅面积都在300平米以下，所以只筛选出了小于300平米的数据进行分析。

从图中可以看出，大部分房源集中在200平米以下，面积大小是影响总价的一个重要因素，通常来说，面积越大，价格越高，但总价还受其他因素影响。
________________________


```python
layer_price = data.groupby('楼层属性')['每平米售价（元）'].mean().reset_index().sort_values('每平米售价（元）',ascending=False)
layer_price
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>楼层属性</th>
      <th>每平米售价（元）</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>别墅</td>
      <td>43812.428571</td>
    </tr>
    <tr>
      <th>1</th>
      <td>低</td>
      <td>41590.570259</td>
    </tr>
    <tr>
      <th>3</th>
      <td>高</td>
      <td>38389.839440</td>
    </tr>
    <tr>
      <th>0</th>
      <td>中</td>
      <td>37808.135802</td>
    </tr>
  </tbody>
</table>
</div>




```python

fig = plt.figure(figsize=(10,6))
labels = layer_price['楼层属性']
x = np.arange(len(layer_price['楼层属性']))
height = layer_price['每平米售价（元）']

plt.bar(x, height, align='center', alpha=0.6, width=0.4)
plt.xticks(x, labels, fontproperties=myfont)
plt.xlabel('广 州',fontproperties=myfont)
plt.ylabel('每平米售价',fontproperties=myfont)
plt.title('各 楼 层 售 价',fontproperties=myfont)

plt.show()
```


![png](output_38_0.png)


** 5 楼层越高均价就越高吗？**

除了别墅的单价最高外，低层的房屋售价要高于高层的房屋售价，中层的房屋售价是最低的。
___________________


```python
data.groupby('户型')['名称'].count().sort_values(ascending=False)
```




    户型
    3室2厅     900
    2室2厅     427
    2室1厅     284
    4室2厅     236
    3室1厅     211
    1室1厅     163
    1室0厅     121
    5室2厅      56
    4室1厅      26
    1室2厅      17
    5室3厅      13
    6室2厅       7
    4室3厅       6
    6室3厅       2
    7室3厅       2
    5室1厅       2
    3室3厅       2
    4室0厅       2
    5室4厅       1
    4室4厅       1
    7室2厅       1
    2室0厅       1
    20室6厅      1
    1室3厅       1
    8室1厅       1
    9室2厅       1
    Name: 名称, dtype: int64



**6 哪种户型的出售量最高？**

3室2厅的出售量最大，接下来是2室2厅和2室1厅。

_______________________


```python
deco_num = data.groupby('装修情况')['名称'].count().reset_index().sort_values('名称', ascending=False)
deco_num
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>装修情况</th>
      <th>名称</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>精</td>
      <td>1372</td>
    </tr>
    <tr>
      <th>0</th>
      <td>普通</td>
      <td>851</td>
    </tr>
    <tr>
      <th>3</th>
      <td>豪华</td>
      <td>164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>毛坯</td>
      <td>98</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig = plt.figure(figsize=(10,6))
labels = deco_num['装修情况']
x = np.arange(len(deco_num['装修情况']))
height = deco_num['名称']

plt.bar(x, height, align='center', alpha=0.6, width=0.4)
plt.xticks(x, labels, fontproperties=myfont)
plt.xlabel('广 州',fontproperties=myfont)
plt.ylabel('出售量',fontproperties=myfont)
plt.title('装 修 情 况 与 出 售 量',fontproperties=myfont)

plt.show()
```


![png](output_43_0.png)


** 7 在所出售的房中，哪种装修的数量最多/最少？**

精装修的出售最多，毛坯房最少。
______________________________

## 数据预处理


在将数据作为机器学习算法的输入之前，通常必须整理数据、调整数据格式和结构，这一流程通常称之为预处理。


```python
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>名称</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>户型</th>
      <th>朝向</th>
      <th>楼层</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
      <th>室</th>
      <th>厅</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>马赛国际公寓 珠江新城精美大单间近猎德地铁稀有户型带精装</td>
      <td>68.0</td>
      <td>3250000</td>
      <td>1室1厅</td>
      <td>西北</td>
      <td>中层/33层</td>
      <td>47794</td>
      <td>精</td>
      <td>中</td>
      <td>33.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>锦绣半岛 温馨精致三房  望花园 环境舒适 空气清新</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>3室2厅</td>
      <td>西北</td>
      <td>低层/25层</td>
      <td>34953</td>
      <td>精</td>
      <td>低</td>
      <td>25.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>五山花园一期 精装三房，配套齐全，环境好</td>
      <td>115.0</td>
      <td>7500000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/8层</td>
      <td>65217</td>
      <td>精</td>
      <td>中</td>
      <td>8.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>湖景居 ！81平米 祈福，高品味生活从点击此房开始！</td>
      <td>81.0</td>
      <td>2250000</td>
      <td>3室2厅</td>
      <td>北</td>
      <td>中层/4层</td>
      <td>27778</td>
      <td>普通</td>
      <td>中</td>
      <td>4.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>邮通小区 精装舒适  地铁物业 南向望花园  宜居小区</td>
      <td>60.0</td>
      <td>2600000</td>
      <td>2室1厅</td>
      <td>南</td>
      <td>低层/9层</td>
      <td>43333</td>
      <td>精</td>
      <td>低</td>
      <td>9.0</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = data.drop(['户型', '楼层', '名称'], axis=1)
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>朝向</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
      <th>室</th>
      <th>厅</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>68.0</td>
      <td>3250000</td>
      <td>西北</td>
      <td>47794</td>
      <td>精</td>
      <td>中</td>
      <td>33.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>96.7</td>
      <td>3380000</td>
      <td>西北</td>
      <td>34953</td>
      <td>精</td>
      <td>低</td>
      <td>25.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>115.0</td>
      <td>7500000</td>
      <td>北</td>
      <td>65217</td>
      <td>精</td>
      <td>中</td>
      <td>8.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>81.0</td>
      <td>2250000</td>
      <td>北</td>
      <td>27778</td>
      <td>普通</td>
      <td>中</td>
      <td>4.0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>60.0</td>
      <td>2600000</td>
      <td>南</td>
      <td>43333</td>
      <td>精</td>
      <td>低</td>
      <td>9.0</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 2485 entries, 0 to 2487
    Data columns (total 10 columns):
    位置           2485 non-null object
    建筑面积(平方米)    2485 non-null float64
    总价（元）        2485 non-null int64
    朝向           2485 non-null object
    每平米售价（元）     2485 non-null int64
    装修情况         2485 non-null object
    楼层属性         2485 non-null object
    层数           2485 non-null float64
    室            2485 non-null int64
    厅            2485 non-null int64
    dtypes: float64(2), int64(4), object(4)
    memory usage: 213.6+ KB



```python
data['层数'] = data['层数'].astype(int)
```

### 对数字特征进行标准化

对数据进行缩放不会更改每个特征的分布形状；但是，标准化可以确保在应用监督式学习器时，能够平等地对待每个特征。但应用缩放之后，原始形式的数据将不再具有相同的原始含义。


```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler() # default=(0, 1)
numerical = ['建筑面积(平方米)', '总价（元）', '每平米售价（元）', '层数', '室', '厅']
data[numerical] = scaler.fit_transform(data[numerical])
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>位置</th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>朝向</th>
      <th>每平米售价（元）</th>
      <th>装修情况</th>
      <th>楼层属性</th>
      <th>层数</th>
      <th>室</th>
      <th>厅</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天河</td>
      <td>0.075829</td>
      <td>0.085196</td>
      <td>西北</td>
      <td>0.300459</td>
      <td>精</td>
      <td>中</td>
      <td>0.666667</td>
      <td>0.000000</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>番禺</td>
      <td>0.121169</td>
      <td>0.088827</td>
      <td>西北</td>
      <td>0.211781</td>
      <td>精</td>
      <td>低</td>
      <td>0.488889</td>
      <td>0.105263</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>天河</td>
      <td>0.150079</td>
      <td>0.203911</td>
      <td>北</td>
      <td>0.420780</td>
      <td>精</td>
      <td>中</td>
      <td>0.111111</td>
      <td>0.105263</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>番禺</td>
      <td>0.096367</td>
      <td>0.057263</td>
      <td>北</td>
      <td>0.162232</td>
      <td>普通</td>
      <td>中</td>
      <td>0.022222</td>
      <td>0.105263</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>天河</td>
      <td>0.063191</td>
      <td>0.067039</td>
      <td>南</td>
      <td>0.269652</td>
      <td>精</td>
      <td>低</td>
      <td>0.133333</td>
      <td>0.052632</td>
      <td>0.166667</td>
    </tr>
  </tbody>
</table>
</div>



### 转换非数字特征

通常，学习算法都预期输入是数字，这就需要转换非数字特征（称为分类变量）。一种转换分类变量的常见方式是独热编码方法。独热编码会为每个非数字特征的每个可能类别创建一个_“虚拟”_变量。例如，假设 someFeature 有三个潜在条目：A、B 或 C。我们将此特征编码为 someFeature_A、someFeature_B 和 someFeature_C。


```python
unnumerical = ['位置', '朝向', '装修情况', '楼层属性']
data = pd.get_dummies(data)

data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>建筑面积(平方米)</th>
      <th>总价（元）</th>
      <th>每平米售价（元）</th>
      <th>层数</th>
      <th>室</th>
      <th>厅</th>
      <th>位置_增城</th>
      <th>位置_天河</th>
      <th>位置_海珠</th>
      <th>位置_番禺</th>
      <th>...</th>
      <th>朝向_西北</th>
      <th>朝向_西南</th>
      <th>装修情况_普通</th>
      <th>装修情况_毛坯</th>
      <th>装修情况_精</th>
      <th>装修情况_豪华</th>
      <th>楼层属性_中</th>
      <th>楼层属性_低</th>
      <th>楼层属性_别墅</th>
      <th>楼层属性_高</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.075829</td>
      <td>0.085196</td>
      <td>0.300459</td>
      <td>0.666667</td>
      <td>0.000000</td>
      <td>0.166667</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.121169</td>
      <td>0.088827</td>
      <td>0.211781</td>
      <td>0.488889</td>
      <td>0.105263</td>
      <td>0.333333</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.150079</td>
      <td>0.203911</td>
      <td>0.420780</td>
      <td>0.111111</td>
      <td>0.105263</td>
      <td>0.333333</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.096367</td>
      <td>0.057263</td>
      <td>0.162232</td>
      <td>0.022222</td>
      <td>0.105263</td>
      <td>0.333333</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.063191</td>
      <td>0.067039</td>
      <td>0.269652</td>
      <td>0.133333</td>
      <td>0.052632</td>
      <td>0.166667</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 32 columns</p>
</div>



### 数据拆分


```python
# Split the data into features and target label
label = data['总价（元）']
features = data.drop('总价（元）', axis=1)
```


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features,
                                                    label,
                                                    test_size = 0.2,
                                                    random_state = 0)
print("Training set has {} samples.".format(X_train.shape[0]))
print("Testing set has {} samples.".format(X_test.shape[0]))
```

    Training set has 1988 samples.
    Testing set has 497 samples.


### 模型构建


```python
from sklearn.metrics import make_scorer, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV, ShuffleSplit

def fit_model(X, y):
    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(n_splits=10, test_size=0.20, random_state=42)
    regressor = DecisionTreeRegressor(random_state=42)
    params = {'max_depth': np.arange(1,15)}
    scoring_fnc = make_scorer(r2_score)
    grid = GridSearchCV(regressor, params, scoring=scoring_fnc, cv=cv_sets)
    grid = grid.fit(X, y)
    return grid.best_estimator_

```


```python
reg = fit_model(X_train, y_train)
print("Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth']))
```

    Parameter 'max_depth' is 10 for the optimal model.


### 模型评估


```python
y_pred = reg.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("Optimal model has R^2 score {:,.2f} on test data".format(r2))
```

    Optimal model has R^2 score 0.95 on test data

