# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class VaultResponseCustomer(object):

    """Implementation of the 'Vault Response Customer' model.

    This object defines a customer in your system. Use it to manage customer
    profiles, save payment methods and contact details.

    Attributes:
        id (str): The unique ID for a customer generated by PayPal.
        merchant_customer_id (str): Merchants and partners may already have a
            data-store where their customer information is persisted. Use
            merchant_customer_id to associate the PayPal-generated customer.id
            to your representation of a customer.
        links (List[object]): An array of request-related HATEOAS links.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "merchant_customer_id": 'merchant_customer_id',
        "links": 'links'
    }

    _optionals = [
        'id',
        'merchant_customer_id',
        'links',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 merchant_customer_id=APIHelper.SKIP,
                 links=APIHelper.SKIP):
        """Constructor for the VaultResponseCustomer class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if merchant_customer_id is not APIHelper.SKIP:
            self.merchant_customer_id = merchant_customer_id 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        merchant_customer_id = dictionary.get("merchant_customer_id") if dictionary.get("merchant_customer_id") else APIHelper.SKIP
        links = dictionary.get("links") if dictionary.get("links") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   merchant_customer_id,
                   links)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'merchant_customer_id={(self.merchant_customer_id if hasattr(self, "merchant_customer_id") else None)!r}, '
                f'links={(self.links if hasattr(self, "links") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'merchant_customer_id={(self.merchant_customer_id if hasattr(self, "merchant_customer_id") else None)!s}, '
                f'links={(self.links if hasattr(self, "links") else None)!s})')
