# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import weatherapi.models.location
import weatherapi.models.current

class CurrentJsonResponse(object):

    """Implementation of the 'CurrentJson Response' model.

    TODO: type model description here.

    Attributes:
        location (Location): TODO: type description here.
        current (Current): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "location":'location',
        "current":'current'
    }

    def __init__(self,
                 location=None,
                 current=None):
        """Constructor for the CurrentJsonResponse class"""

        # Initialize members of the class
        self.location = location
        self.current = current


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        location = weatherapi.models.location.Location.from_dictionary(dictionary.get('location')) if dictionary.get('location') else None
        current = weatherapi.models.current.Current.from_dictionary(dictionary.get('current')) if dictionary.get('current') else None

        # Return an object of this model
        return cls(location,
                   current)


