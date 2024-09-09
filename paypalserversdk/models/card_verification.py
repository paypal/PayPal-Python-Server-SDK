# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class CardVerification(object):

    """Implementation of the 'Card Verification' model.

    The API caller can opt in to verify the card through PayPal offered
    verification services (e.g. Smart Dollar Auth, 3DS).

    Attributes:
        method (CardVerificationMethod): The method used for card
            verification.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "method": 'method'
    }

    _optionals = [
        'method',
    ]

    def __init__(self,
                 method='SCA_WHEN_REQUIRED'):
        """Constructor for the CardVerification class"""

        # Initialize members of the class
        self.method = method 

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
        method = dictionary.get("method") if dictionary.get("method") else 'SCA_WHEN_REQUIRED'
        # Return an object of this model
        return cls(method)