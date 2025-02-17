"""
    Interpol: Interpol Red Notices API

    Interpol Red Notices Website API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.interpol.api_client import ApiClient, Endpoint as _Endpoint
from deutschland.interpol.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from deutschland.interpol.model.red_notice_detail import RedNoticeDetail
from deutschland.interpol.model.red_notice_detail_images import RedNoticeDetailImages
from deutschland.interpol.model.red_notices import RedNotices


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.notices_v1_red_get_endpoint = _Endpoint(
            settings={
                "response_type": (RedNotices,),
                "auth": [],
                "endpoint_path": "/notices/v1/red",
                "operation_id": "notices_v1_red_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "forename",
                    "name",
                    "nationality",
                    "age_max",
                    "age_min",
                    "free_text",
                    "sex_id",
                    "arrest_warrant_country_id",
                    "page",
                    "result_per_page",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "sex_id",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("sex_id",): {"EMPTY": "", "F": "F", "M": "M", "U": "U"},
                },
                "openapi_types": {
                    "forename": (str,),
                    "name": (str,),
                    "nationality": (str,),
                    "age_max": (int,),
                    "age_min": (int,),
                    "free_text": (str,),
                    "sex_id": (str,),
                    "arrest_warrant_country_id": (str,),
                    "page": (int,),
                    "result_per_page": (int,),
                },
                "attribute_map": {
                    "forename": "forename",
                    "name": "name",
                    "nationality": "nationality",
                    "age_max": "ageMax",
                    "age_min": "ageMin",
                    "free_text": "freeText",
                    "sex_id": "sexId",
                    "arrest_warrant_country_id": "arrestWarrantCountryId",
                    "page": "page",
                    "result_per_page": "resultPerPage",
                },
                "location_map": {
                    "forename": "query",
                    "name": "query",
                    "nationality": "query",
                    "age_max": "query",
                    "age_min": "query",
                    "free_text": "query",
                    "sex_id": "query",
                    "arrest_warrant_country_id": "query",
                    "page": "query",
                    "result_per_page": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.notices_v1_red_notice_id_get_endpoint = _Endpoint(
            settings={
                "response_type": (RedNoticeDetail,),
                "auth": [],
                "endpoint_path": "/notices/v1/red/{noticeID}",
                "operation_id": "notices_v1_red_notice_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "notice_id",
                ],
                "required": [
                    "notice_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "notice_id": (str,),
                },
                "attribute_map": {
                    "notice_id": "noticeID",
                },
                "location_map": {
                    "notice_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.notices_v1_red_notice_id_images_get_endpoint = _Endpoint(
            settings={
                "response_type": (RedNoticeDetailImages,),
                "auth": [],
                "endpoint_path": "/notices/v1/red/{noticeID}/images",
                "operation_id": "notices_v1_red_notice_id_images_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "notice_id",
                ],
                "required": [
                    "notice_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "notice_id": (str,),
                },
                "attribute_map": {
                    "notice_id": "noticeID",
                },
                "location_map": {
                    "notice_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def notices_v1_red_get(self, **kwargs):
        """Get Red Notices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.notices_v1_red_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            forename (str): First name. [optional]
            name (str): Last name. [optional]
            nationality (str): Two digit country code. [optional]
            age_max (int): maximum age. [optional]
            age_min (int): minimum age. [optional]
            free_text (str): Free text query. [optional]
            sex_id (str): Free text query. [optional]
            arrest_warrant_country_id (str): Two digit country code. [optional]
            page (int): pagination - starts with 1. [optional]
            result_per_page (int): resultPerPage. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RedNotices
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.notices_v1_red_get_endpoint.call_with_http_info(**kwargs)

    def notices_v1_red_notice_id_get(self, notice_id, **kwargs):
        """Get Red Notice Details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.notices_v1_red_notice_id_get(notice_id, async_req=True)
        >>> result = thread.get()

        Args:
            notice_id (str): Notice ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RedNoticeDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["notice_id"] = notice_id
        return self.notices_v1_red_notice_id_get_endpoint.call_with_http_info(**kwargs)

    def notices_v1_red_notice_id_images_get(self, notice_id, **kwargs):
        """Get Red Notice Images  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.notices_v1_red_notice_id_images_get(notice_id, async_req=True)
        >>> result = thread.get()

        Args:
            notice_id (str): Notice ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RedNoticeDetailImages
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["notice_id"] = notice_id
        return self.notices_v1_red_notice_id_images_get_endpoint.call_with_http_info(
            **kwargs
        )
