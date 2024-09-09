# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.capture_payment_instruction import CapturePaymentInstruction
from paypalserversdk.models.money import Money


class CaptureRequest(object):

    """Implementation of the 'Capture Request' model.

    TODO: type model description here.

    Attributes:
        invoice_id (str): The API caller-provided external invoice number for
            this order. Appears in both the payer's transaction history and
            the emails that the payer receives.
        note_to_payer (str): An informational note about this settlement.
            Appears in both the payer's transaction history and the emails
            that the payer receives.
        amount (Money): The currency and amount for a financial transaction,
            such as a balance or payment due.
        final_capture (bool): Indicates whether you can make additional
            captures against the authorized payment. Set to `true` if you do
            not intend to capture additional payments against the
            authorization. Set to `false` if you intend to capture additional
            payments against the authorization.
        payment_instruction (CapturePaymentInstruction): Any additional
            payment instructions to be consider during payment processing.
            This processing instruction is applicable for Capturing an order
            or Authorizing an Order.
        soft_descriptor (str): The payment descriptor on the payer's account
            statement.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_id": 'invoice_id',
        "note_to_payer": 'note_to_payer',
        "amount": 'amount',
        "final_capture": 'final_capture',
        "payment_instruction": 'payment_instruction',
        "soft_descriptor": 'soft_descriptor'
    }

    _optionals = [
        'invoice_id',
        'note_to_payer',
        'amount',
        'final_capture',
        'payment_instruction',
        'soft_descriptor',
    ]

    def __init__(self,
                 invoice_id=APIHelper.SKIP,
                 note_to_payer=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 final_capture=False,
                 payment_instruction=APIHelper.SKIP,
                 soft_descriptor=APIHelper.SKIP):
        """Constructor for the CaptureRequest class"""

        # Initialize members of the class
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if note_to_payer is not APIHelper.SKIP:
            self.note_to_payer = note_to_payer 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        self.final_capture = final_capture 
        if payment_instruction is not APIHelper.SKIP:
            self.payment_instruction = payment_instruction 
        if soft_descriptor is not APIHelper.SKIP:
            self.soft_descriptor = soft_descriptor 

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
        invoice_id = dictionary.get("invoice_id") if dictionary.get("invoice_id") else APIHelper.SKIP
        note_to_payer = dictionary.get("note_to_payer") if dictionary.get("note_to_payer") else APIHelper.SKIP
        amount = Money.from_dictionary(dictionary.get('amount')) if 'amount' in dictionary.keys() else APIHelper.SKIP
        final_capture = dictionary.get("final_capture") if dictionary.get("final_capture") else False
        payment_instruction = CapturePaymentInstruction.from_dictionary(dictionary.get('payment_instruction')) if 'payment_instruction' in dictionary.keys() else APIHelper.SKIP
        soft_descriptor = dictionary.get("soft_descriptor") if dictionary.get("soft_descriptor") else APIHelper.SKIP
        # Return an object of this model
        return cls(invoice_id,
                   note_to_payer,
                   amount,
                   final_capture,
                   payment_instruction,
                   soft_descriptor)