# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Money(object):

    """Implementation of the 'Money' model.

    The currency and amount for a financial transaction, such as a balance or
    payment due.

    Attributes:
        currency_code (str): The [three-character ISO-4217 currency
            code](/api/rest/reference/currency-codes/) that identifies the
            currency.
        value (str): The value, which might be:<ul><li>An integer for
            currencies like `JPY` that are not typically fractional.</li><li>A
            decimal fraction for currencies like `TND` that are subdivided
            into thousandths.</li></ul>For the required number of decimal
            places for a currency code, see [Currency
            Codes](/api/rest/reference/currency-codes/).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_code": 'currency_code',
        "value": 'value'
    }

    def __init__(self,
                 currency_code=None,
                 value=None):
        """Constructor for the Money class"""

        # Initialize members of the class
        self.currency_code = currency_code 
        self.value = value 

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
        currency_code = dictionary.get("currency_code") if dictionary.get("currency_code") else None
        value = dictionary.get("value") if dictionary.get("value") else None
        # Return an object of this model
        return cls(currency_code,
                   value)
