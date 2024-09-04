# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.capture_status_details import CaptureStatusDetails
from paypalrestapis.models.link_description import LinkDescription
from paypalrestapis.models.money import Money
from paypalrestapis.models.network_transaction_reference import NetworkTransactionReference
from paypalrestapis.models.payee import Payee
from paypalrestapis.models.payment_supplementary_data import PaymentSupplementaryData
from paypalrestapis.models.processor_response import ProcessorResponse
from paypalrestapis.models.seller_protection import SellerProtection
from paypalrestapis.models.seller_receivable_breakdown import SellerReceivableBreakdown


class CapturedPayment(object):

    """Implementation of the 'Captured Payment' model.

    A captured payment.

    Attributes:
        status (CaptureStatus): The status of the captured payment.
        status_details (CaptureStatusDetails): The details of the captured
            payment status.
        id (str): The PayPal-generated ID for the captured payment.
        amount (Money): The currency and amount for a financial transaction,
            such as a balance or payment due.
        invoice_id (str): The API caller-provided external invoice number for
            this order. Appears in both the payer's transaction history and
            the emails that the payer receives.
        custom_id (str): The API caller-provided external ID. Used to
            reconcile API caller-initiated transactions with PayPal
            transactions. Appears in transaction and settlement reports.
        network_transaction_reference (NetworkTransactionReference): Reference
            values used by the card network to identify a transaction.
        seller_protection (SellerProtection): The level of protection offered
            as defined by [PayPal Seller Protection for
            Merchants](https://www.paypal.com/us/webapps/mpp/security/seller-pr
            otection).
        final_capture (bool): Indicates whether you can make additional
            captures against the authorized payment. Set to `true` if you do
            not intend to capture additional payments against the
            authorization. Set to `false` if you intend to capture additional
            payments against the authorization.
        seller_receivable_breakdown (SellerReceivableBreakdown): The detailed
            breakdown of the capture activity. This is not available for
            transactions that are in pending state.
        disbursement_mode (DisbursementMode): The funds that are held on
            behalf of the merchant.
        links (List[LinkDescription]): An array of related [HATEOAS
            links](/docs/api/reference/api-responses/#hateoas-links).
        processor_response (ProcessorResponse): The processor response
            information for payment requests, such as direct credit card
            transactions.
        create_time (str): The date and time, in [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds
            are required while fractional seconds are
            optional.<blockquote><strong>Note:</strong> The regular expression
            provides guidance but does not reject all invalid
            dates.</blockquote>
        update_time (str): The date and time, in [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds
            are required while fractional seconds are
            optional.<blockquote><strong>Note:</strong> The regular expression
            provides guidance but does not reject all invalid
            dates.</blockquote>
        supplementary_data (PaymentSupplementaryData): The supplementary
            data.
        payee (Payee): The details for the merchant who receives the funds and
            fulfills the order. The merchant is also known as the payee.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "status_details": 'status_details',
        "id": 'id',
        "amount": 'amount',
        "invoice_id": 'invoice_id',
        "custom_id": 'custom_id',
        "network_transaction_reference": 'network_transaction_reference',
        "seller_protection": 'seller_protection',
        "final_capture": 'final_capture',
        "seller_receivable_breakdown": 'seller_receivable_breakdown',
        "disbursement_mode": 'disbursement_mode',
        "links": 'links',
        "processor_response": 'processor_response',
        "create_time": 'create_time',
        "update_time": 'update_time',
        "supplementary_data": 'supplementary_data',
        "payee": 'payee'
    }

    _optionals = [
        'status',
        'status_details',
        'id',
        'amount',
        'invoice_id',
        'custom_id',
        'network_transaction_reference',
        'seller_protection',
        'final_capture',
        'seller_receivable_breakdown',
        'disbursement_mode',
        'links',
        'processor_response',
        'create_time',
        'update_time',
        'supplementary_data',
        'payee',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 status_details=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 invoice_id=APIHelper.SKIP,
                 custom_id=APIHelper.SKIP,
                 network_transaction_reference=APIHelper.SKIP,
                 seller_protection=APIHelper.SKIP,
                 final_capture=False,
                 seller_receivable_breakdown=APIHelper.SKIP,
                 disbursement_mode='INSTANT',
                 links=APIHelper.SKIP,
                 processor_response=APIHelper.SKIP,
                 create_time=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 supplementary_data=APIHelper.SKIP,
                 payee=APIHelper.SKIP):
        """Constructor for the CapturedPayment class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_details is not APIHelper.SKIP:
            self.status_details = status_details 
        if id is not APIHelper.SKIP:
            self.id = id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if custom_id is not APIHelper.SKIP:
            self.custom_id = custom_id 
        if network_transaction_reference is not APIHelper.SKIP:
            self.network_transaction_reference = network_transaction_reference 
        if seller_protection is not APIHelper.SKIP:
            self.seller_protection = seller_protection 
        self.final_capture = final_capture 
        if seller_receivable_breakdown is not APIHelper.SKIP:
            self.seller_receivable_breakdown = seller_receivable_breakdown 
        self.disbursement_mode = disbursement_mode 
        if links is not APIHelper.SKIP:
            self.links = links 
        if processor_response is not APIHelper.SKIP:
            self.processor_response = processor_response 
        if create_time is not APIHelper.SKIP:
            self.create_time = create_time 
        if update_time is not APIHelper.SKIP:
            self.update_time = update_time 
        if supplementary_data is not APIHelper.SKIP:
            self.supplementary_data = supplementary_data 
        if payee is not APIHelper.SKIP:
            self.payee = payee 

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
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_details = CaptureStatusDetails.from_dictionary(dictionary.get('status_details')) if 'status_details' in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        amount = Money.from_dictionary(dictionary.get('amount')) if 'amount' in dictionary.keys() else APIHelper.SKIP
        invoice_id = dictionary.get("invoice_id") if dictionary.get("invoice_id") else APIHelper.SKIP
        custom_id = dictionary.get("custom_id") if dictionary.get("custom_id") else APIHelper.SKIP
        network_transaction_reference = NetworkTransactionReference.from_dictionary(dictionary.get('network_transaction_reference')) if 'network_transaction_reference' in dictionary.keys() else APIHelper.SKIP
        seller_protection = SellerProtection.from_dictionary(dictionary.get('seller_protection')) if 'seller_protection' in dictionary.keys() else APIHelper.SKIP
        final_capture = dictionary.get("final_capture") if dictionary.get("final_capture") else False
        seller_receivable_breakdown = SellerReceivableBreakdown.from_dictionary(dictionary.get('seller_receivable_breakdown')) if 'seller_receivable_breakdown' in dictionary.keys() else APIHelper.SKIP
        disbursement_mode = dictionary.get("disbursement_mode") if dictionary.get("disbursement_mode") else 'INSTANT'
        links = None
        if dictionary.get('links') is not None:
            links = [LinkDescription.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        processor_response = ProcessorResponse.from_dictionary(dictionary.get('processor_response')) if 'processor_response' in dictionary.keys() else APIHelper.SKIP
        create_time = dictionary.get("create_time") if dictionary.get("create_time") else APIHelper.SKIP
        update_time = dictionary.get("update_time") if dictionary.get("update_time") else APIHelper.SKIP
        supplementary_data = PaymentSupplementaryData.from_dictionary(dictionary.get('supplementary_data')) if 'supplementary_data' in dictionary.keys() else APIHelper.SKIP
        payee = Payee.from_dictionary(dictionary.get('payee')) if 'payee' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   status_details,
                   id,
                   amount,
                   invoice_id,
                   custom_id,
                   network_transaction_reference,
                   seller_protection,
                   final_capture,
                   seller_receivable_breakdown,
                   disbursement_mode,
                   links,
                   processor_response,
                   create_time,
                   update_time,
                   supplementary_data,
                   payee)
