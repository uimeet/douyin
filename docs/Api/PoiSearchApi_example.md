###PoiSearchApi_poi_search_keyword_get
```python
from __future__ import print_function
import time
import douyin.open.video_poi
from douyin.open.video_poi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_poi.PoiSearchApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
count = 10 # int | 每页数量
keyword = 'keyword_example' # str | 查询关键字，例如美食
cursor = 0 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)
city = 'city_example' # str | 查询城市，例如上海、北京 (optional)

try:
    # 关键字搜索
    api_response = api_instance.poi_search_keyword_get(access_token, count, keyword, cursor=cursor, city=city)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSearchApi->poi_search_keyword_get: %s\n" % e)
```
