# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.apple_pay_payment_data import ApplePayPaymentData
from paypalserversdk.models.apple_pay_tokenized_card import ApplePayTokenizedCard
from paypalserversdk.models.money import Money


class ApplePayDecryptedTokenData(object):

    """Implementation of the 'Apple Pay Decrypted Token Data' model.

    Information about the Payment data obtained by decrypting Apple Pay
    token.

    Attributes:
        transaction_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        tokenized_card (ApplePayTokenizedCard): The payment card to use to
            fund a payment. Can be a credit or debit card.
        device_manufacturer_id (str): Apple Pay Hex-encoded device
            manufacturer identifier. The pattern is defined by an external
            party and supports Unicode.
        payment_data_type (ApplePayPaymentDataType): Indicates the type of
            payment data passed, in case of Non China the payment data is
            3DSECURE and for China it is EMV.
        payment_data (ApplePayPaymentData): Information about the decrypted
            apple pay payment data for the token like cryptogram, eci
            indicator.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tokenized_card": 'tokenized_card',
        "transaction_amount": 'transaction_amount',
        "device_manufacturer_id": 'device_manufacturer_id',
        "payment_data_type": 'payment_data_type',
        "payment_data": 'payment_data'
    }

    _optionals = [
        'transaction_amount',
        'device_manufacturer_id',
        'payment_data_type',
        'payment_data',
    ]

    def __init__(self,
                 tokenized_card=None,
                 transaction_amount=APIHelper.SKIP,
                 device_manufacturer_id=APIHelper.SKIP,
                 payment_data_type=APIHelper.SKIP,
                 payment_data=APIHelper.SKIP):
        """Constructor for the ApplePayDecryptedTokenData class"""

        # Initialize members of the class
        if transaction_amount is not APIHelper.SKIP:
            self.transaction_amount = transaction_amount 
        self.tokenized_card = tokenized_card 
        if device_manufacturer_id is not APIHelper.SKIP:
            self.device_manufacturer_id = device_manufacturer_id 
        if payment_data_type is not APIHelper.SKIP:
            self.payment_data_type = payment_data_type 
        if payment_data is not APIHelper.SKIP:
            self.payment_data = payment_data 

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
        tokenized_card = ApplePayTokenizedCard.from_dictionary(dictionary.get('tokenized_card')) if dictionary.get('tokenized_card') else None
        transaction_amount = Money.from_dictionary(dictionary.get('transaction_amount')) if 'transaction_amount' in dictionary.keys() else APIHelper.SKIP
        device_manufacturer_id = dictionary.get("device_manufacturer_id") if dictionary.get("device_manufacturer_id") else APIHelper.SKIP
        payment_data_type = dictionary.get("payment_data_type") if dictionary.get("payment_data_type") else APIHelper.SKIP
        payment_data = ApplePayPaymentData.from_dictionary(dictionary.get('payment_data')) if 'payment_data' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(tokenized_card,
                   transaction_amount,
                   device_manufacturer_id,
                   payment_data_type,
                   payment_data)
