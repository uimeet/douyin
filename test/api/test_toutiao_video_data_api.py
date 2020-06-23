# coding: utf-8

"""

    通过头条视频id批量获取已分享视频数据信息

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.toutiao.video.data.api.toutiao_video_data_api import ToutiaoVideoDataApi
from douyin.open.toutiao.video.data.rest import ApiException

from douyin.open.toutiao.video.data.model.toutiao_video_data_body import ToutiaoVideoDataBody
from douyin.open.toutiao.video.data.model.toutiao_video_data_response import ToutiaoVideoDataResponse


class TestToutiaoVideoDataApi(unittest.TestCase):
    """ToutiaoVideoDataApi unit test stubs"""

    def setUp(self):
        self.api = ToutiaoVideoDataApi()

    def tearDown(self):
        pass

    def test_toutiao_video_data_post(self):
        """Test case for toutiao_video_data_post

        批量获取视频数据信息
        """
        body=ToutiaoVideoDataBody()
        resp = self.api.toutiao_video_data_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', body=body)
        pass


if __name__ == '__main__':
    unittest.main()
