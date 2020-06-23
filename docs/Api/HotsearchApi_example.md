###HotsearchApi_hotsearch_sentences_get
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
###HotsearchApi_hotsearch_videos_get
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
