# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.venmo_wallet_customer_information import VenmoWalletCustomerInformation
from paypalserversdk.models.venmo_wallet_vault_attributes import VenmoWalletVaultAttributes


class VenmoWalletAdditionalAttributes(object):

    """Implementation of the 'Venmo Wallet Additional Attributes' model.

    Additional attributes associated with the use of this Venmo Wallet.

    Attributes:
        customer (VenmoWalletCustomerInformation): The details about a
            customer in PayPal's system of record.
        vault (VenmoWalletVaultAttributes): Resource consolidating common
            request and response attirbutes for vaulting Venmo Wallet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'customer',
        "vault": 'vault'
    }

    _optionals = [
        'customer',
        'vault',
    ]

    def __init__(self,
                 customer=APIHelper.SKIP,
                 vault=APIHelper.SKIP):
        """Constructor for the VenmoWalletAdditionalAttributes class"""

        # Initialize members of the class
        if customer is not APIHelper.SKIP:
            self.customer = customer 
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
        customer = VenmoWalletCustomerInformation.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        vault = VenmoWalletVaultAttributes.from_dictionary(dictionary.get('vault')) if 'vault' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(customer,
                   vault)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'customer={(self.customer if hasattr(self, "customer") else None)!r}, '
                f'vault={(self.vault if hasattr(self, "vault") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'customer={(self.customer if hasattr(self, "customer") else None)!s}, '
                f'vault={(self.vault if hasattr(self, "vault") else None)!s})')
