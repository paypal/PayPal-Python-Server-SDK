# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.related_identifiers import RelatedIdentifiers


class PaymentSupplementaryData(object):

    """Implementation of the 'Payment Supplementary Data' model.

    The supplementary data.

    Attributes:
        related_ids (RelatedIdentifiers): Identifiers related to a specific
            resource.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "related_ids": 'related_ids'
    }

    _optionals = [
        'related_ids',
    ]

    def __init__(self,
                 related_ids=APIHelper.SKIP):
        """Constructor for the PaymentSupplementaryData class"""

        # Initialize members of the class
        if related_ids is not APIHelper.SKIP:
            self.related_ids = related_ids 

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
        related_ids = RelatedIdentifiers.from_dictionary(dictionary.get('related_ids')) if 'related_ids' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(related_ids)
