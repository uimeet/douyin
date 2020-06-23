# douyin.open.poi.order.PoiOrderApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_ext_hotel_order_cancel_post**](PoiOrderApi.md#poi_ext_hotel_order_cancel_post) | **POST** /poi/ext/hotel/order/cancel/ | 订单退款(该接口由接入方实现)
[**poi_ext_hotel_order_commit_post**](PoiOrderApi.md#poi_ext_hotel_order_commit_post) | **POST** /poi/ext/hotel/order/commit/ | 下单接口(该接口由接入方实现)
[**poi_ext_hotel_order_status_post**](PoiOrderApi.md#poi_ext_hotel_order_status_post) | **POST** /poi/ext/hotel/order/status/ | 订单状态通知(该接口由接入方实现)
[**poi_order_status_post**](PoiOrderApi.md#poi_order_status_post) | **POST** /poi/order/status/ | 订单状态同步接口

# **poi_ext_hotel_order_cancel_post**
> PoiOrderStatusResponse poi_ext_hotel_order_cancel_post(body=body)

订单退款(该接口由接入方实现)

# 该接口由接入方实现 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiExtHotelOrderCancelBody**](PoiExtHotelOrderCancelBody.md)|  | [optional] 

### Return type

[**PoiOrderStatusResponse**](PoiOrderStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_ext_hotel_order_commit_post**
> PoiExtHotelOrderCommitResponse2 poi_ext_hotel_order_commit_post(body=body)

下单接口(该接口由接入方实现)

# 该接口由接入方实现 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiExtHotelOrderCommitBody**](PoiExtHotelOrderCommitBody.md)|  | [optional] 

### Return type

[**PoiExtHotelOrderCommitResponse2**](PoiExtHotelOrderCommitResponse2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_ext_hotel_order_status_post**
> PoiExtHotelOrderStatusResponse poi_ext_hotel_order_status_post(body=body)

订单状态通知(该接口由接入方实现)

# 该接口由接入方实现 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiExtHotelOrderStatusBody**](PoiExtHotelOrderStatusBody.md)|  | [optional] 

### Return type

[**PoiExtHotelOrderStatusResponse**](PoiExtHotelOrderStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_order_status_post**
> PoiOrderStatusResponse poi_order_status_post(body, access_token)

订单状态同步接口

* Scope: `poi.product` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiOrderStatusBody**](PoiOrderStatusBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**PoiOrderStatusResponse**](PoiOrderStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

