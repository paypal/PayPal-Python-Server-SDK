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
from paypalserversdk.models.order_authorize_response import OrderAuthorizeResponse
from paypalserversdk.models.order import Order
from paypalserversdk.exceptions.error_exception import ErrorException


class OrdersController(BaseController):

    """A Controller to access Endpoints in the paypalserversdk API."""
    def __init__(self, config):
        super(OrdersController, self).__init__(config)

    def orders_authorize(self,
                         options=dict()):
        """Does a POST request to /v2/checkout/orders/{id}/authorize.

        Authorizes payment for an order. To successfully authorize payment for
        an order, the buyer must first approve the order or a valid
        payment_source must be provided in the request. A buyer can approve
        the order upon being redirected to the rel:approve URL that was
        returned in the HATEOAS links in the create order
        response.<blockquote><strong>Note:</strong> For error handling and
        troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/
        #authorize-order">Orders v2 errors</a>.</blockquote>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order for which to authorize.
                    paypal_request_id -- str -- The server stores keys for 6
                        hours. The API callers can request the times to up to
                        72 hours by speaking to their Account Manager.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value
                        is:<ul><li><code>return=minimal</code>. The server
                        returns a minimal response to optimize communication
                        between the API caller and the server. A minimal
                        response includes the <code>id</code>,
                        <code>status</code> and HATEOAS
                        links.</li><li><code>return=representation</code>. The
                        server returns a complete resource representation,
                        including the current state of the resource.</li></ul>
                    paypal_client_metadata_id -- str -- TODO: type description
                        here.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see <a
                        href="https://developer.paypal.com/api/rest/requests/#p
                        aypal-auth-assertion">PayPal-Auth-Assertion</a>.
                    body -- OrderAuthorizeRequest -- TODO: type description
                        here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful response to an idempotent request returns the HTTP
                `200 OK` status code with a JSON response body that shows
                authorized payment details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}/authorize')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
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
                          .key('PayPal-Client-Metadata-Id')
                          .value(options.get('paypal_client_metadata_id', None)))
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
            .deserialize_into(OrderAuthorizeResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The authorized payment failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_track_create(self,
                            options=dict()):
        """Does a POST request to /v2/checkout/orders/{id}/track.

        Adds tracking information for an Order.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order that the tracking
                        information is associated with.
                    body -- OrderTrackerRequest -- TODO: type description here.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see <a
                        href="https://developer.paypal.com/api/rest/requests/#p
                        aypal-auth-assertion">PayPal-Auth-Assertion</a>.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful response to an idempotent request returns the HTTP
                `200 OK` status code with a JSON response body that shows
                tracker details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}/track')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .header_param(Parameter()
                          .key('PayPal-Auth-Assertion')
                          .value(options.get('paypal_auth_assertion', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_create(self,
                      options=dict()):
        """Does a POST request to /v2/checkout/orders.

        Creates an order. Merchants and partners can add Level 2 and 3 data to
        payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">
        checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/pr
        ocessing/">multiparty checkout</a>.<blockquote><strong>Note:</strong>
        For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/
        #create-order">Orders v2 errors</a>.</blockquote>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    body -- OrderRequest -- TODO: type description here.
                    paypal_request_id -- str -- The server stores keys for 6
                        hours. The API callers can request the times to up to
                        72 hours by speaking to their Account Manager.
                    paypal_partner_attribution_id -- str -- TODO: type
                        description here.
                    paypal_client_metadata_id -- str -- TODO: type description
                        here.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value
                        is:<ul><li><code>return=minimal</code>. The server
                        returns a minimal response to optimize communication
                        between the API caller and the server. A minimal
                        response includes the <code>id</code>,
                        <code>status</code> and HATEOAS
                        links.</li><li><code>return=representation</code>. The
                        server returns a complete resource representation,
                        including the current state of the resource.</li></ul>

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful response to an idempotent request returns the HTTP
                `200 OK` status code with a JSON response body that shows
                order details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders')
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
                          .key('PayPal-Partner-Attribution-Id')
                          .value(options.get('paypal_partner_attribution_id', None)))
            .header_param(Parameter()
                          .key('PayPal-Client-Metadata-Id')
                          .value(options.get('paypal_client_metadata_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_patch(self,
                     options=dict()):
        """Does a PATCH request to /v2/checkout/orders/{id}.

        Updates an order with a `CREATED` or `APPROVED` status. You cannot
        update an order with the `COMPLETED` status.<br/><br/>To make an
        update, you must provide a `reference_id`. If you omit this value with
        an order that contains only one purchase unit, PayPal sets the value
        to `default` which enables you to use the path:
        <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\
        "</code>. Merchants and partners can add Level 2 and 3 data to
        payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">
        checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/pr
        ocessing/">multiparty checkout</a>.<blockquote><strong>Note:</strong>
        For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/
        #patch-order">Orders v2 errors</a>.</blockquote>Patchable attributes
        or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes<
        /th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td>
        </td></tr><tr><td><code>payer</code></td><td>replace,
        add</td><td>Using replace op for <code>payer</code> will replace the
        whole <code>payer</code> object with the value sent in
        request.</td></tr><tr><td><code>purchase_units</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></
        td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].description</co
        de></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</co
        de></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].sh
        ipping.name</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_add
        ress</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_num
        ber</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</
        code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</
        code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</cod
        e></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</c
        ode></td><td>replace,
        remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></
        td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</
        code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</cod
        e></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruc
        tion</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_un
        its[].payment_instruction.disbursement_mode</code></td><td>replace</td>
        <td>By default, <code>disbursement_mode</code> is
        <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_i
        nstruction.payee_receivable_fx_rate_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruc
        tion.platform_fees</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_d
        ata.airline</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_d
        ata.card</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>application_context.client_confi
        guration</code></td><td>replace, add</td><td></td></tr></tbody></table>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order to update.
                    body -- List[Patch] -- TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP `204 No Content` status
                code with an empty object in the JSON response body.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_capture(self,
                       options=dict()):
        """Does a POST request to /v2/checkout/orders/{id}/capture.

        Captures payment for an order. To successfully capture payment for an
        order, the buyer must first approve the order or a valid
        payment_source must be provided in the request. A buyer can approve
        the order upon being redirected to the rel:approve URL that was
        returned in the HATEOAS links in the create order
        response.<blockquote><strong>Note:</strong> For error handling and
        troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/
        #capture-order">Orders v2 errors</a>.</blockquote>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order for which to capture a
                        payment.
                    paypal_request_id -- str -- The server stores keys for 6
                        hours. The API callers can request the times to up to
                        72 hours by speaking to their Account Manager.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value
                        is:<ul><li><code>return=minimal</code>. The server
                        returns a minimal response to optimize communication
                        between the API caller and the server. A minimal
                        response includes the <code>id</code>,
                        <code>status</code> and HATEOAS
                        links.</li><li><code>return=representation</code>. The
                        server returns a complete resource representation,
                        including the current state of the resource.</li></ul>
                    paypal_client_metadata_id -- str -- TODO: type description
                        here.
                    paypal_auth_assertion -- str -- An API-caller-provided
                        JSON Web Token (JWT) assertion that identifies the
                        merchant. For details, see <a
                        href="https://developer.paypal.com/api/rest/requests/#p
                        aypal-auth-assertion">PayPal-Auth-Assertion</a>.
                    body -- OrderCaptureRequest -- TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful response to an idempotent request returns the HTTP
                `200 OK` status code with a JSON response body that shows
                captured payment details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}/capture')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
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
                          .key('PayPal-Client-Metadata-Id')
                          .value(options.get('paypal_client_metadata_id', None)))
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
            .deserialize_into(Order.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('403', 'The authorized payment failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_get(self,
                   options=dict()):
        """Does a GET request to /v2/checkout/orders/{id}.

        Shows details for an order, by ID.<blockquote><strong>Note:</strong>
        For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/
        #get-order">Orders v2 errors</a>.</blockquote>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order for which to show details.
                    fields -- str -- A comma-separated list of fields that
                        should be returned for the order. Valid filter field
                        is `payment_source`.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP `200 OK` status code and a
                JSON response body that shows order details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
                            .should_encode(True))
            .query_param(Parameter()
                         .key('fields')
                         .value(options.get('fields', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Authentication failed due to missing authorization header, or invalid authentication credentials.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_confirm(self,
                       options=dict()):
        """Does a POST request to /v2/checkout/orders/{id}/confirm-payment-source.

        Payer confirms their intent to pay for the the Order with the given
        payment source.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order for which the payer
                        confirms their intent to pay.
                    paypal_client_metadata_id -- str -- TODO: type description
                        here.
                    prefer -- str -- The preferred server response upon
                        successful completion of the request. Value
                        is:<ul><li><code>return=minimal</code>. The server
                        returns a minimal response to optimize communication
                        between the API caller and the server. A minimal
                        response includes the <code>id</code>,
                        <code>status</code> and HATEOAS
                        links.</li><li><code>return=representation</code>. The
                        server returns a complete resource representation,
                        including the current state of the resource.</li></ul>
                    body -- ConfirmOrderRequest -- TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request indicates that the payment source was added
                to the Order. A successful request returns the HTTP `200 OK`
                status code with a JSON response body that shows order details.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}/confirm-payment-source')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('PayPal-Client-Metadata-Id')
                          .value(options.get('paypal_client_metadata_id', None)))
            .header_param(Parameter()
                          .key('Prefer')
                          .value(options.get('prefer', None)))
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
            .deserialize_into(Order.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()

    def orders_trackers_patch(self,
                              options=dict()):
        """Does a PATCH request to /v2/checkout/orders/{id}/trackers/{tracker_id}.

        Updates or cancels the tracking information for a PayPal order, by ID.
        Updatable attributes or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes<
        /th></thead><tbody></tr><tr><td><code>items</code></td><td>replace</td>
        <td>Using replace op for <code>items</code> will replace the entire
        <code>items</code> object with the value sent in
        request.</td></tr><tr><td><code>notify_payer</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>status</code></td><td>replace</td><
        td>Only patching status to CANCELLED is currently
        supported.</td></tr></tbody></table>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- str -- The ID of the order that the tracking
                        information is associated with.
                    tracker_id -- str -- The order tracking ID.
                    body -- List[Patch] -- TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                successful request returns the HTTP `204 No Content` status
                code with an empty object in the JSON response body.

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v2/checkout/orders/{id}/trackers/{tracker_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('id')
                            .value(options.get('id', None))
                            .should_encode(True))
            .template_param(Parameter()
                            .key('tracker_id')
                            .value(options.get('tracker_id', None))
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(options.get('body', None)))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('Oauth2'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('400', 'Request is not well-formed, syntactically incorrect, or violates schema.', ErrorException)
            .local_error('403', 'Authorization failed due to insufficient permissions.', ErrorException)
            .local_error('404', 'The specified resource does not exist.', ErrorException)
            .local_error('422', 'The requested action could not be performed, semantically incorrect, or failed business validation.', ErrorException)
            .local_error('500', 'An internal server error has occurred.', ErrorException)
            .local_error('default', 'The error response.', ErrorException)
        ).execute()
