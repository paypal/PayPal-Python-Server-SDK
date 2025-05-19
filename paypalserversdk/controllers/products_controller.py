from paypalserversdk.api_helper import APIHelper
from paypalserversdk.configuration import Server
from paypalserversdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from paypalserversdk.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from paypalserversdk.exceptions.error_exception import ErrorException


class ProductsController(BaseController):
    """A Controller to access Endpoints in the paypalserversdk API."""

    def __init__(self, config):
        super(ProductsController, self).__init__(config)

    def create_product(self, options=dict()):
        """Creates a product by making a POST request to /v1/catalogs/products.

        The product creation API allows merchants and partners to add a new
        product to their PayPal catalog. A product can represent a service,
        software, or any other item that can be sold through PayPal.

        Args:
            options (dict, optional): Key-value pairs for any of the parameters 
                to this API Endpoint. All parameters to the endpoint are supplied 
                through the dictionary with their names being the key and their 
                desired values being the value. A list of parameters that can be 
                used are:

                body -- dict -- The request body parameter containing the product 
                    details. This includes fields such as:
                    - "name": The name of the product.
                    - "description": A short description of the product.
                    - "type": The product type (e.g., "SERVICE").
                    - "category": The product category (e.g., "SOFTWARE").

        Returns:
            ApiResponse: An object with the response value as well as other useful 
                information such as status codes and headers. A successful response 
                will contain details of the newly created product including the product ID.

        Raises:
            ErrorException: When an error occurs while making the API request. This 
                exception includes the HTTP response code, an error message, and the 
                HTTP body received from the server.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT
                                   ).path('/v1/catalogs/products').http_method(HttpMethodEnum.POST).header_param(
                                       Parameter().key('Content-Type').value('application/json')
                                   ).body_param(Parameter().value(options.get('body', None))).auth(Single('Oauth2'))
        ).response(
            ResponseHandler().deserializer(APIHelper.json_deserialize).is_api_response(True).local_error(
                '400', 'Invalid product data.', ErrorException
            ).local_error('401', 'Unauthorized.',
                          ErrorException).local_error('default', 'Error creating product.', ErrorException)
        ).execute()
