# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BlikLevel0PaymentObject(object):

    """Implementation of the 'BLIK Level_0 Payment Object' model.

    Information used to pay using BLIK level_0 flow.

    Attributes:
        auth_code (str): The 6-digit code used to authenticate a consumer
            within BLIK.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth_code": 'auth_code'
    }

    def __init__(self,
                 auth_code=None):
        """Constructor for the BlikLevel0PaymentObject class"""

        # Initialize members of the class
        self.auth_code = auth_code 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        auth_code = dictionary.get("auth_code") if dictionary.get("auth_code") else None
        # Return an object of this model
        return cls(auth_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'auth_code={self.auth_code!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'auth_code={self.auth_code!s})')
