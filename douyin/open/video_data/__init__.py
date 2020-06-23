# coding: utf-8

# flake8: noqa

"""

    通过抖音视频id批量获取已分享视频数据信息

    
"""

from __future__ import absolute_import

# import apis into sdk package
from douyin.open.video_data.api.video_data_api import VideoDataApi
# import ApiClient
from douyin.open.video_data.api_client import ApiClient
from douyin.open.video_data.configuration import Configuration
# import models into sdk package
from douyin.open.video_data.model.description import Description
from douyin.open.video_data.model.error_code import ErrorCode
from douyin.open.video_data.model.video import Video
from douyin.open.video_data.model.video_data_body import VideoDataBody
from douyin.open.video_data.model.video_data_response import VideoDataResponse
from douyin.open.video_data.model.video_data_response_data import VideoDataResponseData
from douyin.open.video_data.model.video_data_response_data_response import VideoDataResponseDataResponse
from douyin.open.video_data.model.video_statistics import VideoStatistics
