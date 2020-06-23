# coding: utf-8

"""

    获取用户的粉丝数据

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.fans_data.api.fans_data_api import FansDataApi
from douyin.open.fans_data.rest import ApiException

from douyin.open.fans_data.model.fans_data_response import FansDataResponse


class TestFansDataApi(unittest.TestCase):
    """FansDataApi unit test stubs"""

    def setUp(self):
        self.api = FansDataApi()

    def tearDown(self):
        pass

    def test_fans_data_get(self):
        """Test case for fans_data_get

        获取用户粉丝数据
        """
        
        resp = self.api.fans_data_get(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', )
        print(resp)
        pass


if __name__ == '__main__':
    unittest.main()
