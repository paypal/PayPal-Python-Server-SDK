# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.link_description import LinkDescription


class ErrorDetails(object):

    """Implementation of the 'Error Details' model.

    The error details. Required for client-side `4XX` errors.

    Attributes:
        field (str): The field that caused the error. If this field is in the
            body, set this value to the field's JSON pointer value. Required
            for client-side errors.
        value (str): The value of the field that caused the error.
        location (str): The location of the field that caused the error. Value
            is `body`, `path`, or `query`.
        issue (str): The unique, fine-grained application-level error code.
        links (List[LinkDescription]): An array of request-related [HATEOAS
            links](/api/rest/responses/#hateoas-links) that are either
            relevant to the issue by providing additional information or
            offering potential resolutions.
        description (str): The human-readable description for an issue. The
            description can change over the lifetime of an API, so clients
            must not depend on this value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "issue": 'issue',
        "field": 'field',
        "value": 'value',
        "location": 'location',
        "links": 'links',
        "description": 'description'
    }

    _optionals = [
        'field',
        'value',
        'location',
        'links',
        'description',
    ]

    def __init__(self,
                 issue=None,
                 field=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 location='body',
                 links=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the ErrorDetails class"""

        # Initialize members of the class
        if field is not APIHelper.SKIP:
            self.field = field 
        if value is not APIHelper.SKIP:
            self.value = value 
        self.location = location 
        self.issue = issue 
        if links is not APIHelper.SKIP:
            self.links = links 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        issue = dictionary.get("issue") if dictionary.get("issue") else None
        field = dictionary.get("field") if dictionary.get("field") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        location = dictionary.get("location") if dictionary.get("location") else 'body'
        links = None
        if dictionary.get('links') is not None:
            links = [LinkDescription.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        # Return an object of this model
        return cls(issue,
                   field,
                   value,
                   location,
                   links,
                   description)
