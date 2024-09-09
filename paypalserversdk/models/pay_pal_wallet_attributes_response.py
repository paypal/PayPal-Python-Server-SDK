# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.cobranded_card import CobrandedCard
from paypalserversdk.models.pay_pal_wallet_vault_response import PayPalWalletVaultResponse


class PayPalWalletAttributesResponse(object):

    """Implementation of the 'PayPal Wallet Attributes Response' model.

    Additional attributes associated with the use of a PayPal Wallet.

    Attributes:
        vault (PayPalWalletVaultResponse): The details about a saved PayPal
            Wallet payment source.
        cobranded_cards (List[CobrandedCard]): An array of merchant cobranded
            cards used by buyer to complete an order. This array will be
            present if a merchant has onboarded their cobranded card with
            PayPal and provided corresponding label(s).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault": 'vault',
        "cobranded_cards": 'cobranded_cards'
    }

    _optionals = [
        'vault',
        'cobranded_cards',
    ]

    def __init__(self,
                 vault=APIHelper.SKIP,
                 cobranded_cards=APIHelper.SKIP):
        """Constructor for the PayPalWalletAttributesResponse class"""

        # Initialize members of the class
        if vault is not APIHelper.SKIP:
            self.vault = vault 
        if cobranded_cards is not APIHelper.SKIP:
            self.cobranded_cards = cobranded_cards 

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
        vault = PayPalWalletVaultResponse.from_dictionary(dictionary.get('vault')) if 'vault' in dictionary.keys() else APIHelper.SKIP
        cobranded_cards = None
        if dictionary.get('cobranded_cards') is not None:
            cobranded_cards = [CobrandedCard.from_dictionary(x) for x in dictionary.get('cobranded_cards')]
        else:
            cobranded_cards = APIHelper.SKIP
        # Return an object of this model
        return cls(vault,
                   cobranded_cards)