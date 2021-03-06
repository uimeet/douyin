# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.poi.product.api_client import ApiClient


class PoiSpuApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def poi_sku_sync_post(self, body, access_token, **kwargs):
        """SKU同步

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_sku_sync_post(body, access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param PoiSkuSyncBody body: (required)
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: PoiSkuSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_sku_sync_post_with_http_info(body, access_token, **kwargs)
        else:
            (data) = self.poi_sku_sync_post_with_http_info(body, access_token, **kwargs)
            return data

    def poi_sku_sync_post_with_http_info(self, body, access_token, **kwargs):
        """SKU同步  # noqa: E501

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_sku_sync_post_with_http_info(body, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PoiSkuSyncBody body: (required)
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: PoiSkuSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_sku_sync_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `poi_sku_sync_post`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `poi_sku_sync_post`")

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
            '/poi/sku/sync/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiSkuSyncResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_spu_query_get(self, access_token, spu_ext_id, **kwargs):
        """查询SPU

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_spu_query_get(access_token, spu_ext_id, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param str spu_ext_id: (required)
        :return: PoiSpuQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_spu_query_get_with_http_info(access_token, spu_ext_id, **kwargs)
        else:
            (data) = self.poi_spu_query_get_with_http_info(access_token, spu_ext_id, **kwargs)
            return data

    def poi_spu_query_get_with_http_info(self, access_token, spu_ext_id, **kwargs):
        """查询SPU  # noqa: E501

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_spu_query_get_with_http_info(access_token, spu_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param str spu_ext_id: (required)
        :return: PoiSpuQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'spu_ext_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_spu_query_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `poi_spu_query_get`")
        # verify the required parameter 'spu_ext_id' is set
        if ('spu_ext_id' not in params or
                params['spu_ext_id'] is None):
            raise ValueError("Missing the required parameter `spu_ext_id` when calling `poi_spu_query_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'spu_ext_id' in params:
            query_params.append(('spu_ext_id', params['spu_ext_id']))

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
            '/poi/spu/query/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiSpuQueryResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_spu_sync_post(self, body, access_token, **kwargs):
        """SPU同步

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_spu_sync_post(body, access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param PoiSpuSyncBody body: (required)
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: PoiSpuSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_spu_sync_post_with_http_info(body, access_token, **kwargs)
        else:
            (data) = self.poi_spu_sync_post_with_http_info(body, access_token, **kwargs)
            return data

    def poi_spu_sync_post_with_http_info(self, body, access_token, **kwargs):
        """SPU同步  # noqa: E501

        * Scope: `poi.product` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_spu_sync_post_with_http_info(body, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PoiSpuSyncBody body: (required)
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: PoiSpuSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_spu_sync_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `poi_spu_sync_post`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `poi_spu_sync_post`")

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
            '/poi/spu/sync/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiSpuSyncResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
