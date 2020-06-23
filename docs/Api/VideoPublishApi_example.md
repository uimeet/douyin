###VideoPublishApi_video_create_post
```python
from __future__ import print_function
import time
import douyin.open.video_create
from douyin.open.video_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_create.VideoPublishApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/video_create.VideoCreateBody() # VideoCreateBody |  (optional)

try:
    # 创建抖音视频
    api_response = api_instance.video_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_create_post: %s\n" % e)
```
###VideoPublishApi_video_part_complete_post
```python
from __future__ import print_function
import time
import douyin.open.video_create
from douyin.open.video_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_create.VideoPublishApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。

try:
    # 完成上传
    api_response = api_instance.video_part_complete_post(open_id, access_token, upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_complete_post: %s\n" % e)
```
###VideoPublishApi_video_part_init_post
```python
from __future__ import print_function
import time
import douyin.open.video_create
from douyin.open.video_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_create.VideoPublishApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 初始化上传
    api_response = api_instance.video_part_init_post(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_init_post: %s\n" % e)
```
###VideoPublishApi_video_part_upload_post
```python
from __future__ import print_function
import time
import douyin.open.video_create
from douyin.open.video_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_create.VideoPublishApi()
video = 'video_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。
part_number = 56 # int | 第几个分片，从1开始 

try:
    # 上传视频分片到文件服务器
    api_response = api_instance.video_part_upload_post(video, open_id, access_token, upload_id, part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_upload_post: %s\n" % e)
```
###VideoPublishApi_video_upload_post
```python
from __future__ import print_function
import time
import douyin.open.video_create
from douyin.open.video_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_create.VideoPublishApi()
video = 'video_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传视频到文件服务器
    api_response = api_instance.video_upload_post(video, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_upload_post: %s\n" % e)
```
