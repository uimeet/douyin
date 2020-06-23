# douyin.open.poi.order_sync.PoiOrderSyncApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_order_sync_post**](PoiOrderSyncApi.md#poi_order_sync_post) | **POST** /poi/order/sync/ | 订单同步

# **poi_order_sync_post**
> PoiOrderSyncResponse1 poi_order_sync_post(body, access_token)

订单同步

* Scope: `poi.product` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiOrderSyncBody**](PoiOrderSyncBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**PoiOrderSyncResponse1**](PoiOrderSyncResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

