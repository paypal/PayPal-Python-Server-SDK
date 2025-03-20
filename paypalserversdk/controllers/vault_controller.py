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
from apimatic_core.authentication.multiple.single_auth import Single
from paypalserversdk.models.payment_token_response import PaymentTokenResponse
from paypalserversdk.models.customer_vault_payment_tokens_response import CustomerVaultPaymentTokensResponse
from paypalserversdk.models.setup_token_response import SetupTokenResponse
from paypalserversdk.exceptions.error_exception import ErrorException


class VaultController(BaseController):

    """A Controller to access Endpoints in the paypalserversdk API."""
    def __init__(self, config):
        super(VaultController, self).__init__(config)

    def create_payment_token(self,
                             options=dict()):
        """Does a POST request to /v3/vault/payment-tokens.

        Creates a Payment Token from the given payment source and adds it to
        the Vault of the associated customer.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    body -- PaymentTokenRequest -- Payment Token creation with
                        a financial instrument and an optional customer_id.
                    paypal_request_id -- str -- The server stores keys for 3
                        hours.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Idempotent response for a successful creation of payment token.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/payment-tokens')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentTokenResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'Request contains reference to resources that do not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()

    def list_customer_payment_tokens(self,
                                     options=dict()):
        """Does a GET request to /v3/vault/payment-tokens.

        Returns all payment tokens for a customer.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    customer_id -- str -- A unique identifier representing a
                        specific customer in merchant's/partner's system or
                        records.
                    page_size -- int -- A non-negative, non-zero integer
                        indicating the maximum number of results to return at
                        one time.
                    page -- int -- A non-negative, non-zero integer
                        representing the page of the results.
                    total_required -- bool -- A boolean indicating total
                        number of items (total_items) and pages (total_pages)
                        are expected to be returned in the response.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Successful execution.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/payment-tokens')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('customer_id')
                         .value(options.get('customer_id', None)))
            .query_param(Parameter()
                         .key('page_size')
                         .value(options.get('page_size', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('total_required')
                         .value(options.get('total_required', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerVaultPaymentTokensResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()

    def get_payment_token(self,
                          id):
        """Does a GET request to /v3/vault/payment-tokens/{id}.

        Returns a readable representation of vaulted payment source associated
        with the payment token id.

        Args:
            id (str): ID of the payment token.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Successful execution.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/payment-tokens/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentTokenResponse.from_dictionary)
            .is_api_response(True)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()

    def delete_payment_token(self,
                             id):
        """Does a DELETE request to /v3/vault/payment-tokens/{id}.

        Delete the payment token associated with the payment token id.

        Args:
            id (str): ID of the payment token.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The
                server has successfully executed the method, but there is no
                entity body to return.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/payment-tokens/{id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()

    def create_setup_token(self,
                           options=dict()):
        """Does a POST request to /v3/vault/setup-tokens.

        Creates a Setup Token from the given payment source and adds it to the
        Vault of the associated customer.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    body -- SetupTokenRequest -- Setup Token creation with a
                        instrument type optional financial instrument details
                        and customer_id.
                    paypal_request_id -- str -- The server stores keys for 3
                        hours.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Idempotent response for a successful creation of setup token.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/setup-tokens')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SetupTokenResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()

    def get_setup_token(self,
                        id):
        """Does a GET request to /v3/vault/setup-tokens/{id}.

        Returns a readable representation of temporarily vaulted payment
        source associated with the setup token id.

        Args:
            id (str): ID of the setup token.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Found
                requested setup-token, returned a payment method associated
                with the token.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v3/vault/setup-tokens/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SetupTokenResponse.from_dictionary)
            .is_api_response(True)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
        ).execute()
