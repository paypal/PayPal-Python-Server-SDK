# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.address import Address
from paypalrestapis.models.name import Name
from paypalrestapis.models.pay_pal_wallet_attributes_response import PayPalWalletAttributesResponse
from paypalrestapis.models.phone_number import PhoneNumber
from paypalrestapis.models.tax_info import TaxInfo


class PayPalWalletResponse(object):

    """Implementation of the 'PayPal Wallet Response' model.

    The PayPal Wallet response.

    Attributes:
        email_address (str): The internationalized email
            address.<blockquote><strong>Note:</strong> Up to 64 characters are
            allowed before and 255 characters are allowed after the
            <code>@</code> sign. However, the generally accepted maximum
            length for an email address is 254 characters. The pattern
            verifies that an unquoted <code>@</code> sign
            exists.</blockquote>
        account_id (str): The PayPal payer ID, which is a masked version of
            the PayPal account number intended for use with third parties. The
            account number is reversibly encrypted and a proprietary variant
            of Base32 is used to encode the result.
        account_status (PayPalWalletAccountVerificationStatus): The account
            status indicates whether the buyer has verified the financial
            details associated with their PayPal account.
        name (Name): The name of the party.
        phone_type (PhoneType): The phone type.
        phone_number (PhoneNumber): The phone number in its canonical
            international [E.164 numbering plan
            format](https://www.itu.int/rec/T-REC-E.164/en).
        birth_date (str): The stand-alone date, in [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6). To
            represent special legal values, such as a date of birth, you
            should use dates with no associated time or time-zone data.
            Whenever possible, use the standard `date_time` type. This regular
            expression does not validate all dates. For example, February 31
            is valid and nothing is known about leap years.
        business_name (str): The business name of the PayPal account holder
            (populated for business accounts only)
        tax_info (TaxInfo): The tax ID of the customer. The customer is also
            known as the payer. Both `tax_id` and `tax_id_type` are required.
        address (Address): The portable international postal address. Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).
        attributes (PayPalWalletAttributesResponse): Additional attributes
            associated with the use of a PayPal Wallet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address": 'email_address',
        "account_id": 'account_id',
        "account_status": 'account_status',
        "name": 'name',
        "phone_type": 'phone_type',
        "phone_number": 'phone_number',
        "birth_date": 'birth_date',
        "business_name": 'business_name',
        "tax_info": 'tax_info',
        "address": 'address',
        "attributes": 'attributes'
    }

    _optionals = [
        'email_address',
        'account_id',
        'account_status',
        'name',
        'phone_type',
        'phone_number',
        'birth_date',
        'business_name',
        'tax_info',
        'address',
        'attributes',
    ]

    def __init__(self,
                 email_address=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_status=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 phone_type=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 birth_date=APIHelper.SKIP,
                 business_name=APIHelper.SKIP,
                 tax_info=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 attributes=APIHelper.SKIP):
        """Constructor for the PayPalWalletResponse class"""

        # Initialize members of the class
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_status is not APIHelper.SKIP:
            self.account_status = account_status 
        if name is not APIHelper.SKIP:
            self.name = name 
        if phone_type is not APIHelper.SKIP:
            self.phone_type = phone_type 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if birth_date is not APIHelper.SKIP:
            self.birth_date = birth_date 
        if business_name is not APIHelper.SKIP:
            self.business_name = business_name 
        if tax_info is not APIHelper.SKIP:
            self.tax_info = tax_info 
        if address is not APIHelper.SKIP:
            self.address = address 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 

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
        email_address = dictionary.get("email_address") if dictionary.get("email_address") else APIHelper.SKIP
        account_id = dictionary.get("account_id") if dictionary.get("account_id") else APIHelper.SKIP
        account_status = dictionary.get("account_status") if dictionary.get("account_status") else APIHelper.SKIP
        name = Name.from_dictionary(dictionary.get('name')) if 'name' in dictionary.keys() else APIHelper.SKIP
        phone_type = dictionary.get("phone_type") if dictionary.get("phone_type") else APIHelper.SKIP
        phone_number = PhoneNumber.from_dictionary(dictionary.get('phone_number')) if 'phone_number' in dictionary.keys() else APIHelper.SKIP
        birth_date = dictionary.get("birth_date") if dictionary.get("birth_date") else APIHelper.SKIP
        business_name = dictionary.get("business_name") if dictionary.get("business_name") else APIHelper.SKIP
        tax_info = TaxInfo.from_dictionary(dictionary.get('tax_info')) if 'tax_info' in dictionary.keys() else APIHelper.SKIP
        address = Address.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        attributes = PayPalWalletAttributesResponse.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(email_address,
                   account_id,
                   account_status,
                   name,
                   phone_type,
                   phone_number,
                   birth_date,
                   business_name,
                   tax_info,
                   address,
                   attributes)
