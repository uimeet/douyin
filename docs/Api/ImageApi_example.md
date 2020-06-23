###ImageApi_image_create_post
```python
from __future__ import print_function
import time
import douyin.open.image_create
from douyin.open.image_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.image_create.ImageApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/image_create.ImageCreateBody() # ImageCreateBody |  (optional)

try:
    # 发布图片
    api_response = api_instance.image_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_create_post: %s\n" % e)
```
###ImageApi_image_upload_post
```python
from __future__ import print_function
import time
import douyin.open.image_create
from douyin.open.image_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.image_create.ImageApi()
image = 'image_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传图片到文件服务器
    api_response = api_instance.image_upload_post(image, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_post: %s\n" % e)
```
