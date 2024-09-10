# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.item import Item
from paypalserversdk.models.payee import Payee
from paypalserversdk.models.payment_instruction import PaymentInstruction
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.supplementary_data import SupplementaryData


class PurchaseUnitRequest(object):

    """Implementation of the 'Purchase Unit Request' model.

    The purchase unit request. Includes required information for the payment
    contract.

    Attributes:
        reference_id (str): The API caller-provided external ID for the
            purchase unit. Required for multiple purchase units when you must
            update the order through `PATCH`. If you omit this value and the
            order contains only one purchase unit, PayPal sets this value to
            `default`.
        amount (AmountWithBreakdown): The total order amount with an optional
            breakdown that provides details, such as the total item amount,
            total tax amount, shipping, handling, insurance, and discounts, if
            any.<br/>If you specify `amount.breakdown`, the amount equals
            `item_total` plus `tax_total` plus `shipping` plus `handling` plus
            `insurance` minus `shipping_discount` minus discount.<br/>The
            amount must be a positive number. For listed of supported
            currencies and decimal precision, see the PayPal REST APIs <a
            href="/docs/integration/direct/rest/currency-codes/">Currency
            Codes</a>.
        payee (Payee): The merchant who receives the funds and fulfills the
            order. The merchant is also known as the payee.
        payment_instruction (PaymentInstruction): Any additional payment
            instructions to be consider during payment processing. This
            processing instruction is applicable for Capturing an order or
            Authorizing an Order.
        description (str): The purchase description. The maximum length of the
            character is dependent on the type of characters used. The
            character length is specified assuming a US ASCII character.
            Depending on type of character; (e.g. accented character, Japanese
            characters) the number of characters that that can be specified as
            input might not equal the permissible max length.
        custom_id (str): The API caller-provided external ID. Used to
            reconcile client transactions with PayPal transactions. Appears in
            transaction and settlement reports but is not visible to the
            payer.
        invoice_id (str): The API caller-provided external invoice number for
            this order. Appears in both the payer's transaction history and
            the emails that the payer receives.
        soft_descriptor (str): The soft descriptor is the dynamic text used to
            construct the statement descriptor that appears on a payer's card
            statement.<br><br>If an Order is paid using the "PayPal Wallet",
            the statement descriptor will appear in following format on the
            payer's card statement:
            <code><var>PAYPAL_prefix</var>+(space)+<var>merchant_descriptor</va
            r>+(space)+
            <var>soft_descriptor</var></code><blockquote><strong>Note:</strong>
            The merchant descriptor is the descriptor of the merchant’s
            payment receiving preferences which can be seen by logging into
            the merchant account
            https://www.sandbox.paypal.com/businessprofile/settings/info/edit</
            blockquote>The <code>PAYPAL</code> prefix uses 8 characters. Only
            the first 22 characters will be displayed in the statement.
            <br>For example, if:<ul><li>The PayPal prefix toggle is
            <code>PAYPAL *</code>.</li><li>The merchant descriptor in the
            profile is <code>Janes Gift</code>.</li><li>The soft descriptor is
            <code>800-123-1234</code>.</li></ul>Then, the statement descriptor
            on the card is <code>PAYPAL * Janes Gift 80</code>.
        items (List[Item]): An array of items that the customer purchases from
            the merchant.
        shipping (ShippingDetails): The shipping details.
        supplementary_data (SupplementaryData): Supplementary data about a
            payment. This object passes information that can be used to
            improve risk assessments and processing costs, for example, by
            providing Level 2 and Level 3 payment data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "reference_id": 'reference_id',
        "payee": 'payee',
        "payment_instruction": 'payment_instruction',
        "description": 'description',
        "custom_id": 'custom_id',
        "invoice_id": 'invoice_id',
        "soft_descriptor": 'soft_descriptor',
        "items": 'items',
        "shipping": 'shipping',
        "supplementary_data": 'supplementary_data'
    }

    _optionals = [
        'reference_id',
        'payee',
        'payment_instruction',
        'description',
        'custom_id',
        'invoice_id',
        'soft_descriptor',
        'items',
        'shipping',
        'supplementary_data',
    ]

    def __init__(self,
                 amount=None,
                 reference_id=APIHelper.SKIP,
                 payee=APIHelper.SKIP,
                 payment_instruction=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 custom_id=APIHelper.SKIP,
                 invoice_id=APIHelper.SKIP,
                 soft_descriptor=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 shipping=APIHelper.SKIP,
                 supplementary_data=APIHelper.SKIP):
        """Constructor for the PurchaseUnitRequest class"""

        # Initialize members of the class
        if reference_id is not APIHelper.SKIP:
            self.reference_id = reference_id 
        self.amount = amount 
        if payee is not APIHelper.SKIP:
            self.payee = payee 
        if payment_instruction is not APIHelper.SKIP:
            self.payment_instruction = payment_instruction 
        if description is not APIHelper.SKIP:
            self.description = description 
        if custom_id is not APIHelper.SKIP:
            self.custom_id = custom_id 
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if soft_descriptor is not APIHelper.SKIP:
            self.soft_descriptor = soft_descriptor 
        if items is not APIHelper.SKIP:
            self.items = items 
        if shipping is not APIHelper.SKIP:
            self.shipping = shipping 
        if supplementary_data is not APIHelper.SKIP:
            self.supplementary_data = supplementary_data 

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
        amount = AmountWithBreakdown.from_dictionary(dictionary.get('amount')) if dictionary.get('amount') else None
        reference_id = dictionary.get("reference_id") if dictionary.get("reference_id") else APIHelper.SKIP
        payee = Payee.from_dictionary(dictionary.get('payee')) if 'payee' in dictionary.keys() else APIHelper.SKIP
        payment_instruction = PaymentInstruction.from_dictionary(dictionary.get('payment_instruction')) if 'payment_instruction' in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        custom_id = dictionary.get("custom_id") if dictionary.get("custom_id") else APIHelper.SKIP
        invoice_id = dictionary.get("invoice_id") if dictionary.get("invoice_id") else APIHelper.SKIP
        soft_descriptor = dictionary.get("soft_descriptor") if dictionary.get("soft_descriptor") else APIHelper.SKIP
        items = None
        if dictionary.get('items') is not None:
            items = [Item.from_dictionary(x) for x in dictionary.get('items')]
        else:
            items = APIHelper.SKIP
        shipping = ShippingDetails.from_dictionary(dictionary.get('shipping')) if 'shipping' in dictionary.keys() else APIHelper.SKIP
        supplementary_data = SupplementaryData.from_dictionary(dictionary.get('supplementary_data')) if 'supplementary_data' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   reference_id,
                   payee,
                   payment_instruction,
                   description,
                   custom_id,
                   invoice_id,
                   soft_descriptor,
                   items,
                   shipping,
                   supplementary_data)
