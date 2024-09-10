# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.authorization_status_details import AuthorizationStatusDetails


class AuthorizationStatusWithDetails(object):

    """Implementation of the 'Authorization Status With Details' model.

    The status fields and status details for an authorized payment.

    Attributes:
        status (AuthorizationStatus): The status for the authorized payment.
        status_details (AuthorizationStatusDetails): The details of the
            authorized payment status.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "status_details": 'status_details'
    }

    _optionals = [
        'status',
        'status_details',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 status_details=APIHelper.SKIP):
        """Constructor for the AuthorizationStatusWithDetails class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_details is not APIHelper.SKIP:
            self.status_details = status_details 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_details = AuthorizationStatusDetails.from_dictionary(dictionary.get('status_details')) if 'status_details' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   status_details)
