# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.network_transaction_reference import NetworkTransactionReference


class StoredPaymentSource(object):

    """Implementation of the 'Stored Payment Source' model.

    Provides additional details to process a payment using a `payment_source`
    that has been stored or is intended to be stored (also referred to as
    stored_credential or card-on-file).<br/>Parameter
    compatibility:<br/><ul><li>`payment_type=ONE_TIME` is compatible only with
    `payment_initiator=CUSTOMER`.</li><li>`usage=FIRST` is compatible only
    with
    `payment_initiator=CUSTOMER`.</li><li>`previous_transaction_reference` or
    `previous_network_transaction_reference` is compatible only with
    `payment_initiator=MERCHANT`.</li><li>Only one of the parameters -
    `previous_transaction_reference` and
    `previous_network_transaction_reference` - can be present in the
    request.</li></ul>

    Attributes:
        payment_initiator (PaymentInitiator): The person or party who
            initiated or triggered the payment.
        payment_type (StoredPaymentSourcePaymentType): Indicates the type of
            the stored payment_source payment.
        usage (StoredPaymentSourceUsageType): Indicates if this is a `first`
            or `subsequent` payment using a stored payment source (also
            referred to as stored credential or card on file).
        previous_network_transaction_reference (NetworkTransactionReference):
            Reference values used by the card network to identify a
            transaction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_initiator": 'payment_initiator',
        "payment_type": 'payment_type',
        "usage": 'usage',
        "previous_network_transaction_reference": 'previous_network_transaction_reference'
    }

    _optionals = [
        'usage',
        'previous_network_transaction_reference',
    ]

    def __init__(self,
                 payment_initiator=None,
                 payment_type=None,
                 usage='DERIVED',
                 previous_network_transaction_reference=APIHelper.SKIP):
        """Constructor for the StoredPaymentSource class"""

        # Initialize members of the class
        self.payment_initiator = payment_initiator 
        self.payment_type = payment_type 
        self.usage = usage 
        if previous_network_transaction_reference is not APIHelper.SKIP:
            self.previous_network_transaction_reference = previous_network_transaction_reference 

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
        payment_initiator = dictionary.get("payment_initiator") if dictionary.get("payment_initiator") else None
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else None
        usage = dictionary.get("usage") if dictionary.get("usage") else 'DERIVED'
        previous_network_transaction_reference = NetworkTransactionReference.from_dictionary(dictionary.get('previous_network_transaction_reference')) if 'previous_network_transaction_reference' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment_initiator,
                   payment_type,
                   usage,
                   previous_network_transaction_reference)
