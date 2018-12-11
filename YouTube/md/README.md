
# YouTube视频数据分析及优化建议

![png](./pics/m.png)

## 背景分析

YouTube是世界著名的视频分享网站，它使用了一系列的方式来记录用户的交互行为，包括观看、喜欢、不喜欢、评论等行为。

数据记录了2006年到2018年的部分视频数据，视频数据按国家分类，不同国家的视频类别区分会有所不同，这里取的是US（美国）的数据。

#### DATA

数据来源：https://www.kaggle.com/datasnaek/youtube-new

VARIABLES：
- video_id                   
- trending_date               
- title                      
- channel_title              
- category_id  （int） 

 '1': 'Film & Animation',
 '2': 'Autos & Vehicles',
 '10': 'Music',
 '15': 'Pets & Animals',
 '17': 'Sports',
 '18': 'Short Movies',
 '19': 'Travel & Events',
 '20': 'Gaming',
 '21': 'Videoblogging',
 '22': 'People & Blogs',
 '23': 'Comedy',
 '24': 'Entertainment',
 '25': 'News & Politics',
 '26': 'Howto & Style',
 '27': 'Education',
 '28': 'Science & Technology',
 '29': 'Nonprofits & Activism',
 '30': 'Movies',
 '31': 'Anime/Animation',
 '32': 'Action/Adventure',
 '33': 'Classics',
 '34': 'Comedy',
 '35': 'Documentary',
 '36': 'Drama',
 '37': 'Family',
 '38': 'Foreign',
 '39': 'Horror',
 '40': 'Sci-Fi/Fantasy',
 '41': 'Thriller',
 '42': 'Shorts',
 '43': 'Shows',
 '44': 'Trailers'
 

- publish_time               
- tags                       
- views   （int）                  
- likes    （int）                 
- dislikes   （int）                
- comment_count    （int）         
- thumbnail_link             
- comments_disabled             
- ratings_disabled              
- video_error_or_removed        
- description



## 目标确定

我们希望视频被更多用户所观看，观看后能能产生更多的互动行为（如：点赞，评论）。

提高视频内容的质量，同时减少错误视频和被删除视频推送给用户。

主要通过对观看、喜欢、不喜欢以及评论数等对以下四个方面进行分析：

1. 关注情况分析
2. 转化率分析
3. 质量分析
4. 词频分析

最终能对视频运营情况进行监控，并提出优化策略。

## 数据加载及预处理


```python
import pandas as pd

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
```


