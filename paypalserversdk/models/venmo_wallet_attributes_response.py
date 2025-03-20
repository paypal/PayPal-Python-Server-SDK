# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.vault_response import VaultResponse


class VenmoWalletAttributesResponse(object):

    """Implementation of the 'Venmo Wallet Attributes Response' model.

    Additional attributes associated with the use of a Venmo Wallet.

    Attributes:
        vault (VaultResponse): The details about a saved payment source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault": 'vault'
    }

    _optionals = [
        'vault',
    ]

    def __init__(self,
                 vault=APIHelper.SKIP):
        """Constructor for the VenmoWalletAttributesResponse class"""

        # Initialize members of the class
        if vault is not APIHelper.SKIP:
            self.vault = vault 

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
        vault = VaultResponse.from_dictionary(dictionary.get('vault')) if 'vault' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(vault)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'vault={(self.vault if hasattr(self, "vault") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'vault={(self.vault if hasattr(self, "vault") else None)!s})')
