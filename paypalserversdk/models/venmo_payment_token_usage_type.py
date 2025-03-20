# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VenmoPaymentTokenUsageType(object):

    """Implementation of the 'Venmo Payment Token Usage Type' enum.

    The usage type associated with the Venmo payment token.

    Attributes:
        MERCHANT: The Venmo Payment Token will be used for future transaction
            directly with a merchant.
        PLATFORM: The Venmo Payment Token will be used for future transaction
            on a platform. A platform is typically a marketplace or a channel
            that a payer can purchase goods and services from multiple
            merchants.

    """
    MERCHANT = 'MERCHANT'

    PLATFORM = 'PLATFORM'

