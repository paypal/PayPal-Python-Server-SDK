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
from paypalserversdk.models.payment_authorization import PaymentAuthorization
from paypalserversdk.models.captured_payment import CapturedPayment
from paypalserversdk.models.refund import Refund
from paypalserversdk.exceptions.error_exception import ErrorException
from paypalserversdk.exceptions.api_exception import ApiException


class PaymentsController(BaseController):

    """A Controller to access Endpoints in the paypalserversdk API."""
    def __init__(self, config):
        super(PaymentsController, self).__init__(config)

    def get_authorized_payment(self,
                               options=dict()):
        """Does a GET request to /v2/payments/authorizations/{authorization_id}.

        Shows details for an authorized payment, by ID.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    authorization_id -- str -- The ID of the authorized
                        payment for which to show details.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows authorization details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/authorizations/{authorization_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('authorization_id')
                            .value(options.get('authorization_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentAuthorization.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def capture_authorized_payment(self,
                                   options=dict()):
        """Does a POST request to /v2/payments/authorizations/{authorization_id}/capture.

        Captures an authorized payment, by ID.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    authorization_id -- str -- The PayPal-generated ID for the
                        authorized payment to capture.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.
                    paypal_request_id -- str -- The server stores keys for 45
                        days.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value is:
                        return=minimal. The server returns a minimal response
                        to optimize communication between the API caller and
                        the server. A minimal response includes the id, status
                        and HATEOAS links. return=representation. The server
                        returns a complete resource representation, including
                        the current state of the resource.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.
                    body -- CaptureRequest -- The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows captured payment details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/authorizations/{authorization_id}/capture')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('authorization_id')
                            .value(options.get('authorization_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CapturedPayment.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'The request failed because it is not well-formed or is syntactically incorrect or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The request failed because the caller has insufficient permissions.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('409', 'The server has detected a conflict while processing this request.', ErrorException)
            .local_error('422', 'The request failed because it is semantically incorrect or failed business validation.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def reauthorize_payment(self,
                            options=dict()):
        """Does a POST request to /v2/payments/authorizations/{authorization_id}/reauthorize.

        Reauthorizes an authorized PayPal account payment, by ID. To ensure
        that funds are still available, reauthorize a payment after its
        initial three-day honor period expires. Within the 29-day
        authorization period, you can issue multiple re-authorizations after
        the honor period expires. If 30 days have transpired since the date of
        the original authorization, you must create an authorized payment
        instead of reauthorizing the original authorized payment. A
        reauthorized payment itself has a new honor period of three days. You
        can reauthorize an authorized payment from 4 to 29 days after the
        3-day honor period. The allowed amount depends on context and
        geography, for example in US it is up to 115% of the original
        authorized amount, not to exceed an increase of $75 USD. Supports only
        the `amount` request parameter. Note: This request is currently not
        supported for Partner use cases.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    authorization_id -- str -- The PayPal-generated ID for the
                        authorized payment to reauthorize.
                    paypal_request_id -- str -- The server stores keys for 45
                        days.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value is:
                        return=minimal. The server returns a minimal response
                        to optimize communication between the API caller and
                        the server. A minimal response includes the id, status
                        and HATEOAS links. return=representation. The server
                        returns a complete resource representation, including
                        the current state of the resource.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.
                    body -- ReauthorizeRequest -- The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows the reauthorized payment details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/authorizations/{authorization_id}/reauthorize')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('authorization_id')
                            .value(options.get('authorization_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentAuthorization.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'The request failed because it is not well-formed or is syntactically incorrect or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('422', 'The request failed because it either is semantically incorrect or failed business validation.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def void_payment(self,
                     options=dict()):
        """Does a POST request to /v2/payments/authorizations/{authorization_id}/void.

        Voids, or cancels, an authorized payment, by ID. You cannot void an
        authorized payment that has been fully captured.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    authorization_id -- str -- The PayPal-generated ID for the
                        authorized payment to void.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.
                    paypal_request_id -- str -- The server stores keys for 45
                        days.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value is:
                        return=minimal. The server returns a minimal response
                        to optimize communication between the API caller and
                        the server. A minimal response includes the id, status
                        and HATEOAS links. return=representation. The server
                        returns a complete resource representation, including
                        the current state of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows authorization details. This
                response is returned when the Prefer header is set to
                return=representation.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/authorizations/{authorization_id}/void')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('authorization_id')
                            .value(options.get('authorization_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentAuthorization.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The request failed because the caller has insufficient permissions.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('409', 'The request failed because a previous call for the given resource is in progress.', ErrorException)
            .local_error('422', 'The request failed because it either is semantically incorrect or failed business validation.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def get_captured_payment(self,
                             options=dict()):
        """Does a GET request to /v2/payments/captures/{capture_id}.

        Shows details for a captured payment, by ID.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    capture_id -- str -- The PayPal-generated ID for the
                        captured payment for which to show details.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows captured payment details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/captures/{capture_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('capture_id')
                            .value(options.get('capture_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CapturedPayment.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The request failed because the caller has insufficient permissions.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def refund_captured_payment(self,
                                options=dict()):
        """Does a POST request to /v2/payments/captures/{capture_id}/refund.

        Refunds a captured payment, by ID. For a full refund, include an empty
        payload in the JSON request body. For a partial refund, include an
        amount object in the JSON request body.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    capture_id -- str -- The PayPal-generated ID for the
                        captured payment to refund.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.
                    paypal_request_id -- str -- The server stores keys for 45
                        days.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value is:
                        return=minimal. The server returns a minimal response
                        to optimize communication between the API caller and
                        the server. A minimal response includes the id, status
                        and HATEOAS links. return=representation. The server
                        returns a complete resource representation, including
                        the current state of the resource.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.
                    body -- RefundRequest -- The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows refund details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/captures/{capture_id}/refund')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('capture_id')
                            .value(options.get('capture_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('PayPal-Request-Id')
                          .value(options.get('paypal_request_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Refund.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'The request failed because it is not well-formed or is syntactically incorrect or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The request failed because the caller has insufficient permissions.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('409', 'The request failed because a previous call for the given resource is in progress.', ErrorException)
            .local_error('422', 'The request failed because it either is semantically incorrect or failed business validation.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def get_refund(self,
                   options=dict()):
        """Does a GET request to /v2/payments/refunds/{refund_id}.

        Shows details for a refund, by ID.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    refund_id -- str -- The PayPal-generated ID for the refund
                        for which to show details.
                    paypal_mock_response -- str -- PayPal's REST API uses a
                        request header to invoke negative testing in the
                        sandbox. This header configures the sandbox into a
                        negative testing state for transactions that include
                        the merchant.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see
                        [PayPal-Auth-Assertion](/docs/api/reference/api-request
                        s/#paypal-auth-assertion). Note:For three party
                        transactions in which a partner is managing the API
                        calls on behalf of a merchant, the partner must
                        identify the merchant using either a
                        PayPal-Auth-Assertion header or an access token with
                        target_subject.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP 200 OK status code and a
                JSON response body that shows refund details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/payments/refunds/{refund_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('refund_id')
                            .value(options.get('refund_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('PayPal-Mock-Response')
                          .value(options.get('paypal_mock_response', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Refund.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The request failed because the caller has insufficient permissions.', ErrorException)
            .local_error('404', 'The request failed because the resource does not exist.', ErrorException)
            .local_error('500', 'The request failed because an internal server error occurred.', ApiException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()
