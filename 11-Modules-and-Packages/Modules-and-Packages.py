# Code 1
# Create an example dictionary
periodic_table = {'Hydrogen': 1, 'Helium': 2}

# Assigning a new key to the dictionary
carbon = periodic_table.setdefault('Carbon', 12)
periodic_table

# Code 2
helium = periodic_table.setdefault('Helium', 100)
periodic_table

# Code 3
from collections import defaultdict

# Attempting to call lead
periodic_table = defaultdict(int)
periodic_table['Lead']

# Showing that we have created Lead in our dictionary
periodic_table

# Code 4
from collections import Counter

# Define an example list
breakfast = ['porridge', 'jam', 'cereal', 'porridge', 'porridge', 'muffin', 'jam']

# Creating a counter
breakfast_counter = Counter(breakfast)
breakfast_counter