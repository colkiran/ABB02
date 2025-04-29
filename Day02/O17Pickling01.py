
"""
Pickle Module :
1. it serializes the python object into binary format
2. its faster and it also works with custom defined objects
3. Better choice for serialization and deserialization of python objects
"""

import pickle

data = {'name': 'Peter', 'age': 55, 'city': 'California', 'Country' :'India', 'Qlf': 'Btech'}
print(f"data :{data}")

with open("data.pickle", "wb") as f1:
    pickle.dump(data, f1)
    print("Pickling completed.....")

with open("data.pickle", "rb") as f2:
    print('-' * 60)
    print("unpickling the data")
    data = pickle.load(f2)
    print(data)
    







