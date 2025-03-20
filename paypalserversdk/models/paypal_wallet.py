# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.address import Address
from paypalserversdk.models.name import Name
from paypalserversdk.models.paypal_wallet_attributes import PaypalWalletAttributes
from paypalserversdk.models.paypal_wallet_experience_context import PaypalWalletExperienceContext
from paypalserversdk.models.paypal_wallet_stored_credential import PaypalWalletStoredCredential
from paypalserversdk.models.phone_with_type import PhoneWithType
from paypalserversdk.models.tax_info import TaxInfo


class PaypalWallet(object):

    """Implementation of the 'PayPal Wallet' model.

    A resource that identifies a PayPal Wallet is used for payment.

    Attributes:
        vault_id (str): The PayPal-generated ID for the vaulted payment
            source. This ID should be stored on the merchant's server so the
            saved payment source can be used for future transactions.
        email_address (str): The internationalized email address. Note: Up to
            64 characters are allowed before and 255 characters are allowed
            after the @ sign. However, the generally accepted maximum length
            for an email address is 254 characters. The pattern verifies that
            an unquoted @ sign exists.
        name (Name): The name of the party.
        phone (PhoneWithType): The phone information.
        birth_date (str): The stand-alone date, in [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6). To
            represent special legal values, such as a date of birth, you
            should use dates with no associated time or time-zone data.
            Whenever possible, use the standard `date_time` type. This regular
            expression does not validate all dates. For example, February 31
            is valid and nothing is known about leap years.
        tax_info (TaxInfo): The tax ID of the customer. The customer is also
            known as the payer. Both `tax_id` and `tax_id_type` are required.
        address (Address): The portable international postal address. Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).
        attributes (PaypalWalletAttributes): Additional attributes associated
            with the use of this PayPal Wallet.
        experience_context (PaypalWalletExperienceContext): Customizes the
            payer experience during the approval process for payment with
            PayPal. Note: Partners and Marketplaces might configure brand_name
            and shipping_preference during partner account setup, which
            overrides the request values.
        billing_agreement_id (str): The PayPal billing agreement ID.
            References an approved recurring payment for goods or services.
        stored_credential (PaypalWalletStoredCredential): Provides additional
            details to process a payment using the PayPal wallet billing
            agreement or a vaulted payment method that has been stored or is
            intended to be stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault_id": 'vault_id',
        "email_address": 'email_address',
        "name": 'name',
        "phone": 'phone',
        "birth_date": 'birth_date',
        "tax_info": 'tax_info',
        "address": 'address',
        "attributes": 'attributes',
        "experience_context": 'experience_context',
        "billing_agreement_id": 'billing_agreement_id',
        "stored_credential": 'stored_credential'
    }

    _optionals = [
        'vault_id',
        'email_address',
        'name',
        'phone',
        'birth_date',
        'tax_info',
        'address',
        'attributes',
        'experience_context',
        'billing_agreement_id',
        'stored_credential',
    ]

    def __init__(self,
                 vault_id=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 birth_date=APIHelper.SKIP,
                 tax_info=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 attributes=APIHelper.SKIP,
                 experience_context=APIHelper.SKIP,
                 billing_agreement_id=APIHelper.SKIP,
                 stored_credential=APIHelper.SKIP):
        """Constructor for the PaypalWallet class"""

        # Initialize members of the class
        if vault_id is not APIHelper.SKIP:
            self.vault_id = vault_id 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if name is not APIHelper.SKIP:
            self.name = name 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if birth_date is not APIHelper.SKIP:
            self.birth_date = birth_date 
        if tax_info is not APIHelper.SKIP:
            self.tax_info = tax_info 
        if address is not APIHelper.SKIP:
            self.address = address 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 
        if experience_context is not APIHelper.SKIP:
            self.experience_context = experience_context 
        if billing_agreement_id is not APIHelper.SKIP:
            self.billing_agreement_id = billing_agreement_id 
        if stored_credential is not APIHelper.SKIP:
            self.stored_credential = stored_credential 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        vault_id = dictionary.get("vault_id") if dictionary.get("vault_id") else APIHelper.SKIP
        email_address = dictionary.get("email_address") if dictionary.get("email_address") else APIHelper.SKIP
        name = Name.from_dictionary(dictionary.get('name')) if 'name' in dictionary.keys() else APIHelper.SKIP
        phone = PhoneWithType.from_dictionary(dictionary.get('phone')) if 'phone' in dictionary.keys() else APIHelper.SKIP
        birth_date = dictionary.get("birth_date") if dictionary.get("birth_date") else APIHelper.SKIP
        tax_info = TaxInfo.from_dictionary(dictionary.get('tax_info')) if 'tax_info' in dictionary.keys() else APIHelper.SKIP
        address = Address.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        attributes = PaypalWalletAttributes.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        experience_context = PaypalWalletExperienceContext.from_dictionary(dictionary.get('experience_context')) if 'experience_context' in dictionary.keys() else APIHelper.SKIP
        billing_agreement_id = dictionary.get("billing_agreement_id") if dictionary.get("billing_agreement_id") else APIHelper.SKIP
        stored_credential = PaypalWalletStoredCredential.from_dictionary(dictionary.get('stored_credential')) if 'stored_credential' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(vault_id,
                   email_address,
                   name,
                   phone,
                   birth_date,
                   tax_info,
                   address,
                   attributes,
                   experience_context,
                   billing_agreement_id,
                   stored_credential)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'vault_id={(self.vault_id if hasattr(self, "vault_id") else None)!r}, '
                f'email_address={(self.email_address if hasattr(self, "email_address") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!r}, '
                f'birth_date={(self.birth_date if hasattr(self, "birth_date") else None)!r}, '
                f'tax_info={(self.tax_info if hasattr(self, "tax_info") else None)!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r}, '
                f'attributes={(self.attributes if hasattr(self, "attributes") else None)!r}, '
                f'experience_context={(self.experience_context if hasattr(self, "experience_context") else None)!r}, '
                f'billing_agreement_id={(self.billing_agreement_id if hasattr(self, "billing_agreement_id") else None)!r}, '
                f'stored_credential={(self.stored_credential if hasattr(self, "stored_credential") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'vault_id={(self.vault_id if hasattr(self, "vault_id") else None)!s}, '
                f'email_address={(self.email_address if hasattr(self, "email_address") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!s}, '
                f'birth_date={(self.birth_date if hasattr(self, "birth_date") else None)!s}, '
                f'tax_info={(self.tax_info if hasattr(self, "tax_info") else None)!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s}, '
                f'attributes={(self.attributes if hasattr(self, "attributes") else None)!s}, '
                f'experience_context={(self.experience_context if hasattr(self, "experience_context") else None)!s}, '
                f'billing_agreement_id={(self.billing_agreement_id if hasattr(self, "billing_agreement_id") else None)!s}, '
                f'stored_credential={(self.stored_credential if hasattr(self, "stored_credential") else None)!s})')
