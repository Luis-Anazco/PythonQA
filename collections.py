dict1 = {1:'Hello', 2:'Bye', 3:'Perhaps'}

print(dict1)

dict1.pop(1)
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

for key, value in dict1.items():
    print(f'Key: {key}, Value: {value}')

tup1 = 'dog', 'cat', 'turtle'
ani1, ani2, ani3 = tup1
print(ani1)

list = ['john', 'mark', 'john', 'james']
set = set(list)
print(set)