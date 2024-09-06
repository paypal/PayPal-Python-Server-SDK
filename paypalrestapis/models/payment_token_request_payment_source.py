# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.payment_token_request_card import PaymentTokenRequestCard
from paypalrestapis.models.vault_token_request import VaultTokenRequest


class PaymentTokenRequestPaymentSource(object):

    """Implementation of the 'Payment Token Request Payment Source' model.

    The payment method to vault with the instrument details.

    Attributes:
        card (PaymentTokenRequestCard): A Resource representing a request to
            vault a Card.
        token (VaultTokenRequest): The Tokenized Payment Source representing a
            Request to Vault a Token.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card": 'card',
        "token": 'token'
    }

    _optionals = [
        'card',
        'token',
    ]

    def __init__(self,
                 card=APIHelper.SKIP,
                 token=APIHelper.SKIP):
        """Constructor for the PaymentTokenRequestPaymentSource class"""

        # Initialize members of the class
        if card is not APIHelper.SKIP:
            self.card = card 
        if token is not APIHelper.SKIP:
            self.token = token 

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
        card = PaymentTokenRequestCard.from_dictionary(dictionary.get('card')) if 'card' in dictionary.keys() else APIHelper.SKIP
        token = VaultTokenRequest.from_dictionary(dictionary.get('token')) if 'token' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card,
                   token)
