# douyin.open.im_message_send.ImApi

All URIs are relative to *https://www.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**im_message_send_post**](ImApi.md#im_message_send_post) | **POST** /im/message/send/ | 给抖音用户发送消息

# **im_message_send_post**
> ImMessageSendResponse im_message_send_post(body, open_id, access_token)

给抖音用户发送消息

* Scope: `im` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.im_message_send
from douyin.open.im_message_send.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.im_message_send.ImApi()
body = douyin/open/im_message_send.ImMessageSendBody() # ImMessageSendBody | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 给抖音用户发送消息
    api_response = api_instance.im_message_send_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImApi->im_message_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImMessageSendBody**](ImMessageSendBody.md)|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**ImMessageSendResponse**](ImMessageSendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

