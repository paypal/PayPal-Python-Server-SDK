# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.exchange_rate import ExchangeRate
from paypalserversdk.models.money import Money
from paypalserversdk.models.platform_fee import PlatformFee


class SellerReceivableBreakdown(object):

    """Implementation of the 'Seller Receivable Breakdown' model.

    The detailed breakdown of the capture activity. This is not available for
    transactions that are in pending state.

    Attributes:
        gross_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        paypal_fee (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        paypal_fee_in_receivable_currency (Money): The currency and amount for
            a financial transaction, such as a balance or payment due.
        net_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        receivable_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        exchange_rate (ExchangeRate): The exchange rate that determines the
            amount to convert from one currency to another currency.
        platform_fees (List[PlatformFee]): An array of platform or partner
            fees, commissions, or brokerage fees that associated with the
            captured payment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gross_amount": 'gross_amount',
        "paypal_fee": 'paypal_fee',
        "paypal_fee_in_receivable_currency": 'paypal_fee_in_receivable_currency',
        "net_amount": 'net_amount',
        "receivable_amount": 'receivable_amount',
        "exchange_rate": 'exchange_rate',
        "platform_fees": 'platform_fees'
    }

    _optionals = [
        'paypal_fee',
        'paypal_fee_in_receivable_currency',
        'net_amount',
        'receivable_amount',
        'exchange_rate',
        'platform_fees',
    ]

    def __init__(self,
                 gross_amount=None,
                 paypal_fee=APIHelper.SKIP,
                 paypal_fee_in_receivable_currency=APIHelper.SKIP,
                 net_amount=APIHelper.SKIP,
                 receivable_amount=APIHelper.SKIP,
                 exchange_rate=APIHelper.SKIP,
                 platform_fees=APIHelper.SKIP):
        """Constructor for the SellerReceivableBreakdown class"""

        # Initialize members of the class
        self.gross_amount = gross_amount 
        if paypal_fee is not APIHelper.SKIP:
            self.paypal_fee = paypal_fee 
        if paypal_fee_in_receivable_currency is not APIHelper.SKIP:
            self.paypal_fee_in_receivable_currency = paypal_fee_in_receivable_currency 
        if net_amount is not APIHelper.SKIP:
            self.net_amount = net_amount 
        if receivable_amount is not APIHelper.SKIP:
            self.receivable_amount = receivable_amount 
        if exchange_rate is not APIHelper.SKIP:
            self.exchange_rate = exchange_rate 
        if platform_fees is not APIHelper.SKIP:
            self.platform_fees = platform_fees 

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
        gross_amount = Money.from_dictionary(dictionary.get('gross_amount')) if dictionary.get('gross_amount') else None
        paypal_fee = Money.from_dictionary(dictionary.get('paypal_fee')) if 'paypal_fee' in dictionary.keys() else APIHelper.SKIP
        paypal_fee_in_receivable_currency = Money.from_dictionary(dictionary.get('paypal_fee_in_receivable_currency')) if 'paypal_fee_in_receivable_currency' in dictionary.keys() else APIHelper.SKIP
        net_amount = Money.from_dictionary(dictionary.get('net_amount')) if 'net_amount' in dictionary.keys() else APIHelper.SKIP
        receivable_amount = Money.from_dictionary(dictionary.get('receivable_amount')) if 'receivable_amount' in dictionary.keys() else APIHelper.SKIP
        exchange_rate = ExchangeRate.from_dictionary(dictionary.get('exchange_rate')) if 'exchange_rate' in dictionary.keys() else APIHelper.SKIP
        platform_fees = None
        if dictionary.get('platform_fees') is not None:
            platform_fees = [PlatformFee.from_dictionary(x) for x in dictionary.get('platform_fees')]
        else:
            platform_fees = APIHelper.SKIP
        # Return an object of this model
        return cls(gross_amount,
                   paypal_fee,
                   paypal_fee_in_receivable_currency,
                   net_amount,
                   receivable_amount,
                   exchange_rate,
                   platform_fees)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'gross_amount={self.gross_amount!r}, '
                f'paypal_fee={(self.paypal_fee if hasattr(self, "paypal_fee") else None)!r}, '
                f'paypal_fee_in_receivable_currency={(self.paypal_fee_in_receivable_currency if hasattr(self, "paypal_fee_in_receivable_currency") else None)!r}, '
                f'net_amount={(self.net_amount if hasattr(self, "net_amount") else None)!r}, '
                f'receivable_amount={(self.receivable_amount if hasattr(self, "receivable_amount") else None)!r}, '
                f'exchange_rate={(self.exchange_rate if hasattr(self, "exchange_rate") else None)!r}, '
                f'platform_fees={(self.platform_fees if hasattr(self, "platform_fees") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'gross_amount={self.gross_amount!s}, '
                f'paypal_fee={(self.paypal_fee if hasattr(self, "paypal_fee") else None)!s}, '
                f'paypal_fee_in_receivable_currency={(self.paypal_fee_in_receivable_currency if hasattr(self, "paypal_fee_in_receivable_currency") else None)!s}, '
                f'net_amount={(self.net_amount if hasattr(self, "net_amount") else None)!s}, '
                f'receivable_amount={(self.receivable_amount if hasattr(self, "receivable_amount") else None)!s}, '
                f'exchange_rate={(self.exchange_rate if hasattr(self, "exchange_rate") else None)!s}, '
                f'platform_fees={(self.platform_fees if hasattr(self, "platform_fees") else None)!s})')
