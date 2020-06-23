# coding: utf-8

"""

    获取用户的粉丝数据

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.fans_data.api_client import ApiClient


class FansDataApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fans_data_get(self, open_id, access_token, **kwargs):
        """获取用户粉丝数据

        * Scope: `fans.data` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fans_data_get(open_id, access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: FansDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fans_data_get_with_http_info(open_id, access_token, **kwargs)
        else:
            (data) = self.fans_data_get_with_http_info(open_id, access_token, **kwargs)
            return data

    def fans_data_get_with_http_info(self, open_id, access_token, **kwargs):
        """获取用户粉丝数据  # noqa: E501

        * Scope: `fans.data` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fans_data_get_with_http_info(open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: FansDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['open_id', 'access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fans_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `fans_data_get`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `fans_data_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/fans/data/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FansDataResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
