# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.three_d_secure_authentication_response import ThreeDSecureAuthenticationResponse


class AuthenticationResponse(object):

    """Implementation of the 'Authentication Response' model.

    Results of Authentication such as 3D Secure.

    Attributes:
        liability_shift (LiabilityShiftIndicator): Liability shift indicator.
            The outcome of the issuer's authentication.
        three_d_secure (ThreeDSecureAuthenticationResponse): Results of 3D
            Secure Authentication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "liability_shift": 'liability_shift',
        "three_d_secure": 'three_d_secure'
    }

    _optionals = [
        'liability_shift',
        'three_d_secure',
    ]

    def __init__(self,
                 liability_shift=APIHelper.SKIP,
                 three_d_secure=APIHelper.SKIP):
        """Constructor for the AuthenticationResponse class"""

        # Initialize members of the class
        if liability_shift is not APIHelper.SKIP:
            self.liability_shift = liability_shift 
        if three_d_secure is not APIHelper.SKIP:
            self.three_d_secure = three_d_secure 

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
        liability_shift = dictionary.get("liability_shift") if dictionary.get("liability_shift") else APIHelper.SKIP
        three_d_secure = ThreeDSecureAuthenticationResponse.from_dictionary(dictionary.get('three_d_secure')) if 'three_d_secure' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(liability_shift,
                   three_d_secure)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'liability_shift={(self.liability_shift if hasattr(self, "liability_shift") else None)!r}, '
                f'three_d_secure={(self.three_d_secure if hasattr(self, "three_d_secure") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'liability_shift={(self.liability_shift if hasattr(self, "liability_shift") else None)!s}, '
                f'three_d_secure={(self.three_d_secure if hasattr(self, "three_d_secure") else None)!s})')
