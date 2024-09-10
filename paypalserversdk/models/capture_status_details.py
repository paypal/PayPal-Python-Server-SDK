# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class CaptureStatusDetails(object):

    """Implementation of the 'Capture Status Details' model.

    The details of the captured payment status.

    Attributes:
        reason (CaptureIncompleteReason): The reason why the captured payment
            status is `PENDING` or `DENIED`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason'
    }

    _optionals = [
        'reason',
    ]

    def __init__(self,
                 reason=APIHelper.SKIP):
        """Constructor for the CaptureStatusDetails class"""

        # Initialize members of the class
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(reason)