# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper


class BinDetails(object):

    """Implementation of the 'Bin Details' model.

    Bank Identification Number (BIN) details used to fund a payment.

    Attributes:
        bin (str): The Bank Identification Number (BIN) signifies the number
            that is being used to identify the granular level details (except
            the PII information) of the card.
        issuing_bank (str): The issuer of the card instrument.
        bin_country_code (str): The [two-character ISO 3166-1
            code](/api/rest/reference/country-codes/) that identifies the
            country or region.<blockquote><strong>Note:</strong> The country
            code for Great Britain is <code>GB</code> and not <code>UK</code>
            as used in the top-level domain names for that country. Use the
            `C2` country code for China worldwide for comparable uncontrolled
            price (CUP) method, bank card, and cross-border
            transactions.</blockquote>
        products (List[str]): The type of card product assigned to the BIN by
            the issuer. These values are defined by the issuer and may change
            over time. Some examples include: PREPAID_GIFT, CONSUMER,
            CORPORATE.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bin": 'bin',
        "issuing_bank": 'issuing_bank',
        "bin_country_code": 'bin_country_code',
        "products": 'products'
    }

    _optionals = [
        'bin',
        'issuing_bank',
        'bin_country_code',
        'products',
    ]

    def __init__(self,
                 bin=APIHelper.SKIP,
                 issuing_bank=APIHelper.SKIP,
                 bin_country_code=APIHelper.SKIP,
                 products=APIHelper.SKIP):
        """Constructor for the BinDetails class"""

        # Initialize members of the class
        if bin is not APIHelper.SKIP:
            self.bin = bin 
        if issuing_bank is not APIHelper.SKIP:
            self.issuing_bank = issuing_bank 
        if bin_country_code is not APIHelper.SKIP:
            self.bin_country_code = bin_country_code 
        if products is not APIHelper.SKIP:
            self.products = products 

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
        bin = dictionary.get("bin") if dictionary.get("bin") else APIHelper.SKIP
        issuing_bank = dictionary.get("issuing_bank") if dictionary.get("issuing_bank") else APIHelper.SKIP
        bin_country_code = dictionary.get("bin_country_code") if dictionary.get("bin_country_code") else APIHelper.SKIP
        products = dictionary.get("products") if dictionary.get("products") else APIHelper.SKIP
        # Return an object of this model
        return cls(bin,
                   issuing_bank,
                   bin_country_code,
                   products)