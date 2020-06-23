# douyin.open.sandbox.SandboxApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_webhook_event_send_post**](SandboxApi.md#sandbox_webhook_event_send_post) | **POST** /sandbox/webhook/event/send/ | 模拟webhook事件

# **sandbox_webhook_event_send_post**
> CommonResponse sandbox_webhook_event_send_post(body, access_token)

模拟webhook事件

### Example
```python
from __future__ import print_function
import time
import douyin.open.sandbox
from douyin.open.sandbox.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.sandbox.SandboxApi()
body = douyin/open/sandbox.SandboxWebhookEventSendBody() # SandboxWebhookEventSendBody | 
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 模拟webhook事件
    api_response = api_instance.sandbox_webhook_event_send_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_webhook_event_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxWebhookEventSendBody**](SandboxWebhookEventSendBody.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

