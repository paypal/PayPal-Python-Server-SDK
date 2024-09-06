# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails


class VaultedDigitalWallet(object):

    """Implementation of the 'Vaulted Digital Wallet' model.

    Resource consolidating common request and response attributes for vaulting
    a Digital Wallet.

    Attributes:
        description (str): The description displayed to the consumer on the
            approval flow for a digital wallet, as well as on the merchant
            view of the payment token management experience. exp: PayPal.com.
        shipping (VaultedDigitalWalletShippingDetails): The shipping details.
        permit_multiple_payment_tokens (bool): Create multiple payment tokens
            for the same payer, merchant/platform combination. Use this when
            the customer has not logged in at merchant/platform. The payment
            token thus generated, can then also be used to create the customer
            account at merchant/platform. Use this also when multiple payment
            tokens are required for the same payer, different customer at
            merchant/platform. This helps to identify customers distinctly
            even though they may share the same PayPal account. This only
            applies to PayPal payment source.
        usage_type (str): The usage type associated with a digital wallet
            payment token.
        customer_type (str): The customer type associated with a digital
            wallet payment token. This is to indicate whether the customer
            acting on the merchant / platform is either a business or a
            consumer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "shipping": 'shipping',
        "permit_multiple_payment_tokens": 'permit_multiple_payment_tokens',
        "usage_type": 'usage_type',
        "customer_type": 'customer_type'
    }

    _optionals = [
        'description',
        'shipping',
        'permit_multiple_payment_tokens',
        'usage_type',
        'customer_type',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 shipping=APIHelper.SKIP,
                 permit_multiple_payment_tokens=False,
                 usage_type=APIHelper.SKIP,
                 customer_type=APIHelper.SKIP):
        """Constructor for the VaultedDigitalWallet class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if shipping is not APIHelper.SKIP:
            self.shipping = shipping 
        self.permit_multiple_payment_tokens = permit_multiple_payment_tokens 
        if usage_type is not APIHelper.SKIP:
            self.usage_type = usage_type 
        if customer_type is not APIHelper.SKIP:
            self.customer_type = customer_type 

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
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        shipping = VaultedDigitalWalletShippingDetails.from_dictionary(dictionary.get('shipping')) if 'shipping' in dictionary.keys() else APIHelper.SKIP
        permit_multiple_payment_tokens = dictionary.get("permit_multiple_payment_tokens") if dictionary.get("permit_multiple_payment_tokens") else False
        usage_type = dictionary.get("usage_type") if dictionary.get("usage_type") else APIHelper.SKIP
        customer_type = dictionary.get("customer_type") if dictionary.get("customer_type") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   shipping,
                   permit_multiple_payment_tokens,
                   usage_type,
                   customer_type)
