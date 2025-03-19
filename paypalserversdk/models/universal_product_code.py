# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UniversalProductCode(object):

    """Implementation of the 'Universal Product Code' model.

    The Universal Product Code of the item.

    Attributes:
        mtype (UpcType): The Universal Product Code type.
        code (str): The UPC product code of the item.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "code": 'code'
    }

    def __init__(self,
                 mtype=None,
                 code=None):
        """Constructor for the UniversalProductCode class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.code = code 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        code = dictionary.get("code") if dictionary.get("code") else None
        # Return an object of this model
        return cls(mtype,
                   code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!r}, '
                f'code={self.code!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!s}, '
                f'code={self.code!s})')
