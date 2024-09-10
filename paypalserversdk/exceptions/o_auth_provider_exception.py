# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from paypalserversdk.api_helper import APIHelper
import paypalserversdk.exceptions.api_exception


class OAuthProviderException(paypalserversdk.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the OAuthProviderException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(OAuthProviderException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.error = dictionary.get("error") if dictionary.get("error") else None
        self.error_description = dictionary.get("error_description") if dictionary.get("error_description") else None
        self.error_uri = dictionary.get("error_uri") if dictionary.get("error_uri") else None
