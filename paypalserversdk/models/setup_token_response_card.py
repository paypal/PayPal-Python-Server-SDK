# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.bin_details import BinDetails
from paypalserversdk.models.card_authentication_response import CardAuthenticationResponse
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.card_verification_details import CardVerificationDetails
from paypalserversdk.models.network_transaction_reference_entity import NetworkTransactionReferenceEntity


class SetupTokenResponseCard(object):

    """Implementation of the 'Setup Token Response Card' model.

    Attributes:
        name (str): The card holder's name as it appears on the card.
        last_digits (str): The last digits of the payment card.
        brand (CardBrand): The card network or brand. Applies to credit,
            debit, gift, and payment cards.
        expiry (str): The year and month, in ISO-8601 `YYYY-MM` date format.
            See [Internet date and time
            format](https://tools.ietf.org/html/rfc3339#section-5.6).
        billing_address (CardResponseAddress): Address request details.
        verification_status (CardVerificationStatus): Verification status of
            Card.
        verification (CardVerificationDetails): Card Verification details
            including the authorization details and 3D SECURE details.
        network_transaction_reference (NetworkTransactionReferenceEntity):
            Previous network transaction reference including id in response.
        authentication_result (CardAuthenticationResponse): Results of
            Authentication such as 3D Secure.
        bin_details (BinDetails): Bank Identification Number (BIN) details
            used to fund a payment.
        mtype (CardType): Type of card. i.e Credit, Debit and so on.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "last_digits": 'last_digits',
        "brand": 'brand',
        "expiry": 'expiry',
        "billing_address": 'billing_address',
        "verification_status": 'verification_status',
        "verification": 'verification',
        "network_transaction_reference": 'network_transaction_reference',
        "authentication_result": 'authentication_result',
        "bin_details": 'bin_details',
        "mtype": 'type'
    }

    _optionals = [
        'name',
        'last_digits',
        'brand',
        'expiry',
        'billing_address',
        'verification_status',
        'verification',
        'network_transaction_reference',
        'authentication_result',
        'bin_details',
        'mtype',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 last_digits=APIHelper.SKIP,
                 brand=APIHelper.SKIP,
                 expiry=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 verification_status=APIHelper.SKIP,
                 verification=APIHelper.SKIP,
                 network_transaction_reference=APIHelper.SKIP,
                 authentication_result=APIHelper.SKIP,
                 bin_details=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the SetupTokenResponseCard class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if last_digits is not APIHelper.SKIP:
            self.last_digits = last_digits 
        if brand is not APIHelper.SKIP:
            self.brand = brand 
        if expiry is not APIHelper.SKIP:
            self.expiry = expiry 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if verification_status is not APIHelper.SKIP:
            self.verification_status = verification_status 
        if verification is not APIHelper.SKIP:
            self.verification = verification 
        if network_transaction_reference is not APIHelper.SKIP:
            self.network_transaction_reference = network_transaction_reference 
        if authentication_result is not APIHelper.SKIP:
            self.authentication_result = authentication_result 
        if bin_details is not APIHelper.SKIP:
            self.bin_details = bin_details 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        last_digits = dictionary.get("last_digits") if dictionary.get("last_digits") else APIHelper.SKIP
        brand = dictionary.get("brand") if dictionary.get("brand") else APIHelper.SKIP
        expiry = dictionary.get("expiry") if dictionary.get("expiry") else APIHelper.SKIP
        billing_address = CardResponseAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        verification_status = dictionary.get("verification_status") if dictionary.get("verification_status") else APIHelper.SKIP
        verification = CardVerificationDetails.from_dictionary(dictionary.get('verification')) if 'verification' in dictionary.keys() else APIHelper.SKIP
        network_transaction_reference = NetworkTransactionReferenceEntity.from_dictionary(dictionary.get('network_transaction_reference')) if 'network_transaction_reference' in dictionary.keys() else APIHelper.SKIP
        authentication_result = CardAuthenticationResponse.from_dictionary(dictionary.get('authentication_result')) if 'authentication_result' in dictionary.keys() else APIHelper.SKIP
        bin_details = BinDetails.from_dictionary(dictionary.get('bin_details')) if 'bin_details' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   last_digits,
                   brand,
                   expiry,
                   billing_address,
                   verification_status,
                   verification,
                   network_transaction_reference,
                   authentication_result,
                   bin_details,
                   mtype)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'last_digits={(self.last_digits if hasattr(self, "last_digits") else None)!r}, '
                f'brand={(self.brand if hasattr(self, "brand") else None)!r}, '
                f'expiry={(self.expiry if hasattr(self, "expiry") else None)!r}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!r}, '
                f'verification_status={(self.verification_status if hasattr(self, "verification_status") else None)!r}, '
                f'verification={(self.verification if hasattr(self, "verification") else None)!r}, '
                f'network_transaction_reference={(self.network_transaction_reference if hasattr(self, "network_transaction_reference") else None)!r}, '
                f'authentication_result={(self.authentication_result if hasattr(self, "authentication_result") else None)!r}, '
                f'bin_details={(self.bin_details if hasattr(self, "bin_details") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'last_digits={(self.last_digits if hasattr(self, "last_digits") else None)!s}, '
                f'brand={(self.brand if hasattr(self, "brand") else None)!s}, '
                f'expiry={(self.expiry if hasattr(self, "expiry") else None)!s}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!s}, '
                f'verification_status={(self.verification_status if hasattr(self, "verification_status") else None)!s}, '
                f'verification={(self.verification if hasattr(self, "verification") else None)!s}, '
                f'network_transaction_reference={(self.network_transaction_reference if hasattr(self, "network_transaction_reference") else None)!s}, '
                f'authentication_result={(self.authentication_result if hasattr(self, "authentication_result") else None)!s}, '
                f'bin_details={(self.bin_details if hasattr(self, "bin_details") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s})')
