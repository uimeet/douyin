# douyin.open.image_create.ImageApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_create_post**](ImageApi.md#image_create_post) | **POST** /image/create/ | 发布图片
[**image_upload_post**](ImageApi.md#image_upload_post) | **POST** /image/upload/ | 上传图片到文件服务器

# **image_create_post**
> ImageCreateResponse image_create_post(open_id, access_token, body=body)

发布图片

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.image_create
from douyin.open.image_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.image_create.ImageApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/image_create.ImageCreateBody() # ImageCreateBody |  (optional)

try:
    # 发布图片
    api_response = api_instance.image_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**ImageCreateBody**](ImageCreateBody.md)|  | [optional] 

### Return type

[**ImageCreateResponse**](ImageCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_upload_post**
> ImageUploadResponse image_upload_post(image, open_id, access_token)

上传图片到文件服务器

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.image_create
from douyin.open.image_create.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.image_create.ImageApi()
image = 'image_example' # str | 
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传图片到文件服务器
    api_response = api_instance.image_upload_post(image, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

