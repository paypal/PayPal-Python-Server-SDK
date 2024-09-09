# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.customer_request import CustomerRequest
from paypalserversdk.models.payment_token_request_payment_source import PaymentTokenRequestPaymentSource


class PaymentTokenRequest(object):

    """Implementation of the 'Payment Token Request' model.

    Payment Token Request where the `source` defines the type of instrument to
    be stored.

    Attributes:
        customer (CustomerRequest): Customer in merchant's or partner's system
            of records.
        payment_source (PaymentTokenRequestPaymentSource): The payment method
            to vault with the instrument details.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_source": 'payment_source',
        "customer": 'customer'
    }

    _optionals = [
        'customer',
    ]

    def __init__(self,
                 payment_source=None,
                 customer=APIHelper.SKIP):
        """Constructor for the PaymentTokenRequest class"""

        # Initialize members of the class
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        self.payment_source = payment_source 

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
        payment_source = PaymentTokenRequestPaymentSource.from_dictionary(dictionary.get('payment_source')) if dictionary.get('payment_source') else None
        customer = CustomerRequest.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment_source,
                   customer)
