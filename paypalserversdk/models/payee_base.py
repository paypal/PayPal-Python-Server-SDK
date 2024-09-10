# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class PayeeBase(object):

    """Implementation of the 'Payee Base' model.

    The details for the merchant who receives the funds and fulfills the
    order. The merchant is also known as the payee.

    Attributes:
        email_address (str): The internationalized email
            address.<blockquote><strong>Note:</strong> Up to 64 characters are
            allowed before and 255 characters are allowed after the
            <code>@</code> sign. However, the generally accepted maximum
            length for an email address is 254 characters. The pattern
            verifies that an unquoted <code>@</code> sign
            exists.</blockquote>
        merchant_id (str): The account identifier for a PayPal account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address": 'email_address',
        "merchant_id": 'merchant_id'
    }

    _optionals = [
        'email_address',
        'merchant_id',
    ]

    def __init__(self,
                 email_address=APIHelper.SKIP,
                 merchant_id=APIHelper.SKIP):
        """Constructor for the PayeeBase class"""

        # Initialize members of the class
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if merchant_id is not APIHelper.SKIP:
            self.merchant_id = merchant_id 

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
        email_address = dictionary.get("email_address") if dictionary.get("email_address") else APIHelper.SKIP
        merchant_id = dictionary.get("merchant_id") if dictionary.get("merchant_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(email_address,
                   merchant_id)