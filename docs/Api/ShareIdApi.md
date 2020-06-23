# douyin.open.share_id.ShareIdApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**share_id_get**](ShareIdApi.md#share_id_get) | **GET** /share-id/ | 获取share-id

# **share_id_get**
> ShareidResponse share_id_get(access_token, need_callback=need_callback, source_style_id=source_style_id, default_hashtag=default_hashtag, link_param=link_param)

获取share-id

* Scope: `aweme.share` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.share_id
from douyin.open.share_id.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.share_id.ShareIdApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
need_callback = True # bool |  (optional)
source_style_id = 'source_style_id_example' # str | 多来源样式id（暂未开放） (optional)
default_hashtag = 'default_hashtag_example' # str | 追踪分享默认hashtag (optional)
link_param = 'link_param_example' # str | 分享来源url附加参数（暂未开放） (optional)

try:
    # 获取share-id
    api_response = api_instance.share_id_get(access_token, need_callback=need_callback, source_style_id=source_style_id, default_hashtag=default_hashtag, link_param=link_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareIdApi->share_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **need_callback** | **bool**|  | [optional] 
 **source_style_id** | **str**| 多来源样式id（暂未开放） | [optional] 
 **default_hashtag** | **str**| 追踪分享默认hashtag | [optional] 
 **link_param** | **str**| 分享来源url附加参数（暂未开放） | [optional] 

### Return type

[**ShareidResponse**](ShareidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

