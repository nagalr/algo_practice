

dict = {'aaa': 'bbb', 'ccc': 'ddd'}

# extract keys, values of dict
keys = list(dict.keys())
values = list(dict.values())

# find the key that its value is 'bar'
a = keys[values.index('ddd')]

# print all
print(keys)
print(values)

print('the key of ddd is: ' + str(a))
