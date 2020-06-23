# douyin.open.devtool.monitor.DefaultApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devtool_monitor_call_post**](DefaultApi.md#devtool_monitor_call_post) | **POST** /devtool/monitor/call/ | 获取接口调用监控情况

# **devtool_monitor_call_post**
> DevtoolMonitorCallResponse devtool_monitor_call_post(access_token, time_type, begin_time, end_time, body=body)

获取接口调用监控情况

* Scope: `devtool` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.devtool.monitor
from douyin.open.devtool.monitor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.devtool.monitor.DefaultApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
time_type = 'time_type_example' # str | 时间类型
begin_time = 'begin_time_example' # str | 开始日期(20190101)
end_time = 'end_time_example' # str | 结束日期(20190101)
body = douyin/open/devtool/monitor.DevtoolMonitorCallBody() # DevtoolMonitorCallBody |  (optional)

try:
    # 获取接口调用监控情况
    api_response = api_instance.devtool_monitor_call_post(access_token, time_type, begin_time, end_time, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devtool_monitor_call_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **time_type** | **str**| 时间类型 | 
 **begin_time** | **str**| 开始日期(20190101) | 
 **end_time** | **str**| 结束日期(20190101) | 
 **body** | [**DevtoolMonitorCallBody**](DevtoolMonitorCallBody.md)|  | [optional] 

### Return type

[**DevtoolMonitorCallResponse**](DevtoolMonitorCallResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

