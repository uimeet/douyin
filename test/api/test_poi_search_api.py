# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.video_poi.api.poi_search_api import PoiSearchApi
from douyin.open.video_poi.rest import ApiException

from douyin.open.video_poi.model.poi_search_keyword_response import PoiSearchKeywordResponse


class TestPoiSearchApi(unittest.TestCase):
    """PoiSearchApi unit test stubs"""

    def setUp(self):
        self.api = PoiSearchApi()

    def tearDown(self):
        pass

    def test_poi_search_keyword_get(self):
        """Test case for poi_search_keyword_get

        关键字搜索
        """
        
        resp = self.api.poi_search_keyword_get(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', cursor=0, count=10, keyword='keyword_example', city='city_example', )
        pass


if __name__ == '__main__':
    unittest.main()
