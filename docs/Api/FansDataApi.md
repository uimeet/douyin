# douyin.open.fans_data.FansDataApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fans_data_get**](FansDataApi.md#fans_data_get) | **GET** /fans/data/ | 获取用户粉丝数据

# **fans_data_get**
> FansDataResponse fans_data_get(open_id, access_token)

获取用户粉丝数据

* Scope: `fans.data` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**FansDataResponse**](FansDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

