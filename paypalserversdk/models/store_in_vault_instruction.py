# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class StoreInVaultInstruction(object):

    """Implementation of the 'Store In Vault Instruction' enum.

    Defines how and when the payment source gets vaulted.

    Attributes:
        ON_SUCCESS: Defines that the payment_source will be vaulted only when
            at least one authorization or capture using that payment_source is
            successful.

    """
    ON_SUCCESS = 'ON_SUCCESS'

