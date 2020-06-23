###ToutiaoVideoPublishApi_toutiao_video_create_post
```python
from __future__ import print_function
import time
import douyin.open.toutiao.video.create
from douyin.open.toutiao.video.create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.toutiao.video.create.ToutiaoVideoPublishApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/toutiao/video/create.ToutiaoVideoCreateBody() # ToutiaoVideoCreateBody |  (optional)

try:
    # 创建头条视频  注意：重复的video_id不会生成新的视频
    api_response = api_instance.toutiao_video_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_create_post: %s\n" % e)
```
###ToutiaoVideoPublishApi_toutiao_video_upload_post
```python
from __future__ import print_function
import time
import douyin.open.toutiao.video.create
from douyin.open.toutiao.video.create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.toutiao.video.create.ToutiaoVideoPublishApi()
video = 'video_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传视频到文件服务器
    api_response = api_instance.toutiao_video_upload_post(video, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_upload_post: %s\n" % e)
```
