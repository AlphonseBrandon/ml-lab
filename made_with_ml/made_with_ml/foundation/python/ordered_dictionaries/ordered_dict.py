"""
Turnin unordered dictionaries to ordered using OrderDict
"""
from collections import OrderedDict

# Native dictionary
d = {}
d['a'] = 2
d['c'] = 3
d['b'] = 1

print("Native Dictionary\n",d)

# Dictionary Items
print("Dictionary Items\n", d.items())

# Ordered by keys
print("Ordere by key\n",OrderedDict(sorted(d.items())))

# Ordere by values
print("Ordere by values\n",OrderedDict(sorted(d.items(), key=lambda x: x[1])))
