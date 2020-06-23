# douyin.open.video_data.VideoDataApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_data_post**](VideoDataApi.md#video_data_post) | **POST** /video/data/ | 批量获取视频数据信息

# **video_data_post**
> VideoDataResponse video_data_post(body, open_id, access_token)

批量获取视频数据信息

* Scope: `video.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.video_data
from douyin.open.video_data.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_data.VideoDataApi()
body = douyin/open/video_data.VideoDataBody() # VideoDataBody | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 批量获取视频数据信息
    api_response = api_instance.video_data_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoDataApi->video_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VideoDataBody**](VideoDataBody.md)|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**VideoDataResponse**](VideoDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

