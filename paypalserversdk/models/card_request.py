# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_attributes import CardAttributes
from paypalserversdk.models.card_experience_context import CardExperienceContext
from paypalserversdk.models.card_stored_credential import CardStoredCredential
from paypalserversdk.models.network_token import NetworkToken


class CardRequest(object):

    """Implementation of the 'Card Request' model.

    The payment card to use to fund a payment. Can be a credit or debit
    card.<blockquote><strong>Note:</strong> Passing card number, cvv and
    expiry directly via the API requires <a
    href="https://www.pcisecuritystandards.org/pci_security/completing_self_ass
    essment"> PCI SAQ D compliance</a>. <br>*PayPal offers a mechanism by
    which you do not have to take on the <strong>PCI SAQ D</strong> burden by
    using hosted fields - refer to <a
    href="https://developer.paypal.com/docs/checkout/advanced/integrate/">this
    Integration Guide</a>*.</blockquote>

    Attributes:
        name (str): The card holder's name as it appears on the card.
        number (str): The primary account number (PAN) for the payment card.
        expiry (str): The year and month, in ISO-8601 `YYYY-MM` date format.
            See [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6).
        security_code (str): The three- or four-digit security code of the
            card. Also known as the CVV, CVC, CVN, CVE, or CID. This parameter
            cannot be present in the request when
            `payment_initiator=MERCHANT`.
        billing_address (Address): The portable international postal address.
            Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).
        attributes (CardAttributes): Additional attributes associated with the
            use of this card.
        vault_id (str): The PayPal-generated ID for the vaulted payment
            source. This ID should be stored on the merchant's server so the
            saved payment source can be used for future transactions.
        single_use_token (str): The PayPal-generated, short-lived,
            one-time-use token, used to communicate payment information to
            PayPal for transaction processing.
        stored_credential (CardStoredCredential): Provides additional details
            to process a payment using a `card` that has been stored or is
            intended to be stored (also referred to as stored_credential or
            card-on-file).<br/>Parameter
            compatibility:<br/><ul><li>`payment_type=ONE_TIME` is compatible
            only with `payment_initiator=CUSTOMER`.</li><li>`usage=FIRST` is
            compatible only with
            `payment_initiator=CUSTOMER`.</li><li>`previous_transaction_referen
            ce` or `previous_network_transaction_reference` is compatible only
            with `payment_initiator=MERCHANT`.</li><li>Only one of the
            parameters - `previous_transaction_reference` and
            `previous_network_transaction_reference` - can be present in the
            request.</li></ul>
        network_token (NetworkToken): The Third Party Network token used to
            fund a payment.
        experience_context (CardExperienceContext): Customizes the payer
            experience during the 3DS Approval for payment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "number": 'number',
        "expiry": 'expiry',
        "security_code": 'security_code',
        "billing_address": 'billing_address',
        "attributes": 'attributes',
        "vault_id": 'vault_id',
        "single_use_token": 'single_use_token',
        "stored_credential": 'stored_credential',
        "network_token": 'network_token',
        "experience_context": 'experience_context'
    }

    _optionals = [
        'name',
        'number',
        'expiry',
        'security_code',
        'billing_address',
        'attributes',
        'vault_id',
        'single_use_token',
        'stored_credential',
        'network_token',
        'experience_context',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 expiry=APIHelper.SKIP,
                 security_code=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 attributes=APIHelper.SKIP,
                 vault_id=APIHelper.SKIP,
                 single_use_token=APIHelper.SKIP,
                 stored_credential=APIHelper.SKIP,
                 network_token=APIHelper.SKIP,
                 experience_context=APIHelper.SKIP):
        """Constructor for the CardRequest class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if number is not APIHelper.SKIP:
            self.number = number 
        if expiry is not APIHelper.SKIP:
            self.expiry = expiry 
        if security_code is not APIHelper.SKIP:
            self.security_code = security_code 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 
        if vault_id is not APIHelper.SKIP:
            self.vault_id = vault_id 
        if single_use_token is not APIHelper.SKIP:
            self.single_use_token = single_use_token 
        if stored_credential is not APIHelper.SKIP:
            self.stored_credential = stored_credential 
        if network_token is not APIHelper.SKIP:
            self.network_token = network_token 
        if experience_context is not APIHelper.SKIP:
            self.experience_context = experience_context 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        expiry = dictionary.get("expiry") if dictionary.get("expiry") else APIHelper.SKIP
        security_code = dictionary.get("security_code") if dictionary.get("security_code") else APIHelper.SKIP
        billing_address = Address.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        attributes = CardAttributes.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        vault_id = dictionary.get("vault_id") if dictionary.get("vault_id") else APIHelper.SKIP
        single_use_token = dictionary.get("single_use_token") if dictionary.get("single_use_token") else APIHelper.SKIP
        stored_credential = CardStoredCredential.from_dictionary(dictionary.get('stored_credential')) if 'stored_credential' in dictionary.keys() else APIHelper.SKIP
        network_token = NetworkToken.from_dictionary(dictionary.get('network_token')) if 'network_token' in dictionary.keys() else APIHelper.SKIP
        experience_context = CardExperienceContext.from_dictionary(dictionary.get('experience_context')) if 'experience_context' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   number,
                   expiry,
                   security_code,
                   billing_address,
                   attributes,
                   vault_id,
                   single_use_token,
                   stored_credential,
                   network_token,
                   experience_context)
