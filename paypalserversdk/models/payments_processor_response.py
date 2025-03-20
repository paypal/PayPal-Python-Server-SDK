# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class PaymentsProcessorResponse(object):

    """Implementation of the 'Payments Processor Response' model.

    The processor response information for payment requests, such as direct
    credit card transactions.

    Attributes:
        avs_code (AvsCode): The address verification code for Visa, Discover,
            Mastercard, or American Express transactions.
        cvv_code (CvvCode): The card verification value code for for Visa,
            Discover, Mastercard, or American Express.
        response_code (ProcessorResponseCode): Processor response code for the
            non-PayPal payment processor errors.
        payment_advice_code (PaymentsPaymentAdviceCode): The declined payment
            transactions might have payment advice codes. The card networks,
            like Visa and Mastercard, return payment advice codes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "avs_code": 'avs_code',
        "cvv_code": 'cvv_code',
        "response_code": 'response_code',
        "payment_advice_code": 'payment_advice_code'
    }

    _optionals = [
        'avs_code',
        'cvv_code',
        'response_code',
        'payment_advice_code',
    ]

    def __init__(self,
                 avs_code=APIHelper.SKIP,
                 cvv_code=APIHelper.SKIP,
                 response_code=APIHelper.SKIP,
                 payment_advice_code=APIHelper.SKIP):
        """Constructor for the PaymentsProcessorResponse class"""

        # Initialize members of the class
        if avs_code is not APIHelper.SKIP:
            self.avs_code = avs_code 
        if cvv_code is not APIHelper.SKIP:
            self.cvv_code = cvv_code 
        if response_code is not APIHelper.SKIP:
            self.response_code = response_code 
        if payment_advice_code is not APIHelper.SKIP:
            self.payment_advice_code = payment_advice_code 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        avs_code = dictionary.get("avs_code") if dictionary.get("avs_code") else APIHelper.SKIP
        cvv_code = dictionary.get("cvv_code") if dictionary.get("cvv_code") else APIHelper.SKIP
        response_code = dictionary.get("response_code") if dictionary.get("response_code") else APIHelper.SKIP
        payment_advice_code = dictionary.get("payment_advice_code") if dictionary.get("payment_advice_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(avs_code,
                   cvv_code,
                   response_code,
                   payment_advice_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'avs_code={(self.avs_code if hasattr(self, "avs_code") else None)!r}, '
                f'cvv_code={(self.cvv_code if hasattr(self, "cvv_code") else None)!r}, '
                f'response_code={(self.response_code if hasattr(self, "response_code") else None)!r}, '
                f'payment_advice_code={(self.payment_advice_code if hasattr(self, "payment_advice_code") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'avs_code={(self.avs_code if hasattr(self, "avs_code") else None)!s}, '
                f'cvv_code={(self.cvv_code if hasattr(self, "cvv_code") else None)!s}, '
                f'response_code={(self.response_code if hasattr(self, "response_code") else None)!s}, '
                f'payment_advice_code={(self.payment_advice_code if hasattr(self, "payment_advice_code") else None)!s})')
