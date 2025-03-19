# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VaultInstructionAction(object):

    """Implementation of the 'Vault Instruction Action' enum.

    Vault Instruction on action to be performed after a successful payer
    approval.

    Attributes:
        ON_CREATE_PAYMENT_TOKENS: Vault the payment method after API caller
            performs a successful POST on Payment Tokens.
        ON_PAYER_APPROVAL: Vault the payment method on successful payer
            authentication and approval.

    """
    ON_CREATE_PAYMENT_TOKENS = 'ON_CREATE_PAYMENT_TOKENS'

    ON_PAYER_APPROVAL = 'ON_PAYER_APPROVAL'