```python
df = pd.read_csv('USvideos.csv')
df.head()
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
      <th>video_id</th>
      <th>trending_date</th>
      <th>title</th>
      <th>channel_title</th>
      <th>category_id</th>
      <th>publish_time</th>
      <th>tags</th>
      <th>views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>comment_count</th>
      <th>thumbnail_link</th>
      <th>comments_disabled</th>
      <th>ratings_disabled</th>
      <th>video_error_or_removed</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2kyS6SvSYSE</td>
      <td>17.14.11</td>
      <td>WE WANT TO TALK ABOUT OUR MARRIAGE</td>
      <td>CaseyNeistat</td>
      <td>22</td>
      <td>2017-11-13T17:13:01.000Z</td>
      <td>SHANtell martin</td>
      <td>748374</td>
      <td>57527</td>
      <td>2966</td>
      <td>15954</td>
      <td>https://i.ytimg.com/vi/2kyS6SvSYSE/default.jpg</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>SHANTELL'S CHANNEL - https://www.youtube.com/s...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1ZAPwfrtAFY</td>
      <td>17.14.11</td>
      <td>The Trump Presidency: Last Week Tonight with J...</td>
      <td>LastWeekTonight</td>
      <td>24</td>
      <td>2017-11-13T07:30:00.000Z</td>
      <td>last week tonight trump presidency|"last week ...</td>
      <td>2418783</td>
      <td>97185</td>
      <td>6146</td>
      <td>12703</td>
      <td>https://i.ytimg.com/vi/1ZAPwfrtAFY/default.jpg</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>One year after the presidential election, John...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5qpjK5DgCt4</td>
      <td>17.14.11</td>
      <td>Racist Superman | Rudy Mancuso, King Bach &amp; Le...</td>
      <td>Rudy Mancuso</td>
      <td>23</td>
      <td>2017-11-12T19:05:24.000Z</td>
      <td>racist superman|"rudy"|"mancuso"|"king"|"bach"...</td>
      <td>3191434</td>
      <td>146033</td>
      <td>5339</td>
      <td>8181</td>
      <td>https://i.ytimg.com/vi/5qpjK5DgCt4/default.jpg</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>WATCH MY PREVIOUS VIDEO ▶ \n\nSUBSCRIBE ► http...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>puqaWrEC7tY</td>
      <td>17.14.11</td>
      <td>Nickelback Lyrics: Real or Fake?</td>
      <td>Good Mythical Morning</td>
      <td>24</td>
      <td>2017-11-13T11:00:04.000Z</td>
      <td>rhett and link|"gmm"|"good mythical morning"|"...</td>
      <td>343168</td>
      <td>10172</td>
      <td>666</td>
      <td>2146</td>
      <td>https://i.ytimg.com/vi/puqaWrEC7tY/default.jpg</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Today we find out if Link is a Nickelback amat...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d380meD0W0M</td>
      <td>17.14.11</td>
      <td>I Dare You: GOING BALD!?</td>
      <td>nigahiga</td>
      <td>24</td>
      <td>2017-11-12T18:01:41.000Z</td>
      <td>ryan|"higa"|"higatv"|"nigahiga"|"i dare you"|"...</td>
      <td>2095731</td>
      <td>132235</td>
      <td>1989</td>
      <td>17518</td>
      <td>https://i.ytimg.com/vi/d380meD0W0M/default.jpg</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>I know it's been a while since we did this sho...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()
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
      <th>category_id</th>
      <th>views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>comment_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>40949.000000</td>
      <td>4.094900e+04</td>
      <td>4.094900e+04</td>
      <td>4.094900e+04</td>
      <td>4.094900e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.972429</td>
      <td>2.360785e+06</td>
      <td>7.426670e+04</td>
      <td>3.711401e+03</td>
      <td>8.446804e+03</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.568327</td>
      <td>7.394114e+06</td>
      <td>2.288853e+05</td>
      <td>2.902971e+04</td>
      <td>3.743049e+04</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>5.490000e+02</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>17.000000</td>
      <td>2.423290e+05</td>
      <td>5.424000e+03</td>
      <td>2.020000e+02</td>
      <td>6.140000e+02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>24.000000</td>
      <td>6.818610e+05</td>
      <td>1.809100e+04</td>
      <td>6.310000e+02</td>
      <td>1.856000e+03</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000000</td>
      <td>1.823157e+06</td>
      <td>5.541700e+04</td>
      <td>1.938000e+03</td>
      <td>5.755000e+03</td>
    </tr>
    <tr>
      <th>max</th>
      <td>43.000000</td>
      <td>2.252119e+08</td>
      <td>5.613827e+06</td>
      <td>1.674420e+06</td>
      <td>1.361580e+06</td>
    </tr>
  </tbody>
</table>
</div>



### 查看各属性变量类型并检测缺失值


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 40949 entries, 0 to 40948
    Data columns (total 16 columns):
    video_id                  40949 non-null object
    trending_date             40949 non-null object
    title                     40949 non-null object
    channel_title             40949 non-null object
    category_id               40949 non-null int64
    publish_time              40949 non-null object
    tags                      40949 non-null object
    views                     40949 non-null int64
    likes                     40949 non-null int64
    dislikes                  40949 non-null int64
    comment_count             40949 non-null int64
    thumbnail_link            40949 non-null object
    comments_disabled         40949 non-null bool
    ratings_disabled          40949 non-null bool
    video_error_or_removed    40949 non-null bool
    description               40379 non-null object
    dtypes: bool(3), int64(5), object(8)
    memory usage: 4.2+ MB


### 检测重复值并处理


```python
df.duplicated().sum()
```




    48




```python
df.drop_duplicates(inplace=True)
```


```python
df.to_csv('cleaned_videos.csv', index=False)
```

#### （由于Tableau具有很好的可视化效果，接下来的分析采用Tableau进行）
## 一. 关注情况分析
（某类）总次数 = 视频数量 * （某类）平均次数

- (某个类别的)观看总次数 = (这个类别的)视频数量 * (这个类别的)平均观看次数
- (某个类别的)喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均喜欢次数
- (某个类别的)不喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均不喜欢次数
- (某个类别的)评论总次数 = (这个类别的)视频数量 * (这个类别的)平均评论次数

从视频数量和平均行为次数的角度对用户行为（观看、喜欢、不喜欢、评论）进行分析。

### 1. 不同类别视频的关注情况分析
![png](./pics/total_num.png)

** 分析 **

类别ID为10和24的视频获得的view, likes, dislikes, 还是comments总数都是最多的。

接下来将分析是哪些原因导致这些类别的视频获得了较多的views, likes, dislikes, 和comments.

### 2. 影响因素分析
行为总次数 = 视频数量 * 平均行为次数

- (某个类别的)观看总次数 = (这个类别的)视频数量 * (这个类别的)平均观看次数
- (某个类别的)喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均喜欢次数
- (某个类别的)不喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均不喜欢次数
- (某个类别的)评论总次数 = (这个类别的)视频数量 * (这个类别的)平均评论次数

#### 2.1 不同类别的视频数量
![png](./pics/c_num.png)

** 分析 **

类别ID为10和24的视频数量最多，同时用户观看的大部分视频都是2018和2017最近着两年发布的。这也说明正因为这两类视频的数量多，因此与用户互动总数也最多。在总数上类别为10的要多于类别为24的视频，但类别为10的视频数量明显要少于类别为24的，因此我们还需要进一步分析不同类别互动（观看、喜欢、不喜欢、评论）的平均数。

#### 2.2 不同类别的平均观看次数
![png](./pics/c_avg_views.png)

** 分析 **

- (某个类别的)观看总次数 = (这个类别的)视频数量 * (这个类别的)平均观看次数

从平均观看次数看，前几名依次是类别ID为10、1、24、29、20的视频。

类别为1、20、29的视频平均观看次数大于平均值，但数量却小于平均值。

#### 2.3 不同类别的平均喜欢次数
![png](./pics/c_avg_likes.png)

** 分析 **

- (某个类别的)喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均喜欢次数

从平均喜欢数看，前几名依次是类别ID为10、29、1、23、20的视频。

类别为1、20、29的视频平均喜欢次数大于平均值，但数量却小于平均值。

#### 2.4 不同类别的平均不喜欢次数
![png](./pics/c_avg_dislikes.png)

** 分析 **

- (某个类别的)不喜欢总数 = (这个类别的)视频数量 * (这个类别的)平均不喜欢次数

从平均不喜欢次数看，前几名依次是类别ID为29、10、20、24、22的视频。

#### 2.5 不同类别的平均评论次数
![png](./pics/c_avg_comments.png)

** 分析 **

- (某个类别的)评论总次数 = (这个类别的)视频数量 * (这个类别的)平均评论次数

从平均评论次数看，前几名依次是类别ID为29、10、20、24、22的视频。

类别为20、29的视频平均评论次数大于平均值，但数量却小于平均值。

#### 2.6 观看次数与喜欢/不喜欢的关系
![png](./pics/c_views_likes-dislikes.png)

** 分析 **

图中以圆形大小表示某个类别视频的平均观看次数，圆形面积越大表示观看的次数越多，旁边的编号代表视频的类别。

通常观看的人数越多，喜欢/不喜欢的人数也越多，但也有一些类别的视频虽然观看人数并不是最多，却能调动用户的情绪，引起用户点喜欢或不喜欢。

#### 2.7 评论次数与喜欢/不喜欢的关系
![png](./pics/c_comments_likes-dislikes.png)

** 分析 **

通常情况下喜欢/不喜欢的人数越多，评论数量也会越多，几乎没有意外。说明一旦调动了用户情感就能使他们进行评论。

用户观看视频并不一定会让他们点击喜欢或不喜欢，但一旦他们喜欢或不喜欢某个视频就容易产生评论。相对观看数而言，评论数更能反映用户对视频喜欢或不喜欢。

## 二. 转化率分析

用户视频观看数（view）非常重要，但是有的时候用户可能只是误点击了视频，所以分析喜欢/不喜欢点击率、评论转换率也是非常重要的。

通过监控转换率还可以检测异常情况，防止僵尸点击和水军评论。

- 喜欢点击率 = likes数量 / views数量
- 不喜欢点击率 = dislikes数量 / views数量
- 评论转化率 = comments数量 / views数量

### 1. “喜欢”点击率
![png](./pics/rate_likes.png)

** 分析 **

用户看过视频后会点击喜欢的比率最小的是类别ID为25、17、2的视频。因此可以着重提高这几类视频的点赞数。

### 2. “不喜欢”点击率
![png](./pics/rate_dislikes.png)

** 分析 **

用户看过视频后会点击不喜欢的比率最大的是类别ID为29和25的视频。

### 3. 评论转化率
![png](./pics/rate_comments.png)

** 分析 **

用户看过视频后会进行评论的比率最小的是类别ID为20、29、25的视频。因此可以着重提高这几类视频的评论数。

### 3. 不同发布时间的视频转换率
#### 3.1 2006~2018发布的视频
![png](./pics/rate_year.png)

** 分析 **

从前面的分析我们可以知道喜欢或者不喜欢都会导致评论数的增加。2011年和2017年发布的视频是带来了两个评论高峰，而不同的是2011年造成的评论高峰很大一部分原因是不喜欢的人数较多，2017年大部分原因则是喜欢的人数较多。

#### 3.2 2017～2018最近一年发布的视频
![png](./pics/rate_month.png)

** 分析 **

在最近一年中的各转化率存在一定的波动，在波动中有小幅度上涨。其中2017年9月份各项指标最低，2018年6月最高。

而造成这些的原因与视频质量分不开，接下来将分析视频的质量。

## 三. 质量分析

likes所占百分比 = likes数量 /（likes数量+dislikes数量）

### 1. 各类别视频质量
![png](./pics/value_c.png)

** 分析 **

低于平均值的有类别:2（0.9068），17（0.9098），19（0.9275），24（0.9239），25（0.7889），29（0.9242），其中最低的是类别25（0.7889）。因此要重点监控类别为25的视频质量。


### 2. 各渠道视频质量
![png](./pics/value_title.png)

** 分析 **

上图表示likes所占百分比最低的10个渠道，因此我们需要重点监控Daily Caller, JS, Roy Moore for Senate这几个频道的质量。

### 3. 不同发布年份视频的质量
![png](./pics/value_y.png)
![png](./pics/value_m.png)

** 分析 **

2013年前的视频质量波动较大，之后虽有波动但波动较小。最近一年的视频质量（平均值为0.9290）也比过去十年（平均值为0.9016）的视频质量要高。

### 3. 出错或被删除视频分析
#### 3.1 出错或被删除视频所占比例
![png](./pics/er.png)

** 分析 **

错误或被移除的视频占0.06%（图中饼图用了不同颜色标示，但由于太小而不易察觉）。

#### 3.2 出错或被删除视频所在的类别
![png](./pics/er_c.png)

** 分析 **

出错或被删除视频主要集中在类别为1、11、24中。

#### 3.3 出错或被删除视频所在的频道
![png](./pics/er_t.png)


** 分析 **

进一步分析，出错或被删除视频在1类别中的googledoodles和Midnight频道中，在17类别中的DaHoopSpot Productions频道中，在24类别的Cobra Kai和Verizon频道中。

#### 3.3 出错或被删除视频发布年份
![png](./pics/er_y.png)

** 分析 **

出错或被删除视频发布时间集中在2017和2018年中。

## 四. 词云分析视频相关文本信息
构建词云进行分析能帮助我们了解整体的趋势，可以起到监督的作用。

主要对Title, Channel-Title, Tags, Description中的文本进行分析。


```python
df_c = pd.read_csv('cleaned_videos.csv')
```

### 1. Title


```python
plt.figure(figsize = (15,15))

