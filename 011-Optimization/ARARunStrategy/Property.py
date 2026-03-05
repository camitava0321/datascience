# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:28:46 2024

@author: AMITAVA
"""

import random
import string

#Represents a property with property_code, num_rooms, and timezone.
class Property:
    def __init__(self, property_code, num_rooms, timezone, allowedTimezones):
        self.property_code = property_code
        self.num_rooms = num_rooms
        self.timezone = timezone
        self.allowedTimezones = allowedTimezones

    def __repr__(self):
        return f"Property(code={self.property_code}, \
            rooms={self.num_rooms}, timezone={self.timezone},\
                allowedTimezones={self.allowedTimezones})"

# Function : generatProperties
# Creates a Property object with the following fields and appends it to the list of properties.
# Takes N as input, the number of properties to generate, with
# a random 5-letter uppercase property code, 
# a random number of rooms between 100 and 1000.
# a random timezone between 0 and 24.
def generate_properties(N):
    properties = []
    for _ in range(N):
        property_code = ''.join(random.choices(string.ascii_uppercase, k=5))
        num_rooms = random.randint(100, 1000)
        timezone = random.randint(0, 23)
        allowedTimezone1 = (timezone-1) if (timezone-1)>=0 else 23
        allowedTimezone2 = (timezone+1) if (timezone+1)<24 else 0
        allowedTimezones = [allowedTimezone1, timezone, allowedTimezone2]
        property_obj = Property(property_code, num_rooms, timezone, allowedTimezones)
        properties.append(property_obj)
    return properties

# Example usage
#N = 10  # Change this value to generate a different number of properties
#properties = generate_properties(N)
#for prop in properties:
#    print(prop)