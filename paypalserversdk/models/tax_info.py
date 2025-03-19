# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TaxInfo(object):

    """Implementation of the 'Tax Info' model.

    The tax ID of the customer. The customer is also known as the payer. Both
    `tax_id` and `tax_id_type` are required.

    Attributes:
        tax_id (str): The customer's tax ID value.
        tax_id_type (TaxIdType): The customer's tax ID type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_id": 'tax_id',
        "tax_id_type": 'tax_id_type'
    }

    def __init__(self,
                 tax_id=None,
                 tax_id_type=None):
        """Constructor for the TaxInfo class"""

        # Initialize members of the class
        self.tax_id = tax_id 
        self.tax_id_type = tax_id_type 

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
        tax_id = dictionary.get("tax_id") if dictionary.get("tax_id") else None
        tax_id_type = dictionary.get("tax_id_type") if dictionary.get("tax_id_type") else None
        # Return an object of this model
        return cls(tax_id,
                   tax_id_type)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tax_id={self.tax_id!r}, '
                f'tax_id_type={self.tax_id_type!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax_id={self.tax_id!s}, '
                f'tax_id_type={self.tax_id_type!s})')
