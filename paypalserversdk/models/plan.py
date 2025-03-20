# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.billing_cycle import BillingCycle
from paypalserversdk.models.one_time_charge import OneTimeCharge


class Plan(object):

    """Implementation of the 'Plan' model.

    The merchant level Recurring Billing plan metadata for the Billing
    Agreement.

    Attributes:
        billing_cycles (List[BillingCycle]): An array of billing cycles for
            trial billing and regular billing. A plan can have at most two
            trial cycles and only one regular cycle.
        product (object): Product details associated with any one-time product
            purchase.
        one_time_charges (OneTimeCharge): The one-time charge info at the time
            of checkout.
        name (str): Name of the recurring plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "billing_cycles": 'billing_cycles',
        "one_time_charges": 'one_time_charges',
        "product": 'product',
        "name": 'name'
    }

    _optionals = [
        'product',
        'name',
    ]

    def __init__(self,
                 billing_cycles=None,
                 one_time_charges=None,
                 product=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Plan class"""

        # Initialize members of the class
        self.billing_cycles = billing_cycles 
        if product is not APIHelper.SKIP:
            self.product = product 
        self.one_time_charges = one_time_charges 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        billing_cycles = None
        if dictionary.get('billing_cycles') is not None:
            billing_cycles = [BillingCycle.from_dictionary(x) for x in dictionary.get('billing_cycles')]
        one_time_charges = OneTimeCharge.from_dictionary(dictionary.get('one_time_charges')) if dictionary.get('one_time_charges') else None
        product = dictionary.get("product") if dictionary.get("product") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(billing_cycles,
                   one_time_charges,
                   product,
                   name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'billing_cycles={self.billing_cycles!r}, '
                f'product={(self.product if hasattr(self, "product") else None)!r}, '
                f'one_time_charges={self.one_time_charges!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'billing_cycles={self.billing_cycles!s}, '
                f'product={(self.product if hasattr(self, "product") else None)!s}, '
                f'one_time_charges={self.one_time_charges!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s})')
