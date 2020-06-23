# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.video_delete.api.video_delete_api import VideoDeleteApi
from douyin.open.video_delete.rest import ApiException

from douyin.open.video_delete.model.video_delete_body import VideoDeleteBody
from douyin.open.video_delete.model.video_delete_response import VideoDeleteResponse


class TestVideoDeleteApi(unittest.TestCase):
    """VideoDeleteApi unit test stubs"""

    def setUp(self):
        self.api = VideoDeleteApi()

    def tearDown(self):
        pass

    def test_video_delete_post(self):
        """Test case for video_delete_post

        删除授权用户发布的视频
        """
        body=VideoDeleteBody()
        resp = self.api.video_delete_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', body=body)
        pass


if __name__ == '__main__':
    unittest.main()
