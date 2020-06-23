# douyin.open.toutiao.video.create.ToutiaoVideoPublishApi

All URIs are relative to *https://open.snssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**toutiao_video_create_post**](ToutiaoVideoPublishApi.md#toutiao_video_create_post) | **POST** /toutiao/video/create/ | 创建头条视频  注意：重复的video_id不会生成新的视频
[**toutiao_video_upload_post**](ToutiaoVideoPublishApi.md#toutiao_video_upload_post) | **POST** /toutiao/video/upload/ | 上传视频到文件服务器

# **toutiao_video_create_post**
> ToutiaoVideoCreateResponse toutiao_video_create_post(open_id, access_token, body=body)

创建头条视频  注意：重复的video_id不会生成新的视频

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.toutiao.video.create
from douyin.open.toutiao.video.create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.toutiao.video.create.ToutiaoVideoPublishApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/toutiao/video/create.ToutiaoVideoCreateBody() # ToutiaoVideoCreateBody |  (optional)

try:
    # 创建头条视频  注意：重复的video_id不会生成新的视频
    api_response = api_instance.toutiao_video_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**ToutiaoVideoCreateBody**](ToutiaoVideoCreateBody.md)|  | [optional] 

### Return type

[**ToutiaoVideoCreateResponse**](ToutiaoVideoCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toutiao_video_upload_post**
> ToutiaoVideoUploadResponse toutiao_video_upload_post(video, open_id, access_token)

上传视频到文件服务器

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.toutiao.video.create
from douyin.open.toutiao.video.create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.toutiao.video.create.ToutiaoVideoPublishApi()
video = 'video_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传视频到文件服务器
    api_response = api_instance.toutiao_video_upload_post(video, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **str**|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**ToutiaoVideoUploadResponse**](ToutiaoVideoUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

