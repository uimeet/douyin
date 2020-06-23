# douyin.open.user.following.FollowingListApi

All URIs are relative to *https://www.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**following_list_get**](FollowingListApi.md#following_list_get) | **GET** /following/list/ | 获取关注列表

# **following_list_get**
> FollowingListResponse following_list_get(open_id, access_token, count, cursor=cursor)

获取关注列表

* Scope: `following.list` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.user.following
from douyin.open.user.following.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.user.following.FollowingListApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
cursor = 0 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 获取关注列表
    api_response = api_instance.following_list_get(open_id, access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FollowingListApi->following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**FollowingListResponse**](FollowingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