stopwords = set(STOPWORDS)

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=1000,
                          max_font_size=70, 
                          random_state=42
                         ).generate(str(df_c['title']))

fig = plt.figure(1)
plt.imshow(wordcloud)
plt.title("WORD CLOUD - Title")
plt.axis('off')
plt.show()
```


![png](output_54_0.png)


** 分析 ** 

视频title中出现最多的词是：official，talk, VS, video, rudy, week, SNL

### 2. Channel Title


```python
plt.figure(figsize = (15,15))

stopwords = set(STOPWORDS)

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=1000,
                          max_font_size=60, 
                          random_state=42
                         ).generate(str(df_c['channel_title']))


fig = plt.figure(1)
plt.imshow(wordcloud)
plt.title("WORD CLOUD - Channel Title")
plt.axis('off')
plt.show()
```


![png](output_57_0.png)


** 分析 ** 

Channel Title中出现最多的词是：Rudy，night，Mancuso，Saturday，Live

### 3. Tags


```python
plt.figure(figsize = (15,15))

stopwords = set(STOPWORDS)

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=1000,
                          max_font_size=70, 
                          random_state=42
                         ).generate(str(df_c['tags']))

fig = plt.figure(1)
plt.imshow(wordcloud)
plt.title("WORD CLOUD - Tags")
plt.axis('off')
plt.show()
```


![png](output_60_0.png)


** 分析 ** 

Tags中出现最多的词是：SNL，new，week，Cream Season，TED，education

### 4. Description


```python
plt.figure(figsize = (15,15))

