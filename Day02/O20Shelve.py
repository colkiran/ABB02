"""
shelve
------
A shelve is a persistant dictionary like object

-> shelve in python standard library is a simple yet effective tool for persistant data storage when you don't really need a relational database solution.

-> the 'shelf' object defined in this module is a dictionary like object which is persistently stored  in a disk file.

-> this creates a file similar to dbm database on UNIX systems

-> however, objects of only string type is allowed as key in this special dictionary object

value however can be any picklable object

The shelve module defines three classses as follows

Shelf    :  This is the base class for shelf implementation
            It is initialized with dict-like object

BsdDbsShelf : This is a subclass of shelf class.
              The dict object passed to its constructor must support
              first(), next(), previous(), last() and set_location() methods.

DbfilenameShelf : this is also a subclass of Shelf but accepts a filename as parameter to its constructpr rather than the dict object.

The shelf object has the following methods

close()         : Synchronise and close persistent dict objects
sync()          : Write back all entries in the cache of shelf was opened with writeback set to true
get()           : returns value associated with key
items()         : list of tuples - each tuple is a key value pair
keys()          : list of shelf keys
pop()           : Remove specified key and returns the corresponding                    value
update()        : update shelf from another dict / iterable
values()        : list of shelf values
"""

import shelve

s1 = shelve.open("hello")       # creates a file
s1['name'] = 'Kevin'
s1['age'] = 32
s1['city'] = "Newyork"
s1.close()

print("-" * 60)
# read the data from the file
s2 = shelve.open("hello")
print("Name :", s2['name'])
print("Age :", s2['age'])
print("City :", s2['city'])

print("-" * 60)
print(list(s2.items()))
print(list(s2.keys()))
print(list(s2.values()))

print("-" * 60)
print("get :", s2.get('name'))
dict1 = {'name': 'John', 'salary': 65000, 'age': 38, 'desig': 'MGR'}
print(f"dict1 :{dict1}")
s2.update(dict1)

print("-" * 60)
print(list(s2.items()))
res = s2.pop('age')
print(f"res :{res}")

print(list(s2.items()))
