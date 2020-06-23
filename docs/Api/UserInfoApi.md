# douyin.open.user.user_info.UserInfoApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_userinfo_get**](UserInfoApi.md#oauth_userinfo_get) | **GET** /oauth/userinfo/ | 获取用户信息

# **oauth_userinfo_get**
> OauthUserinfoResponse oauth_userinfo_get(access_token, open_id)

获取用户信息

* Scope: `user_info` 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **open_id** | **str**|  | 

### Return type

[**OauthUserinfoResponse**](OauthUserinfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

