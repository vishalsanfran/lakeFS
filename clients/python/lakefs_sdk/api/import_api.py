# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from lakefs_sdk.models.import_creation import ImportCreation
from lakefs_sdk.models.import_creation_response import ImportCreationResponse
from lakefs_sdk.models.import_status import ImportStatus

from lakefs_sdk.api_client import ApiClient
from lakefs_sdk.api_response import ApiResponse
from lakefs_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ImportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def import_cancel(self, repository : StrictStr, branch : StrictStr, id : Annotated[StrictStr, Field(..., description="Unique identifier of the import process")], **kwargs) -> None:  # noqa: E501
        """cancel ongoing import  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_cancel(repository, branch, id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param id: Unique identifier of the import process (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the import_cancel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.import_cancel_with_http_info(repository, branch, id, **kwargs)  # noqa: E501

    @validate_arguments
    def import_cancel_with_http_info(self, repository : StrictStr, branch : StrictStr, id : Annotated[StrictStr, Field(..., description="Unique identifier of the import process")], **kwargs) -> ApiResponse:  # noqa: E501
        """cancel ongoing import  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_cancel_with_http_info(repository, branch, id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param id: Unique identifier of the import process (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'repository',
            'branch',
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_cancel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['branch']:
            _path_params['branch'] = _params['branch']


        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/repositories/{repository}/branches/{branch}/import', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def import_start(self, repository : StrictStr, branch : StrictStr, import_creation : ImportCreation, **kwargs) -> ImportCreationResponse:  # noqa: E501
        """import data from object store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_start(repository, branch, import_creation, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param import_creation: (required)
        :type import_creation: ImportCreation
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ImportCreationResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the import_start_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.import_start_with_http_info(repository, branch, import_creation, **kwargs)  # noqa: E501

    @validate_arguments
    def import_start_with_http_info(self, repository : StrictStr, branch : StrictStr, import_creation : ImportCreation, **kwargs) -> ApiResponse:  # noqa: E501
        """import data from object store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_start_with_http_info(repository, branch, import_creation, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param import_creation: (required)
        :type import_creation: ImportCreation
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ImportCreationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'branch',
            'import_creation'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_start" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['branch']:
            _path_params['branch'] = _params['branch']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['import_creation'] is not None:
            _body_params = _params['import_creation']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '202': "ImportCreationResponse",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '420': None,
        }

        return self.api_client.call_api(
            '/repositories/{repository}/branches/{branch}/import', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def import_status(self, repository : StrictStr, branch : StrictStr, id : Annotated[StrictStr, Field(..., description="Unique identifier of the import process")], **kwargs) -> ImportStatus:  # noqa: E501
        """get import status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_status(repository, branch, id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param id: Unique identifier of the import process (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ImportStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the import_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.import_status_with_http_info(repository, branch, id, **kwargs)  # noqa: E501

    @validate_arguments
    def import_status_with_http_info(self, repository : StrictStr, branch : StrictStr, id : Annotated[StrictStr, Field(..., description="Unique identifier of the import process")], **kwargs) -> ApiResponse:  # noqa: E501
        """get import status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_status_with_http_info(repository, branch, id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param id: Unique identifier of the import process (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ImportStatus, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'branch',
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['branch']:
            _path_params['branch'] = _params['branch']


        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "ImportStatus",
            '401': "Error",
            '404': "Error",
            '420': None,
        }

        return self.api_client.call_api(
            '/repositories/{repository}/branches/{branch}/import', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
