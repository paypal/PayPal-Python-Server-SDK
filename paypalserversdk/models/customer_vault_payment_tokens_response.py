# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.payment_token_response import PaymentTokenResponse
from paypalserversdk.models.vault_response_customer import VaultResponseCustomer


class CustomerVaultPaymentTokensResponse(object):

    """Implementation of the 'Customer Vault Payment Tokens Response' model.

    Collection of payment tokens saved for a given customer.

    Attributes:
        total_items (int): Total number of items.
        total_pages (int): Total number of pages.
        customer (VaultResponseCustomer): This object defines a customer in
            your system. Use it to manage customer profiles, save payment
            methods and contact details.
        payment_tokens (List[PaymentTokenResponse]): The model property of
            type List[PaymentTokenResponse].
        links (List[LinkDescription]): An array of related [HATEOAS
            links](/api/rest/responses/#hateoas).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_items": 'total_items',
        "total_pages": 'total_pages',
        "customer": 'customer',
        "payment_tokens": 'payment_tokens',
        "links": 'links'
    }

    _optionals = [
        'total_items',
        'total_pages',
        'customer',
        'payment_tokens',
        'links',
    ]

    def __init__(self,
                 total_items=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 payment_tokens=APIHelper.SKIP,
                 links=APIHelper.SKIP):
        """Constructor for the CustomerVaultPaymentTokensResponse class"""

        # Initialize members of the class
        if total_items is not APIHelper.SKIP:
            self.total_items = total_items 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if payment_tokens is not APIHelper.SKIP:
            self.payment_tokens = payment_tokens 
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        total_items = dictionary.get("total_items") if dictionary.get("total_items") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        customer = VaultResponseCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        payment_tokens = None
        if dictionary.get('payment_tokens') is not None:
            payment_tokens = [PaymentTokenResponse.from_dictionary(x) for x in dictionary.get('payment_tokens')]
        else:
            payment_tokens = APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [LinkDescription.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        # Return an object of this model
        return cls(total_items,
                   total_pages,
                   customer,
                   payment_tokens,
                   links)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'total_items={(self.total_items if hasattr(self, "total_items") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!r}, '
                f'payment_tokens={(self.payment_tokens if hasattr(self, "payment_tokens") else None)!r}, '
                f'links={(self.links if hasattr(self, "links") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'total_items={(self.total_items if hasattr(self, "total_items") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!s}, '
                f'payment_tokens={(self.payment_tokens if hasattr(self, "payment_tokens") else None)!s}, '
                f'links={(self.links if hasattr(self, "links") else None)!s})')
