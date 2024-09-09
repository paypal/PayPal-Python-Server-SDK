# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class MyBankPaymentObject(object):

    """Implementation of the 'MyBank Payment Object' model.

    Information used to pay using MyBank.

    Attributes:
        name (str): The full name representation like Mr J Smith.
        country_code (str): The [two-character ISO 3166-1
            code](/api/rest/reference/country-codes/) that identifies the
            country or region.<blockquote><strong>Note:</strong> The country
            code for Great Britain is <code>GB</code> and not <code>UK</code>
            as used in the top-level domain names for that country. Use the
            `C2` country code for China worldwide for comparable uncontrolled
            price (CUP) method, bank card, and cross-border
            transactions.</blockquote>
        bic (str): The business identification code (BIC). In payments
            systems, a BIC is used to identify a specific business, most
            commonly a bank.
        iban_last_chars (str): The last characters of the IBAN used to pay.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "country_code": 'country_code',
        "bic": 'bic',
        "iban_last_chars": 'iban_last_chars'
    }

    _optionals = [
        'name',
        'country_code',
        'bic',
        'iban_last_chars',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 bic=APIHelper.SKIP,
                 iban_last_chars=APIHelper.SKIP):
        """Constructor for the MyBankPaymentObject class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if bic is not APIHelper.SKIP:
            self.bic = bic 
        if iban_last_chars is not APIHelper.SKIP:
            self.iban_last_chars = iban_last_chars 

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
        country_code = dictionary.get("country_code") if dictionary.get("country_code") else APIHelper.SKIP
        bic = dictionary.get("bic") if dictionary.get("bic") else APIHelper.SKIP
        iban_last_chars = dictionary.get("iban_last_chars") if dictionary.get("iban_last_chars") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   country_code,
                   bic,
                   iban_last_chars)