stopwords = set(STOPWORDS)

newStopWords= ['https', 'youtube', 'VIDEO','youtu','CHANNEL', 'WATCH']

stopwords.update(newStopWords)

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=1200,
                          max_font_size=80, 
                          random_state=42
                         ).generate(str(df_c['description']))

#print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.title("WORD CLOUD - Description")
plt.axis('off')
plt.show()
```


![png](output_63_0.png)


** 分析 ** 

Description中出现最多的词是：new，Check，now，James，MUSIC，avalilable

## 总结/建议

### 一. 关注情况分析
1. 平均观看、喜欢、不喜欢、和评论数都较高的视频类别有：10、29、1、20、22、24，因此可以多向用户推荐这几类视频。
2. 从数量上来看，只有类别为10和24的视频数量相对其他类别更多，因此我们可以想办法多提高29、1、20、22类别的视频数量，特别是类别为29的视频数量非常少。这样能提高总的观看、喜欢、不喜欢、和评论数。
3. 用户大多数观看的都是2018和2017近两年发布的视频，可见实效性非常重要。
4. 相对观看数而言，评论数更能反映用户对视频喜欢或不喜欢。

### 二. 转化率分析
1. 类别为25、17、2的视频喜欢点击率较低，因此可以着重提高这几类视频的点赞数。
2. 类别为17、2、19、1的视频评论转化率较低，因此可以着重提高这几类视频的评论数。
3. 不同发布时间的视频转换率呈波动状态，近一年（2017～2018）得到大幅提升

### 三. 视频质量分析
1. 类别为25的视频质量最差，因此需重点监控。
2. Daily Caller, JS, Roy Moore for Senate这几个频道的质量最差，因此需重点监控。
3. 最近一年视频质量的稳定性更大，质量更优。
4. 出错或被删除视频发布时间集中在2017和2018年，占总体的0.06%。分布在1类别中的googledoodles和Midnight频道中，在17类别中的DaHoopSpot Productions频道中，在24类别的Cobra Kai和Verizon频道中。

### 四. 词云分析视频相关文本信息
1. Title中出现最多的词是：official，talk, VS, video, Rudy, week, SNL
2. Channel Title中出现最多的词是：Rudy，night，Mancuso，Saturday，Live
3. Tags中出现最多的词是：SNL，new，week，Cream Season，TED，education
4. Description中出现最多的词是：new，Check，now，James，MUSIC，avalilable
