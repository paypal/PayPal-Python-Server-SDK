# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper


class VaultVenmoExperienceContext(object):

    """Implementation of the 'Vault Venmo Experience Context' model.

    Customizes the Vault creation flow experience for your customers.

    Attributes:
        brand_name (str): The label that overrides the business name in the
            PayPal account on the PayPal site. The pattern is defined by an
            external party and supports Unicode.
        shipping_preference (str): The shipping preference. This only applies
            to PayPal payment source.
        vault_instruction (str): Vault Instruction on action to be performed
            after a successful payer approval.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand_name": 'brand_name',
        "shipping_preference": 'shipping_preference',
        "vault_instruction": 'vault_instruction'
    }

    _optionals = [
        'brand_name',
        'shipping_preference',
        'vault_instruction',
    ]

    def __init__(self,
                 brand_name=APIHelper.SKIP,
                 shipping_preference='GET_FROM_FILE',
                 vault_instruction='ON_CREATE_PAYMENT_TOKENS'):
        """Constructor for the VaultVenmoExperienceContext class"""

        # Initialize members of the class
        if brand_name is not APIHelper.SKIP:
            self.brand_name = brand_name 
        self.shipping_preference = shipping_preference 
        self.vault_instruction = vault_instruction 

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
        brand_name = dictionary.get("brand_name") if dictionary.get("brand_name") else APIHelper.SKIP
        shipping_preference = dictionary.get("shipping_preference") if dictionary.get("shipping_preference") else 'GET_FROM_FILE'
        vault_instruction = dictionary.get("vault_instruction") if dictionary.get("vault_instruction") else 'ON_CREATE_PAYMENT_TOKENS'
        # Return an object of this model
        return cls(brand_name,
                   shipping_preference,
                   vault_instruction)
