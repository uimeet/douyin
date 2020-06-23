###EnterpriseLeadsApi_enterprise_leads_tag_create_post
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
###EnterpriseLeadsApi_enterprise_leads_tag_delete_post
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
###EnterpriseLeadsApi_enterprise_leads_tag_list_get
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
###EnterpriseLeadsApi_enterprise_leads_tag_update_post
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
###EnterpriseLeadsApi_enterprise_leads_tag_user_list_get
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
###EnterpriseLeadsApi_enterprise_leads_tag_user_update_post
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
###EnterpriseLeadsApi_enterprise_leads_user_action_list_get
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
###EnterpriseLeadsApi_enterprise_leads_user_detail_get
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
###EnterpriseLeadsApi_enterprise_leads_user_list_get
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
