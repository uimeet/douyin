# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.toutiao.oauth2.api_client import ApiClient


class DefaultApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oauth_access_token_get(self, client_key, client_secret, code, grant_type, **kwargs):
        """获取access_token

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_access_token_get(client_key, client_secret, code, grant_type, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str code: 授权码 (required)
        :param str grant_type: (required)
        :return: OauthAccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, **kwargs)
        else:
            (data) = self.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, **kwargs)
            return data

    def oauth_access_token_get_with_http_info(self, client_key, client_secret, code, grant_type, **kwargs):
        """获取access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str code: 授权码 (required)
        :param str grant_type: (required)
        :return: OauthAccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'client_secret', 'code', 'grant_type']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_access_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `oauth_access_token_get`")
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth_access_token_get`")
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `oauth_access_token_get`")
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth_access_token_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))
        if 'client_secret' in params:
            query_params.append(('client_secret', params['client_secret']))
        if 'code' in params:
            query_params.append(('code', params['code']))
        if 'grant_type' in params:
            query_params.append(('grant_type', params['grant_type']))

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
            '/oauth/access_token/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthAccessTokenResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth_authorize_get(self, client_key, response_type, scope, redirect_uri, **kwargs):
        """获取授权码(code)

        注意该URL不是用来请求的, 需要展示给用户用于扫码。  在抖音APP支持端内唤醒的版本内打开的话会弹出客户端原生授权页面。  使用本接口前提:    1. 首先你需要去官网申请，使你的应用可以使用特定的Scope，具体需要哪些Scope，请查看各接口定义。    2. 其次你需要在本URL的scope字段中填上用户需要授权给你的Scope。    3. 用户授权通过后，你才可以调用相应的接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_authorize_get(client_key, response_type, scope, redirect_uri, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str response_type: 填写code (required)
        :param str scope: 应用授权作用域,多个授权作用域以英文逗号（,）分隔 (required)
        :param str redirect_uri: 授权成功后的回调地址，必须以http/https开头。 (required)
        :param str state: 用于保持请求和回调的状态
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_authorize_get_with_http_info(client_key, response_type, scope, redirect_uri, **kwargs)
        else:
            (data) = self.oauth_authorize_get_with_http_info(client_key, response_type, scope, redirect_uri, **kwargs)
            return data

    def oauth_authorize_get_with_http_info(self, client_key, response_type, scope, redirect_uri, **kwargs):
        """获取授权码(code)  # noqa: E501

        注意该URL不是用来请求的, 需要展示给用户用于扫码。  在抖音APP支持端内唤醒的版本内打开的话会弹出客户端原生授权页面。  使用本接口前提:    1. 首先你需要去官网申请，使你的应用可以使用特定的Scope，具体需要哪些Scope，请查看各接口定义。    2. 其次你需要在本URL的scope字段中填上用户需要授权给你的Scope。    3. 用户授权通过后，你才可以调用相应的接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_authorize_get_with_http_info(client_key, response_type, scope, redirect_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str response_type: 填写code (required)
        :param str scope: 应用授权作用域,多个授权作用域以英文逗号（,）分隔 (required)
        :param str redirect_uri: 授权成功后的回调地址，必须以http/https开头。 (required)
        :param str state: 用于保持请求和回调的状态
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'response_type', 'scope', 'redirect_uri', 'state']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_authorize_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `oauth_authorize_get`")
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `oauth_authorize_get`")
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `oauth_authorize_get`")
        # verify the required parameter 'redirect_uri' is set
        if ('redirect_uri' not in params or
                params['redirect_uri'] is None):
            raise ValueError("Missing the required parameter `redirect_uri` when calling `oauth_authorize_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))
        if 'response_type' in params:
            query_params.append(('response_type', params['response_type']))
        if 'scope' in params:
            query_params.append(('scope', params['scope']))
        if 'redirect_uri' in params:
            query_params.append(('redirect_uri', params['redirect_uri']))
        if 'state' in params:
            query_params.append(('state', params['state']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/oauth/authorize/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth_client_token_get(self, client_key, client_secret, grant_type, **kwargs):
        """生成client_token

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_client_token_get(client_key, client_secret, grant_type, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str grant_type: (required)
        :return: OauthClientTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_client_token_get_with_http_info(client_key, client_secret, grant_type, **kwargs)
        else:
            (data) = self.oauth_client_token_get_with_http_info(client_key, client_secret, grant_type, **kwargs)
            return data

    def oauth_client_token_get_with_http_info(self, client_key, client_secret, grant_type, **kwargs):
        """生成client_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_client_token_get_with_http_info(client_key, client_secret, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str grant_type: (required)
        :return: OauthClientTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'client_secret', 'grant_type']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_client_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `oauth_client_token_get`")
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth_client_token_get`")
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth_client_token_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))
        if 'client_secret' in params:
            query_params.append(('client_secret', params['client_secret']))
        if 'grant_type' in params:
            query_params.append(('grant_type', params['grant_type']))

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
            '/oauth/client_token/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthClientTokenResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth_refresh_token_get(self, client_key, grant_type, refresh_token, **kwargs):
        """刷新access_token

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_refresh_token_get(client_key, grant_type, refresh_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str grant_type: 填refresh_token (required)
        :param str refresh_token: 填写通过access_token获取到的refresh_token参数 (required)
        :return: OauthRefreshTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_refresh_token_get_with_http_info(client_key, grant_type, refresh_token, **kwargs)
        else:
            (data) = self.oauth_refresh_token_get_with_http_info(client_key, grant_type, refresh_token, **kwargs)
            return data

    def oauth_refresh_token_get_with_http_info(self, client_key, grant_type, refresh_token, **kwargs):
        """刷新access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_refresh_token_get_with_http_info(client_key, grant_type, refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str grant_type: 填refresh_token (required)
        :param str refresh_token: 填写通过access_token获取到的refresh_token参数 (required)
        :return: OauthRefreshTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'grant_type', 'refresh_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_refresh_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `oauth_refresh_token_get`")
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth_refresh_token_get`")
        # verify the required parameter 'refresh_token' is set
        if ('refresh_token' not in params or
                params['refresh_token'] is None):
            raise ValueError("Missing the required parameter `refresh_token` when calling `oauth_refresh_token_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))
        if 'grant_type' in params:
            query_params.append(('grant_type', params['grant_type']))
        if 'refresh_token' in params:
            query_params.append(('refresh_token', params['refresh_token']))

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
            '/oauth/refresh_token/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthRefreshTokenResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
