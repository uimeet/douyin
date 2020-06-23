###DefaultApi_devtool_monitor_call_post
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
