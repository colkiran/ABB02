"""
Marshal is the oldest module, Not recommended to use. Its maily used by the python interpreter
"""
import marshal

data = {'name': 'Mike Tyson', 'age': 56, 'Knockouts': 45, 'country': 'USA'}

print(f"data :{data}")

# dumps - return byte object stored in variable 'byte', this function is used to write the supported type value on the open writable binary file.
print("-" * 60)

bytes = marshal.dumps(data)
print(f"After serialization :{bytes}")

print("-" * 60)
# loads - convert the byte object into values
new_data = marshal.loads(bytes)
print(f"After desirialization :{new_data}")
