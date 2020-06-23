###PoiSpuApi_poi_sku_sync_post
```python
from __future__ import print_function
import time
import douyin.open.poi.product
from douyin.open.poi.product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.product.PoiSpuApi()
body = douyin/open/poi/product.PoiSkuSyncBody() # PoiSkuSyncBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # SKU同步
    api_response = api_instance.poi_sku_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_sku_sync_post: %s\n" % e)
```
###PoiSpuApi_poi_spu_query_get
```python
from __future__ import print_function
import time
import douyin.open.poi.product
from douyin.open.poi.product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.product.PoiSpuApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
spu_ext_id = 'spu_ext_id_example' # str | 

try:
    # 查询SPU
    api_response = api_instance.poi_spu_query_get(access_token, spu_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_spu_query_get: %s\n" % e)
```
###PoiSpuApi_poi_spu_sync_post
```python
from __future__ import print_function
import time
import douyin.open.poi.product
from douyin.open.poi.product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.product.PoiSpuApi()
body = douyin/open/poi/product.PoiSpuSyncBody() # PoiSpuSyncBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # SPU同步
    api_response = api_instance.poi_spu_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_spu_sync_post: %s\n" % e)
```
