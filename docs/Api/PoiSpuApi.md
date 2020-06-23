# douyin.open.poi.product.PoiSpuApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_sku_sync_post**](PoiSpuApi.md#poi_sku_sync_post) | **POST** /poi/sku/sync/ | SKU同步
[**poi_spu_query_get**](PoiSpuApi.md#poi_spu_query_get) | **GET** /poi/spu/query/ | 查询SPU
[**poi_spu_sync_post**](PoiSpuApi.md#poi_spu_sync_post) | **POST** /poi/spu/sync/ | SPU同步

# **poi_sku_sync_post**
> PoiSkuSyncResponse poi_sku_sync_post(body, access_token)

SKU同步

* Scope: `poi.product` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiSkuSyncBody**](PoiSkuSyncBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**PoiSkuSyncResponse**](PoiSkuSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_spu_query_get**
> PoiSpuQueryResponse poi_spu_query_get(access_token, spu_ext_id)

查询SPU

* Scope: `poi.product` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **spu_ext_id** | **str**|  | 

### Return type

[**PoiSpuQueryResponse**](PoiSpuQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_spu_sync_post**
> PoiSpuSyncResponse poi_spu_sync_post(body, access_token)

SPU同步

* Scope: `poi.product` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiSpuSyncBody**](PoiSpuSyncBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**PoiSpuSyncResponse**](PoiSpuSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

