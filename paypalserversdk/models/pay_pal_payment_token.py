# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.address import Address
from paypalserversdk.models.name import Name
from paypalserversdk.models.phone import Phone
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails


class PayPalPaymentToken(object):

    """Implementation of the 'PayPal Payment Token' model.

    TODO: type model description here.

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
        email_address (str): The internationalized email
            address.<blockquote><strong>Note:</strong> Up to 64 characters are
            allowed before and 255 characters are allowed after the
            <code>@</code> sign. However, the generally accepted maximum
            length for an email address is 254 characters. The pattern
            verifies that an unquoted <code>@</code> sign
            exists.</blockquote>
        payer_id (str): The account identifier for a PayPal account.
        name (Name): The name of the party.
        phone (PhoneWithType): The phone information.
        address (Address): The portable international postal address. Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).
        account_id (str): The account identifier for a PayPal account.
        phone_number (Phone): The phone number, in its canonical international
            [E.164 numbering plan
            format](https://www.itu.int/rec/T-REC-E.164/en).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "shipping": 'shipping',
        "permit_multiple_payment_tokens": 'permit_multiple_payment_tokens',
        "usage_type": 'usage_type',
        "customer_type": 'customer_type',
        "email_address": 'email_address',
        "payer_id": 'payer_id',
        "name": 'name',
        "phone": 'phone',
        "address": 'address',
        "account_id": 'account_id',
        "phone_number": 'phone_number'
    }

    _optionals = [
        'description',
        'shipping',
        'permit_multiple_payment_tokens',
        'usage_type',
        'customer_type',
        'email_address',
        'payer_id',
        'name',
        'phone',
        'address',
        'account_id',
        'phone_number',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 shipping=APIHelper.SKIP,
                 permit_multiple_payment_tokens=False,
                 usage_type=APIHelper.SKIP,
                 customer_type=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP):
        """Constructor for the PayPalPaymentToken class"""

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
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if address is not APIHelper.SKIP:
            self.address = address 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 

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
        email_address = dictionary.get("email_address") if dictionary.get("email_address") else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if dictionary.get("payer_id") else APIHelper.SKIP
        name = Name.from_dictionary(dictionary.get('name')) if 'name' in dictionary.keys() else APIHelper.SKIP
        phone = PhoneWithType.from_dictionary(dictionary.get('phone')) if 'phone' in dictionary.keys() else APIHelper.SKIP
        address = Address.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("account_id") if dictionary.get("account_id") else APIHelper.SKIP
        phone_number = Phone.from_dictionary(dictionary.get('phone_number')) if 'phone_number' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   shipping,
                   permit_multiple_payment_tokens,
                   usage_type,
                   customer_type,
                   email_address,
                   payer_id,
                   name,
                   phone,
                   address,
                   account_id,
                   phone_number)
