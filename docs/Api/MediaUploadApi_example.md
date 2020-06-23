###MediaUploadApi_media_upload_post
```python
from __future__ import print_function
import time
import douyin.open.media_upload
from douyin.open.media_upload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.media_upload.MediaUploadApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
media = 'media_example' # str |  (optional)

try:
    # 上传素材
    api_response = api_instance.media_upload_post(open_id, access_token, media=media)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaUploadApi->media_upload_post: %s\n" % e)
```
