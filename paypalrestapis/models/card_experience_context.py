# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper


class CardExperienceContext(object):

    """Implementation of the 'Card Experience Context' model.

    Customizes the payer experience during the 3DS Approval for payment.

    Attributes:
        return_url (str): Describes the URL.
        cancel_url (str): Describes the URL.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "return_url": 'return_url',
        "cancel_url": 'cancel_url'
    }

    _optionals = [
        'return_url',
        'cancel_url',
    ]

    def __init__(self,
                 return_url=APIHelper.SKIP,
                 cancel_url=APIHelper.SKIP):
        """Constructor for the CardExperienceContext class"""

        # Initialize members of the class
        if return_url is not APIHelper.SKIP:
            self.return_url = return_url 
        if cancel_url is not APIHelper.SKIP:
            self.cancel_url = cancel_url 

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
        return_url = dictionary.get("return_url") if dictionary.get("return_url") else APIHelper.SKIP
        cancel_url = dictionary.get("cancel_url") if dictionary.get("cancel_url") else APIHelper.SKIP
        # Return an object of this model
        return cls(return_url,
                   cancel_url)
