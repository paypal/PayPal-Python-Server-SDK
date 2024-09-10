# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.vault_customer import VaultCustomer


class VaultResponse(object):

    """Implementation of the 'Vault Response' model.

    The details about a saved payment source.

    Attributes:
        id (str): The PayPal-generated ID for the saved payment source.
        status (VaultStatus): The vault status.
        customer (VaultCustomer): The details about a customer in PayPal's
            system of record.
        links (List[LinkDescription]): An array of request-related HATEOAS
            links.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "status": 'status',
        "customer": 'customer',
        "links": 'links'
    }

    _optionals = [
        'id',
        'status',
        'customer',
        'links',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 links=APIHelper.SKIP):
        """Constructor for the VaultResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        customer = VaultCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [LinkDescription.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   status,
                   customer,
                   links)
