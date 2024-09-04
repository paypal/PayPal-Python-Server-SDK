# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.money import Money
from paypalrestapis.models.payee_base import PayeeBase


class PlatformFee(object):

    """Implementation of the 'Platform Fee' model.

    The platform or partner fee, commission, or brokerage fee that is
    associated with the transaction. Not a separate or isolated transaction
    leg from the external perspective. The platform fee is limited in scope
    and is always associated with the original payment for the purchase unit.

    Attributes:
        amount (Money): The currency and amount for a financial transaction,
            such as a balance or payment due.
        payee (PayeeBase): The details for the merchant who receives the funds
            and fulfills the order. The merchant is also known as the payee.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "payee": 'payee'
    }

    _optionals = [
        'payee',
    ]

    def __init__(self,
                 amount=None,
                 payee=APIHelper.SKIP):
        """Constructor for the PlatformFee class"""

        # Initialize members of the class
        self.amount = amount 
        if payee is not APIHelper.SKIP:
            self.payee = payee 

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
        amount = Money.from_dictionary(dictionary.get('amount')) if dictionary.get('amount') else None
        payee = PayeeBase.from_dictionary(dictionary.get('payee')) if 'payee' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   payee)