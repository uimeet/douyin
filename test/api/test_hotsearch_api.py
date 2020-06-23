# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.hotsearch.api.hotsearch_api import HotsearchApi
from douyin.open.hotsearch.rest import ApiException

from douyin.open.hotsearch.model.hotsearch_sentences_response import HotsearchSentencesResponse
from douyin.open.hotsearch.model.hotsearch_videos_response import HotsearchVideosResponse


class TestHotsearchApi(unittest.TestCase):
    """HotsearchApi unit test stubs"""

    def setUp(self):
        self.api = HotsearchApi()

    def tearDown(self):
        pass

    def test_hotsearch_sentences_get(self):
        """Test case for hotsearch_sentences_get

        获取实时热点词
        """
        
        resp = self.api.hotsearch_sentences_get(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', )
        print(resp)
        pass

    def test_hotsearch_videos_get(self):
        """Test case for hotsearch_videos_get

        获取热点词聚合的视频
        """
        
        resp = self.api.hotsearch_videos_get(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', hot_sentence='hot_sentence_example', )
        print(resp)
        pass


if __name__ == '__main__':
    unittest.main()
