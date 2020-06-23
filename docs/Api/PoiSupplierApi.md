# douyin.open.poi.supplier.PoiSupplierApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_query_get**](PoiSupplierApi.md#poi_query_get) | **GET** /poi/query/ | 获取抖音POI ID
[**poi_supplier_query_get**](PoiSupplierApi.md#poi_supplier_query_get) | **GET** /poi/supplier/query/ | 查询店铺
[**poi_supplier_sync_post**](PoiSupplierApi.md#poi_supplier_sync_post) | **POST** /poi/supplier/sync/ | 商铺同步

# **poi_query_get**
> PoiQueryResponse poi_query_get(access_token, amap_id)

获取抖音POI ID

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.poi.supplier
from douyin.open.poi.supplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.supplier.PoiSupplierApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
amap_id = 'amap_id_example' # str | 

try:
    # 获取抖音POI ID
    api_response = api_instance.poi_query_get(access_token, amap_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **amap_id** | **str**|  | 

### Return type

[**PoiQueryResponse**](PoiQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_query_get**
> PoiSupplierQueryResponse poi_supplier_query_get(access_token, supplier_ext_id)

查询店铺

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.poi.supplier
from douyin.open.poi.supplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.supplier.PoiSupplierApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
supplier_ext_id = 'supplier_ext_id_example' # str | 

try:
    # 查询店铺
    api_response = api_instance.poi_supplier_query_get(access_token, supplier_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **supplier_ext_id** | **str**|  | 

### Return type

[**PoiSupplierQueryResponse**](PoiSupplierQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_sync_post**
> PoiSupplierSyncResponse poi_supplier_sync_post(body, access_token)

商铺同步

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.poi.supplier
from douyin.open.poi.supplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.poi.supplier.PoiSupplierApi()
body = douyin/open/poi/supplier.PoiSupplierSyncBody() # PoiSupplierSyncBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 商铺同步
    api_response = api_instance.poi_supplier_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoiSupplierSyncBody**](PoiSupplierSyncBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**PoiSupplierSyncResponse**](PoiSupplierSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

