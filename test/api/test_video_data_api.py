# coding: utf-8

"""

    通过抖音视频id批量获取已分享视频数据信息

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.video_data.api.video_data_api import VideoDataApi
from douyin.open.video_data.rest import ApiException

from douyin.open.video_data.model.video_data_body import VideoDataBody
from douyin.open.video_data.model.video_data_response import VideoDataResponse


class TestVideoDataApi(unittest.TestCase):
    """VideoDataApi unit test stubs"""

    def setUp(self):
        self.api = VideoDataApi()

    def tearDown(self):
        pass

    def test_video_data_post(self):
        """Test case for video_data_post

        批量获取视频数据信息
        """
        body=VideoDataBody()
        resp = self.api.video_data_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', body=body)
        pass


if __name__ == '__main__':
    unittest.main()
