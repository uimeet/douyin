# douyin.open.enterprise_leads.EnterpriseLeadsApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_leads_tag_create_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_create_post) | **POST** /enterprise/leads/tag/create/ | 创建标签
[**enterprise_leads_tag_delete_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_delete_post) | **POST** /enterprise/leads/tag/delete/ | 删除标签
[**enterprise_leads_tag_list_get**](EnterpriseLeadsApi.md#enterprise_leads_tag_list_get) | **GET** /enterprise/leads/tag/list/ | 获取标签列表
[**enterprise_leads_tag_update_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_update_post) | **POST** /enterprise/leads/tag/update/ | 编辑标签
[**enterprise_leads_tag_user_list_get**](EnterpriseLeadsApi.md#enterprise_leads_tag_user_list_get) | **GET** /enterprise/leads/tag/user/list/ | 获取打标签的用户列表
[**enterprise_leads_tag_user_update_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_user_update_post) | **POST** /enterprise/leads/tag/user/update/ | 给用户设置标签
[**enterprise_leads_user_action_list_get**](EnterpriseLeadsApi.md#enterprise_leads_user_action_list_get) | **GET** /enterprise/leads/user/action/list/ | 获取意向用户互动记录
[**enterprise_leads_user_detail_get**](EnterpriseLeadsApi.md#enterprise_leads_user_detail_get) | **GET** /enterprise/leads/user/detail/ | 获取意向用户详情
[**enterprise_leads_user_list_get**](EnterpriseLeadsApi.md#enterprise_leads_user_list_get) | **GET** /enterprise/leads/user/list/ | 获取意向用户列表

# **enterprise_leads_tag_create_post**
> EnterpriseLeadsTagCreateResponse enterprise_leads_tag_create_post(open_id, access_token, body=body)

创建标签

* Scope: `enterprise.data` * 一个企业号最多创建100个标签 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/enterprise_leads.EnterpriseLeadsTagCreateBody() # EnterpriseLeadsTagCreateBody |  (optional)

try:
    # 创建标签
    api_response = api_instance.enterprise_leads_tag_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**EnterpriseLeadsTagCreateBody**](EnterpriseLeadsTagCreateBody.md)|  | [optional] 

### Return type

[**EnterpriseLeadsTagCreateResponse**](EnterpriseLeadsTagCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_delete_post**
> EnterpriseLeadsTagDeleteResponse enterprise_leads_tag_delete_post(open_id, access_token, body=body)

删除标签

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/enterprise_leads.EnterpriseLeadsTagDeleteBody() # EnterpriseLeadsTagDeleteBody |  (optional)

try:
    # 删除标签
    api_response = api_instance.enterprise_leads_tag_delete_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**EnterpriseLeadsTagDeleteBody**](EnterpriseLeadsTagDeleteBody.md)|  | [optional] 

### Return type

[**EnterpriseLeadsTagDeleteResponse**](EnterpriseLeadsTagDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_list_get**
> EnterpriseLeadsTagListResponse enterprise_leads_tag_list_get(open_id, access_token, count, cursor=cursor)

获取标签列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
cursor = 56 # int | 分页游标 (optional)

try:
    # 获取标签列表
    api_response = api_instance.enterprise_leads_tag_list_get(open_id, access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标 | [optional] 

### Return type

[**EnterpriseLeadsTagListResponse**](EnterpriseLeadsTagListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_update_post**
> EnterpriseLeadsTagCreateResponse enterprise_leads_tag_update_post(open_id, access_token, body=body)

编辑标签

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/enterprise_leads.EnterpriseLeadsTagUpdateBody() # EnterpriseLeadsTagUpdateBody |  (optional)

try:
    # 编辑标签
    api_response = api_instance.enterprise_leads_tag_update_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**EnterpriseLeadsTagUpdateBody**](EnterpriseLeadsTagUpdateBody.md)|  | [optional] 

### Return type

[**EnterpriseLeadsTagCreateResponse**](EnterpriseLeadsTagCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_user_list_get**
> EnterpriseLeadsTagUserListResponse enterprise_leads_tag_user_list_get(open_id, access_token, count, tag_id, cursor=cursor)

获取打标签的用户列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
tag_id = 56 # int | 
cursor = 56 # int | 分页游标 (optional)

try:
    # 获取打标签的用户列表
    api_response = api_instance.enterprise_leads_tag_user_list_get(open_id, access_token, count, tag_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **tag_id** | **int**|  | 
 **cursor** | **int**| 分页游标 | [optional] 

### Return type

[**EnterpriseLeadsTagUserListResponse**](EnterpriseLeadsTagUserListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_user_update_post**
> EnterpriseLeadsTagDeleteResponse enterprise_leads_tag_user_update_post(open_id, access_token, body=body)

给用户设置标签

* Scope: `enterprise.data` * 一个用户最多设置5个标签 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/enterprise_leads.EnterpriseLeadsTagUserUpdateBody() # EnterpriseLeadsTagUserUpdateBody |  (optional)

try:
    # 给用户设置标签
    api_response = api_instance.enterprise_leads_tag_user_update_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_user_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**EnterpriseLeadsTagUserUpdateBody**](EnterpriseLeadsTagUserUpdateBody.md)|  | [optional] 

### Return type

[**EnterpriseLeadsTagDeleteResponse**](EnterpriseLeadsTagDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_action_list_get**
> EnterpriseLeadsUserActionListResponse enterprise_leads_user_action_list_get(open_id, access_token, count, user_id, cursor=cursor, action_type=action_type)

获取意向用户互动记录

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
user_id = 'user_id_example' # str | 
cursor = 'cursor_example' # str |  (optional)
action_type = 56 # int |  (optional)

try:
    # 获取意向用户互动记录
    api_response = api_instance.enterprise_leads_user_action_list_get(open_id, access_token, count, user_id, cursor=cursor, action_type=action_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_action_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **user_id** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **action_type** | **int**|  | [optional] 

### Return type

[**EnterpriseLeadsUserActionListResponse**](EnterpriseLeadsUserActionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_detail_get**
> EnterpriseLeadsUserDetailResponse enterprise_leads_user_detail_get(open_id, access_token, user_id)

获取意向用户详情

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
user_id = 'user_id_example' # str | 

try:
    # 获取意向用户详情
    api_response = api_instance.enterprise_leads_user_detail_get(open_id, access_token, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **user_id** | **str**|  | 

### Return type

[**EnterpriseLeadsUserDetailResponse**](EnterpriseLeadsUserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_list_get**
> EnterpriseLeadsUserListResponse enterprise_leads_user_list_get(open_id, access_token, count, start_time, end_time, action_type, cursor=cursor, leads_level=leads_level)

获取意向用户列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin.open.enterprise_leads
from douyin.open.enterprise_leads.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.enterprise_leads.EnterpriseLeadsApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
start_time = 56 # int | 
end_time = 56 # int | 
action_type = 56 # int | 分类:   * `0` - 全部   * `1` - 私信互动   * `2` - 组件互动   * `3` - 主页互动 
cursor = 56 # int | 分页游标 (optional)
leads_level = 56 # int | 用户状态:   * `-1` - 没兴趣   * `0` - 了解   * `1` - 有兴趣   * `2` - 有意愿   * `10` - 已转化  (optional)

try:
    # 获取意向用户列表
    api_response = api_instance.enterprise_leads_user_list_get(open_id, access_token, count, start_time, end_time, action_type, cursor=cursor, leads_level=leads_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **action_type** | **int**| 分类:   * &#x60;0&#x60; - 全部   * &#x60;1&#x60; - 私信互动   * &#x60;2&#x60; - 组件互动   * &#x60;3&#x60; - 主页互动  | 
 **cursor** | **int**| 分页游标 | [optional] 
 **leads_level** | **int**| 用户状态:   * &#x60;-1&#x60; - 没兴趣   * &#x60;0&#x60; - 了解   * &#x60;1&#x60; - 有兴趣   * &#x60;2&#x60; - 有意愿   * &#x60;10&#x60; - 已转化  | [optional] 

### Return type

[**EnterpriseLeadsUserListResponse**](EnterpriseLeadsUserListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

