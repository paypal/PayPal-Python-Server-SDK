# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.address import Address
from paypalserversdk.models.authentication_response import AuthenticationResponse


class GooglePayCardResponse(object):

    """Implementation of the 'Google Pay Card Response' model.

    The payment card to use to fund a Google Pay payment response. Can be a
    credit or debit card.

    Attributes:
        name (str): The card holder's name as it appears on the card.
        last_digits (str): The last digits of the payment card.
        mtype (CardType): Type of card. i.e Credit, Debit and so on.
        brand (CardBrand): The card network or brand. Applies to credit,
            debit, gift, and payment cards.
        billing_address (Address): The portable international postal address.
            Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).
        authentication_result (AuthenticationResponse): Results of
            Authentication such as 3D Secure.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "last_digits": 'last_digits',
        "mtype": 'type',
        "brand": 'brand',
        "billing_address": 'billing_address',
        "authentication_result": 'authentication_result'
    }

    _optionals = [
        'name',
        'last_digits',
        'mtype',
        'brand',
        'billing_address',
        'authentication_result',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 last_digits=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 brand=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 authentication_result=APIHelper.SKIP):
        """Constructor for the GooglePayCardResponse class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if last_digits is not APIHelper.SKIP:
            self.last_digits = last_digits 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if brand is not APIHelper.SKIP:
            self.brand = brand 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if authentication_result is not APIHelper.SKIP:
            self.authentication_result = authentication_result 

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
        last_digits = dictionary.get("last_digits") if dictionary.get("last_digits") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        brand = dictionary.get("brand") if dictionary.get("brand") else APIHelper.SKIP
        billing_address = Address.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        authentication_result = AuthenticationResponse.from_dictionary(dictionary.get('authentication_result')) if 'authentication_result' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   last_digits,
                   mtype,
                   brand,
                   billing_address,
                   authentication_result)
