# coding: utf-8

"""
    获取应用推送事件订阅状态

    通过access_token查询该应用事件订阅状态

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.events.api_client import ApiClient


class EventStatusApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def event_status_list_get(self, access_token, **kwargs):
        """获取事件订阅状态

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.event_status_list_get(access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: EventStatusListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.event_status_list_get_with_http_info(access_token, **kwargs)
        else:
            (data) = self.event_status_list_get_with_http_info(access_token, **kwargs)
            return data

    def event_status_list_get_with_http_info(self, access_token, **kwargs):
        """获取事件订阅状态  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.event_status_list_get_with_http_info(access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: EventStatusListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method event_status_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `event_status_list_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/event/status/list/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventStatusListResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def event_status_update_post(self, access_token, **kwargs):
        """更新应用推送事件订阅状态

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.event_status_update_post(access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param EventStatusUpdateBody body:
        :return: EventStatusUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.event_status_update_post_with_http_info(access_token, **kwargs)
        else:
            (data) = self.event_status_update_post_with_http_info(access_token, **kwargs)
            return data

    def event_status_update_post_with_http_info(self, access_token, **kwargs):
        """更新应用推送事件订阅状态  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.event_status_update_post_with_http_info(access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param EventStatusUpdateBody body:
        :return: EventStatusUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method event_status_update_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `event_status_update_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/event/status/update/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventStatusUpdateResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
