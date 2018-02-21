#Написать программу, которая берет словарь и меняет местами ключи и значения.

import pprint
dictionary = dict(key1='value1', key2='value2')
print ('Before revert:')
pprint.pprint (dictionary, width=30)

# Создаем список ключей
keys = list()
for i in dictionary.keys():
    keys.append(i)

# Меняем местами ключ и значие
j = 0
while j != len(keys):
    #value = dictionary.get (keys[j])
    dictionary.update ({dictionary.get (keys[j]) : keys[j]})
    dictionary.pop (keys[j])
    #print (value)
    j = j + 1

print ('After revert:')
pprint.pprint (dictionary, width=30)
