###UserInfoApi_oauth_userinfo_get
```python
from __future__ import print_function
import time
import douyin.open.user.user_info
from douyin.open.user.user_info.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.user.user_info.UserInfoApi()
access_token = 'access_token_example' # str | 
open_id = 'open_id_example' # str | 

try:
    # 获取用户信息
    api_response = api_instance.oauth_userinfo_get(access_token, open_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInfoApi->oauth_userinfo_get: %s\n" % e)
```
