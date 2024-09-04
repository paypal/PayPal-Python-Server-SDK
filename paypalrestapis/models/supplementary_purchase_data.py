# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper


class SupplementaryPurchaseData(object):

    """Implementation of the 'Supplementary Purchase Data' model.

    The capture identification-related fields. Includes the invoice ID, custom
    ID, note to payer, and soft descriptor.

    Attributes:
        invoice_id (str): The API caller-provided external invoice number for
            this order. Appears in both the payer's transaction history and
            the emails that the payer receives.
        note_to_payer (str): An informational note about this settlement.
            Appears in both the payer's transaction history and the emails
            that the payer receives.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_id": 'invoice_id',
        "note_to_payer": 'note_to_payer'
    }

    _optionals = [
        'invoice_id',
        'note_to_payer',
    ]

    def __init__(self,
                 invoice_id=APIHelper.SKIP,
                 note_to_payer=APIHelper.SKIP):
        """Constructor for the SupplementaryPurchaseData class"""

        # Initialize members of the class
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if note_to_payer is not APIHelper.SKIP:
            self.note_to_payer = note_to_payer 

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
        # Return an object of this model
        return cls(invoice_id,
                   note_to_payer)