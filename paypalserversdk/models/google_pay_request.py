# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.assurance_details import AssuranceDetails
from paypalserversdk.models.google_pay_card_attributes import GooglePayCardAttributes
from paypalserversdk.models.google_pay_decrypted_token_data import GooglePayDecryptedTokenData
from paypalserversdk.models.google_pay_request_card import GooglePayRequestCard
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode


class GooglePayRequest(object):

    """Implementation of the 'Google Pay Request' model.

    Information needed to pay using Google Pay.

    Attributes:
        name (str): The full name representation like Mr J Smith.
        email_address (str): The internationalized email
            address.<blockquote><strong>Note:</strong> Up to 64 characters are
            allowed before and 255 characters are allowed after the
            <code>@</code> sign. However, the generally accepted maximum
            length for an email address is 254 characters. The pattern
            verifies that an unquoted <code>@</code> sign exists.</blockquote>
        phone_number (PhoneNumberWithCountryCode): The phone number in its
            canonical international [E.164 numbering plan
            format](https://www.itu.int/rec/T-REC-E.164/en).
        card (GooglePayRequestCard): The payment card used to fund a Google
            Pay payment. Can be a credit or debit card.
        decrypted_token (GooglePayDecryptedTokenData): Details shared by
            Google for the merchant to be shared with PayPal. This is required
            to process the transaction using the Google Pay payment method.
        assurance_details (AssuranceDetails): Information about cardholder
            possession validation and cardholder identification and
            verifications (ID&V).
        attributes (GooglePayCardAttributes): Additional attributes associated
            with the use of this card.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email_address": 'email_address',
        "phone_number": 'phone_number',
        "card": 'card',
        "decrypted_token": 'decrypted_token',
        "assurance_details": 'assurance_details',
        "attributes": 'attributes'
    }

    _optionals = [
        'name',
        'email_address',
        'phone_number',
        'card',
        'decrypted_token',
        'assurance_details',
        'attributes',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 card=APIHelper.SKIP,
                 decrypted_token=APIHelper.SKIP,
                 assurance_details=APIHelper.SKIP,
                 attributes=APIHelper.SKIP):
        """Constructor for the GooglePayRequest class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if card is not APIHelper.SKIP:
            self.card = card 
        if decrypted_token is not APIHelper.SKIP:
            self.decrypted_token = decrypted_token 
        if assurance_details is not APIHelper.SKIP:
            self.assurance_details = assurance_details 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        email_address = dictionary.get("email_address") if dictionary.get("email_address") else APIHelper.SKIP
        phone_number = PhoneNumberWithCountryCode.from_dictionary(dictionary.get('phone_number')) if 'phone_number' in dictionary.keys() else APIHelper.SKIP
        card = GooglePayRequestCard.from_dictionary(dictionary.get('card')) if 'card' in dictionary.keys() else APIHelper.SKIP
        decrypted_token = GooglePayDecryptedTokenData.from_dictionary(dictionary.get('decrypted_token')) if 'decrypted_token' in dictionary.keys() else APIHelper.SKIP
        assurance_details = AssuranceDetails.from_dictionary(dictionary.get('assurance_details')) if 'assurance_details' in dictionary.keys() else APIHelper.SKIP
        attributes = GooglePayCardAttributes.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email_address,
                   phone_number,
                   card,
                   decrypted_token,
                   assurance_details,
                   attributes)
