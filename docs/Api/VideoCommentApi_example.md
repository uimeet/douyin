###VideoCommentApi_video_comment_list_get
```python
from __future__ import print_function
import time
import douyin.open.video_comment
from douyin.open.video_comment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_comment.VideoCommentApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
item_id = 'item_id_example' # str | 视频id
cursor = 0 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 评论列表
    api_response = api_instance.video_comment_list_get(open_id, access_token, count, item_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_list_get: %s\n" % e)
```
###VideoCommentApi_video_comment_reply_list_get
```python
from __future__ import print_function
import time
import douyin.open.video_comment
from douyin.open.video_comment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_comment.VideoCommentApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 10 # int | 每页数量
item_id = 'item_id_example' # str | 视频id
comment_id = 'comment_id_example' # str | 评论id
cursor = 0 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 评论回复列表
    api_response = api_instance.video_comment_reply_list_get(open_id, access_token, count, item_id, comment_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_reply_list_get: %s\n" % e)
```
###VideoCommentApi_video_comment_reply_post
```python
from __future__ import print_function
import time
import douyin.open.video_comment
from douyin.open.video_comment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_comment.VideoCommentApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/video_comment.VideoCommentReplyBody() # VideoCommentReplyBody |  (optional)

try:
    # 回复视频评论
    api_response = api_instance.video_comment_reply_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_reply_post: %s\n" % e)
```
###VideoCommentApi_video_comment_top_post
```python
from __future__ import print_function
import time
import douyin.open.video_comment
from douyin.open.video_comment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_comment.VideoCommentApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/video_comment.VideoCommentTopBody() # VideoCommentTopBody |  (optional)

try:
    # 置顶视频评论(企业号)
    api_response = api_instance.video_comment_top_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_top_post: %s\n" % e)
```
