###PoiOrderApi_poi_ext_hotel_order_cancel_post
```python
from __future__ import print_function
import time
import douyin.open.poi.order
from douyin.open.poi.order.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.order.PoiOrderApi()
body = douyin/open/poi/order.PoiExtHotelOrderCancelBody() # PoiExtHotelOrderCancelBody |  (optional)

try:
    # 订单退款(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_cancel_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_cancel_post: %s\n" % e)
```
###PoiOrderApi_poi_ext_hotel_order_commit_post
```python
from __future__ import print_function
import time
import douyin.open.poi.order
from douyin.open.poi.order.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.order.PoiOrderApi()
body = douyin/open/poi/order.PoiExtHotelOrderCommitBody() # PoiExtHotelOrderCommitBody |  (optional)

try:
    # 下单接口(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_commit_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_commit_post: %s\n" % e)
```
###PoiOrderApi_poi_ext_hotel_order_status_post
```python
from __future__ import print_function
import time
import douyin.open.poi.order
from douyin.open.poi.order.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.order.PoiOrderApi()
body = douyin/open/poi/order.PoiExtHotelOrderStatusBody() # PoiExtHotelOrderStatusBody |  (optional)

try:
    # 订单状态通知(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_status_post: %s\n" % e)
```
###PoiOrderApi_poi_order_status_post
```python
from __future__ import print_function
import time
import douyin.open.poi.order
from douyin.open.poi.order.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.order.PoiOrderApi()
body = douyin/open/poi/order.PoiOrderStatusBody() # PoiOrderStatusBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 订单状态同步接口
    api_response = api_instance.poi_order_status_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_order_status_post: %s\n" % e)
```
