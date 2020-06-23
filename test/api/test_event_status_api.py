# coding: utf-8

"""
    获取应用推送事件订阅状态

    通过access_token查询该应用事件订阅状态

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.events.api.event_status_api import EventStatusApi
from douyin.open.events.rest import ApiException

from douyin.open.events.model.event_status_list_response import EventStatusListResponse
from douyin.open.events.model.event_status_update_body import EventStatusUpdateBody
from douyin.open.events.model.event_status_update_response import EventStatusUpdateResponse


class TestEventStatusApi(unittest.TestCase):
    """EventStatusApi unit test stubs"""

    def setUp(self):
        self.api = EventStatusApi()

    def tearDown(self):
        pass

    def test_event_status_list_get(self):
        """Test case for event_status_list_get

        获取事件订阅状态
        """
        
        resp = self.api.event_status_list_get(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', )
        pass

    def test_event_status_update_post(self):
        """Test case for event_status_update_post

        更新应用推送事件订阅状态
        """
        body=EventStatusUpdateBody()
        resp = self.api.event_status_update_post(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', body=body)
        pass


if __name__ == '__main__':
    unittest.main()
