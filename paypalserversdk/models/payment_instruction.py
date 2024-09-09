# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.platform_fee import PlatformFee


class PaymentInstruction(object):

    """Implementation of the 'Payment Instruction' model.

    Any additional payment instructions to be consider during payment
    processing. This processing instruction is applicable for Capturing an
    order or Authorizing an Order.

    Attributes:
        platform_fees (List[PlatformFee]): An array of various fees,
            commissions, tips, or donations. This field is only applicable to
            merchants that been enabled for PayPal Complete Payments Platform
            for Marketplaces and Platforms capability.
        disbursement_mode (DisbursementMode): The funds that are held on
            behalf of the merchant.
        payee_pricing_tier_id (str): This field is only enabled for selected
            merchants/partners to use and provides the ability to trigger a
            specific pricing rate/plan for a payment transaction. The list of
            eligible 'payee_pricing_tier_id' would be provided to you by your
            Account Manager. Specifying values other than the one provided to
            you by your account manager would result in an error.
        payee_receivable_fx_rate_id (str): FX identifier generated returned by
            PayPal to be used for payment processing in order to honor FX rate
            (for eligible integrations) to be used when amount is
            settled/received into the payee account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "platform_fees": 'platform_fees',
        "disbursement_mode": 'disbursement_mode',
        "payee_pricing_tier_id": 'payee_pricing_tier_id',
        "payee_receivable_fx_rate_id": 'payee_receivable_fx_rate_id'
    }

    _optionals = [
        'platform_fees',
        'disbursement_mode',
        'payee_pricing_tier_id',
        'payee_receivable_fx_rate_id',
    ]

    def __init__(self,
                 platform_fees=APIHelper.SKIP,
                 disbursement_mode='INSTANT',
                 payee_pricing_tier_id=APIHelper.SKIP,
                 payee_receivable_fx_rate_id=APIHelper.SKIP):
        """Constructor for the PaymentInstruction class"""

        # Initialize members of the class
        if platform_fees is not APIHelper.SKIP:
            self.platform_fees = platform_fees 
        self.disbursement_mode = disbursement_mode 
        if payee_pricing_tier_id is not APIHelper.SKIP:
            self.payee_pricing_tier_id = payee_pricing_tier_id 
        if payee_receivable_fx_rate_id is not APIHelper.SKIP:
            self.payee_receivable_fx_rate_id = payee_receivable_fx_rate_id 

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
        platform_fees = None
        if dictionary.get('platform_fees') is not None:
            platform_fees = [PlatformFee.from_dictionary(x) for x in dictionary.get('platform_fees')]
        else:
            platform_fees = APIHelper.SKIP
        disbursement_mode = dictionary.get("disbursement_mode") if dictionary.get("disbursement_mode") else 'INSTANT'
        payee_pricing_tier_id = dictionary.get("payee_pricing_tier_id") if dictionary.get("payee_pricing_tier_id") else APIHelper.SKIP
        payee_receivable_fx_rate_id = dictionary.get("payee_receivable_fx_rate_id") if dictionary.get("payee_receivable_fx_rate_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(platform_fees,
                   disbursement_mode,
                   payee_pricing_tier_id,
                   payee_receivable_fx_rate_id)