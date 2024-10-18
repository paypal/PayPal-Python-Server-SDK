# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from paypalserversdk.api_helper import APIHelper
from paypalserversdk.configuration import Server
from paypalserversdk.http.api_response import ApiResponse
from paypalserversdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from paypalserversdk.http.http_method_enum import HttpMethodEnum
from paypalserversdk.models.o_auth_token import OAuthToken
from paypalserversdk.exceptions.o_auth_provider_exception import OAuthProviderException


class OAuthAuthorizationController(BaseController):

    """A Controller to access Endpoints in the paypalserversdk API."""
    def __init__(self, config):
        super(OAuthAuthorizationController, self).__init__(config)

    def request_token(self,
                      options=dict(),
                      _optional_form_parameters=None):
        """Does a POST request to /v1/oauth2/token.

        Create a new OAuth 2 token.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    authorization -- str -- Authorization header in Basic auth
                        format
                    scope -- str -- Requested scopes as a space-delimited list.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/oauth2/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('client_credentials'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(options.get('authorization', None)))
            .form_param(Parameter()
                        .key('scope')
                        .value(options.get('scope', None)))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()
