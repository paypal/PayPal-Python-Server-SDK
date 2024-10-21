# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.experience_context import ExperienceContext


class P24PaymentRequest(object):

    """Implementation of the 'P24 Payment Request' model.

    Information needed to pay using P24 (Przelewy24).

    Attributes:
        name (str): The full name representation like Mr J Smith.
        email (str): The internationalized email
            address.<blockquote><strong>Note:</strong> Up to 64 characters are
            allowed before and 255 characters are allowed after the
            <code>@</code> sign. However, the generally accepted maximum
            length for an email address is 254 characters. The pattern
            verifies that an unquoted <code>@</code> sign exists.</blockquote>
        country_code (str): The [two-character ISO 3166-1
            code](/api/rest/reference/country-codes/) that identifies the
            country or region.<blockquote><strong>Note:</strong> The country
            code for Great Britain is <code>GB</code> and not <code>UK</code>
            as used in the top-level domain names for that country. Use the
            `C2` country code for China worldwide for comparable uncontrolled
            price (CUP) method, bank card, and cross-border
            transactions.</blockquote>
        experience_context (ExperienceContext): Customizes the payer
            experience during the approval process for the payment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email": 'email',
        "country_code": 'country_code',
        "experience_context": 'experience_context'
    }

    _optionals = [
        'experience_context',
    ]

    def __init__(self,
                 name=None,
                 email=None,
                 country_code=None,
                 experience_context=APIHelper.SKIP):
        """Constructor for the P24PaymentRequest class"""

        # Initialize members of the class
        self.name = name 
        self.email = email 
        self.country_code = country_code 
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
        name = dictionary.get("name") if dictionary.get("name") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        country_code = dictionary.get("country_code") if dictionary.get("country_code") else None
        experience_context = ExperienceContext.from_dictionary(dictionary.get('experience_context')) if 'experience_context' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email,
                   country_code,
                   experience_context)
