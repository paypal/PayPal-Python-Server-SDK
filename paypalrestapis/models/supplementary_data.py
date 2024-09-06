# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.card_supplementary_data import CardSupplementaryData


class SupplementaryData(object):

    """Implementation of the 'Supplementary Data' model.

    Supplementary data about a payment. This object passes information that
    can be used to improve risk assessments and processing costs, for example,
    by providing Level 2 and Level 3 payment data.

    Attributes:
        card (CardSupplementaryData): Merchants and partners can add Level 2
            and 3 data to payments to reduce risk and payment processing
            costs. For more information about processing payments, see <a
            href="https://developer.paypal.com/docs/checkout/advanced/processin
            g/">checkout</a> or <a
            href="https://developer.paypal.com/docs/multiparty/checkout/advance
            d/processing/">multiparty checkout</a>.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card": 'card'
    }

    _optionals = [
        'card',
    ]

    def __init__(self,
                 card=APIHelper.SKIP):
        """Constructor for the SupplementaryData class"""

        # Initialize members of the class
        if card is not APIHelper.SKIP:
            self.card = card 

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
        card = CardSupplementaryData.from_dictionary(dictionary.get('card')) if 'card' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card)
