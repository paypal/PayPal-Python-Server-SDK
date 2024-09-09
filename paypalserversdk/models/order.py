# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.payer import Payer
from paypalserversdk.models.payment_source_response import PaymentSourceResponse
from paypalserversdk.models.purchase_unit import PurchaseUnit


class Order(object):

    """Implementation of the 'Order' model.

    The order details.

    Attributes:
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
        id (str): The ID of the order.
        payment_source (PaymentSourceResponse): The payment source used to
            fund the payment.
        intent (CheckoutPaymentIntent): The intent to either capture payment
            immediately or authorize a payment for an order after order
            creation.
        processing_instruction (ProcessingInstruction): The instruction to
            process an order.
        payer (Payer): TODO: type description here.
        purchase_units (List[PurchaseUnit]): An array of purchase units. Each
            purchase unit establishes a contract between a customer and
            merchant. Each purchase unit represents either a full or partial
            order that the customer intends to purchase from the merchant.
        status (OrderStatus): The order status.
        links (List[LinkDescription]): An array of request-related HATEOAS
            links. To complete payer approval, use the `approve` link to
            redirect the payer. The API caller has 3 hours (default setting,
            this which can be changed by your account manager to 24/48/72
            hours to accommodate your use case) from the time the order is
            created, to redirect your payer. Once redirected, the API caller
            has 3 hours for the payer to approve the order and either
            authorize or capture the order. If you are not using the PayPal
            JavaScript SDK to initiate PayPal Checkout (in context) ensure
            that you include `application_context.return_url` is specified or
            you will get "We're sorry, Things don't appear to be working at
            the moment" after the payer approves the payment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_time": 'create_time',
        "update_time": 'update_time',
        "id": 'id',
        "payment_source": 'payment_source',
        "intent": 'intent',
        "processing_instruction": 'processing_instruction',
        "payer": 'payer',
        "purchase_units": 'purchase_units',
        "status": 'status',
        "links": 'links'
    }

    _optionals = [
        'create_time',
        'update_time',
        'id',
        'payment_source',
        'intent',
        'processing_instruction',
        'payer',
        'purchase_units',
        'status',
        'links',
    ]

    def __init__(self,
                 create_time=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 payment_source=APIHelper.SKIP,
                 intent=APIHelper.SKIP,
                 processing_instruction='NO_INSTRUCTION',
                 payer=APIHelper.SKIP,
                 purchase_units=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 links=APIHelper.SKIP):
        """Constructor for the Order class"""

        # Initialize members of the class
        if create_time is not APIHelper.SKIP:
            self.create_time = create_time 
        if update_time is not APIHelper.SKIP:
            self.update_time = update_time 
        if id is not APIHelper.SKIP:
            self.id = id 
        if payment_source is not APIHelper.SKIP:
            self.payment_source = payment_source 
        if intent is not APIHelper.SKIP:
            self.intent = intent 
        self.processing_instruction = processing_instruction 
        if payer is not APIHelper.SKIP:
            self.payer = payer 
        if purchase_units is not APIHelper.SKIP:
            self.purchase_units = purchase_units 
        if status is not APIHelper.SKIP:
            self.status = status 
        if links is not APIHelper.SKIP:
            self.links = links 

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
        create_time = dictionary.get("create_time") if dictionary.get("create_time") else APIHelper.SKIP
        update_time = dictionary.get("update_time") if dictionary.get("update_time") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        payment_source = PaymentSourceResponse.from_dictionary(dictionary.get('payment_source')) if 'payment_source' in dictionary.keys() else APIHelper.SKIP
        intent = dictionary.get("intent") if dictionary.get("intent") else APIHelper.SKIP
        processing_instruction = dictionary.get("processing_instruction") if dictionary.get("processing_instruction") else 'NO_INSTRUCTION'
        payer = Payer.from_dictionary(dictionary.get('payer')) if 'payer' in dictionary.keys() else APIHelper.SKIP
        purchase_units = None
        if dictionary.get('purchase_units') is not None:
            purchase_units = [PurchaseUnit.from_dictionary(x) for x in dictionary.get('purchase_units')]
        else:
            purchase_units = APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [LinkDescription.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        # Return an object of this model
        return cls(create_time,
                   update_time,
                   id,
                   payment_source,
                   intent,
                   processing_instruction,
                   payer,
                   purchase_units,
                   status,
                   links)
