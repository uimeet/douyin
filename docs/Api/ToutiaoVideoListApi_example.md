###ToutiaoVideoListApi_toutiao_video_list_get
```python
from __future__ import print_function
import time
import douyin.open.toutiao.video.list
from douyin.open.toutiao.video.list.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.toutiao.video.list.ToutiaoVideoListApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
cursor = 0 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 获取用户已发布的视频，支持分页
    api_response = api_instance.toutiao_video_list_get(open_id, access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoListApi->toutiao_video_list_get: %s\n" % e)
```
