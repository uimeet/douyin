# douyin.open.events.EventStatusApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_status_list_get**](EventStatusApi.md#event_status_list_get) | **GET** /event/status/list/ | 获取事件订阅状态
[**event_status_update_post**](EventStatusApi.md#event_status_update_post) | **POST** /event/status/update/ | 更新应用推送事件订阅状态

# **event_status_list_get**
> EventStatusListResponse event_status_list_get(access_token)

获取事件订阅状态

### Example
```python
from __future__ import print_function
import time
import douyin.open.events
from douyin.open.events.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.events.EventStatusApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 获取事件订阅状态
    api_response = api_instance.event_status_list_get(access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventStatusApi->event_status_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**EventStatusListResponse**](EventStatusListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_status_update_post**
> EventStatusUpdateResponse event_status_update_post(access_token, body=body)

更新应用推送事件订阅状态

### Example
```python
from __future__ import print_function
import time
import douyin.open.events
from douyin.open.events.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.events.EventStatusApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
body = douyin/open/events.EventStatusUpdateBody() # EventStatusUpdateBody |  (optional)

try:
    # 更新应用推送事件订阅状态
    api_response = api_instance.event_status_update_post(access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventStatusApi->event_status_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **body** | [**EventStatusUpdateBody**](EventStatusUpdateBody.md)|  | [optional] 

### Return type

[**EventStatusUpdateResponse**](EventStatusUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

