from paypalserversdk.api_helper import APIHelper
from paypalserversdk.configuration import Server
from paypalserversdk.http.api_response import ApiResponse
from paypalserversdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from paypalserversdk.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from paypalserversdk.exceptions.error_exception import ErrorException


class PlansController(BaseController):
    """A Controller to manage subscription plans in the PayPal API."""

    def __init__(self, config):
        super(PlansController, self).__init__(config)

    def create_plan(self, options=dict()):
        """Creates a billing plan by making a POST request to /v1/billing/plans.

        The plan creation API allows merchants and partners to define a new 
        subscription billing plan, including pricing, frequency, and billing cycles.

        Args:
            options (dict, optional): Key-value pairs for any of the parameters 
                to this API Endpoint. All parameters to the endpoint are supplied 
                through the dictionary with their names being the key and their 
                desired values being the value. A list of parameters that can be 
                used are:

                body -- dict -- The request body parameter containing the plan 
                    details. This includes fields such as:
                    - "product_id": The ID of the product.
                    - "name": The name of the billing plan.
                    - "description": A description of the plan.
                    - "status": The initial status of the plan (e.g., "ACTIVE").
                    - "billing_cycles": An array of billing cycle objects.
                    - "payment_preferences": Payment preferences for the plan.
                    - "taxes": Tax information applicable to the plan.

        Returns:
            ApiResponse: An object with the response value as well as other useful 
                information such as status codes and headers. A successful response 
                will contain details of the newly created plan including the plan ID.

        Raises:
            ErrorException: When an error occurs while making the API request. This 
                exception includes the HTTP response code, an error message, and the 
                HTTP body received from the server.
        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT
                                   ).path('/v1/billing/plans').http_method(HttpMethodEnum.POST).header_param(
                                       Parameter().key('Content-Type').value('application/json')
                                   ).body_param(Parameter().value(options.get('body', None))).auth(Single('Oauth2'))
        ).response(
            ResponseHandler().deserializer(APIHelper.json_deserialize).is_api_response(True).local_error(
                '400', 'Invalid plan data.', ErrorException
            ).local_error('401', 'Unauthorized.',
                          ErrorException).local_error('default', 'Error creating plan.', ErrorException)
        ).execute()
