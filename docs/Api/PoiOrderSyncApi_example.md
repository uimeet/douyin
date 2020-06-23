###PoiOrderSyncApi_poi_order_sync_post
```python
from __future__ import print_function
import time
import douyin.open.poi.order_sync
from douyin.open.poi.order_sync.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.order_sync.PoiOrderSyncApi()
body = douyin/open/poi/order_sync.PoiOrderSyncBody() # PoiOrderSyncBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 订单同步
    api_response = api_instance.poi_order_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderSyncApi->poi_order_sync_post: %s\n" % e)
```
