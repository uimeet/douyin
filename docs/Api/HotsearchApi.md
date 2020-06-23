# douyin.open.hotsearch.HotsearchApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hotsearch_sentences_get**](HotsearchApi.md#hotsearch_sentences_get) | **GET** /hotsearch/sentences/ | 获取实时热点词
[**hotsearch_videos_get**](HotsearchApi.md#hotsearch_videos_get) | **GET** /hotsearch/videos/ | 获取热点词聚合的视频

# **hotsearch_sentences_get**
> HotsearchSentencesResponse hotsearch_sentences_get(access_token)

获取实时热点词

* Scope: `hotsearch` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.hotsearch
from douyin.open.hotsearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.hotsearch.HotsearchApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 获取实时热点词
    api_response = api_instance.hotsearch_sentences_get(access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotsearchApi->hotsearch_sentences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**HotsearchSentencesResponse**](HotsearchSentencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotsearch_videos_get**
> HotsearchVideosResponse hotsearch_videos_get(access_token, hot_sentence)

获取热点词聚合的视频

* Scope: `hotsearch` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.hotsearch
from douyin.open.hotsearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.hotsearch.HotsearchApi()
access_token = 'clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
hot_sentence = 'hot_sentence_example' # str | 热点词

try:
    # 获取热点词聚合的视频
    api_response = api_instance.hotsearch_videos_get(access_token, hot_sentence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotsearchApi->hotsearch_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **hot_sentence** | **str**| 热点词 | 

### Return type

[**HotsearchVideosResponse**](HotsearchVideosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

