# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class ThreeDSecureCardAuthenticationResponse(object):

    """Implementation of the 'Three-D Secure Card Authentication Response' model.

    Results of 3D Secure Authentication.

    Attributes:
        authentication_status (PaResStatus): Transactions status result
            identifier. The outcome of the issuer's authentication.
        enrollment_status (EnrollmentStatus): Status of Authentication
            eligibility.
        authentication_id (str): The externally received 3ds authentication
            id, to be returned in card detokenization response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authentication_status": 'authentication_status',
        "enrollment_status": 'enrollment_status',
        "authentication_id": 'authentication_id'
    }

    _optionals = [
        'authentication_status',
        'enrollment_status',
        'authentication_id',
    ]

    def __init__(self,
                 authentication_status=APIHelper.SKIP,
                 enrollment_status=APIHelper.SKIP,
                 authentication_id=APIHelper.SKIP):
        """Constructor for the ThreeDSecureCardAuthenticationResponse class"""

        # Initialize members of the class
        if authentication_status is not APIHelper.SKIP:
            self.authentication_status = authentication_status 
        if enrollment_status is not APIHelper.SKIP:
            self.enrollment_status = enrollment_status 
        if authentication_id is not APIHelper.SKIP:
            self.authentication_id = authentication_id 

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
        authentication_status = dictionary.get("authentication_status") if dictionary.get("authentication_status") else APIHelper.SKIP
        enrollment_status = dictionary.get("enrollment_status") if dictionary.get("enrollment_status") else APIHelper.SKIP
        authentication_id = dictionary.get("authentication_id") if dictionary.get("authentication_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(authentication_status,
                   enrollment_status,
                   authentication_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'authentication_status={(self.authentication_status if hasattr(self, "authentication_status") else None)!r}, '
                f'enrollment_status={(self.enrollment_status if hasattr(self, "enrollment_status") else None)!r}, '
                f'authentication_id={(self.authentication_id if hasattr(self, "authentication_id") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'authentication_status={(self.authentication_status if hasattr(self, "authentication_status") else None)!s}, '
                f'enrollment_status={(self.enrollment_status if hasattr(self, "enrollment_status") else None)!s}, '
                f'authentication_id={(self.authentication_id if hasattr(self, "authentication_id") else None)!s})')
