"""
the pickle module also consists of dumps function that pickles python data to a byte object
"""

from pickle import loads, dumps
dct = {'name': 'Margret', 'age': 32, 'gender': 'female', 'city': 'las vegas'}
print(f"dictionary :{dct}")

print("-" * 60)
dictstring = dumps(dct)          # pickles to bytes
print(dictstring)
print(type(dictstring))

print("-" * 60)
# unpickle the byte object to obtain the original dictionary object
dictObj = loads(dictstring)
print(dictObj)
