# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PhoneNumber(object):

    """Implementation of the 'Phone Number' model.

    The phone number in its canonical international [E.164 numbering plan
    format](https://www.itu.int/rec/T-REC-E.164/en).

    Attributes:
        national_number (str): The national number, in its canonical
            international [E.164 numbering plan
            format](https://www.itu.int/rec/T-REC-E.164/en). The combined
            length of the country calling code (CC) and the national number
            must not be greater than 15 digits. The national number consists
            of a national destination code (NDC) and subscriber number (SN).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "national_number": 'national_number'
    }

    def __init__(self,
                 national_number=None):
        """Constructor for the PhoneNumber class"""

        # Initialize members of the class
        self.national_number = national_number 

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
        national_number = dictionary.get("national_number") if dictionary.get("national_number") else None
        # Return an object of this model
        return cls(national_number)
