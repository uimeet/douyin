###FansDataApi_fans_data_get
```python
from __future__ import print_function
import time
import douyin.open.fans_data
from douyin.open.fans_data.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.fans_data.FansDataApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 获取用户粉丝数据
    api_response = api_instance.fans_data_get(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FansDataApi->fans_data_get: %s\n" % e)
```
