my_list = [112,1223,334,784,765,456,4567,76,]
print(my_list)
print(my_list[2])
print(my_list[7])
print(my_list[3:7])

my_list[2] = 520
print(my_list)
my_list[5] = 17
print(my_list)
my_list.append(56789)
print(my_list)
my_list.insert(3,56)
print(my_list)
my_list.insert(7,47)
print(my_list)
my_list.extend([77,88,4567])
print(my_list)
my_list.remove(112)
print(my_list)
del my_list[2]
print(my_list)
my_list.clear()
print(my_list)
my_list.insert(0,3456)
print(my_list)
my_list.extend([34,2345,3678765,5678765,78,76])
print(my_list)
del my_list

my_list2 = [23,234,234,2345,345,2345,8,7654,56,765,43,45,67,65,4,34]
print(my_list2)
my_list2.insert(0,45) #adds according to te index indicated
print(my_list2)
my_list2.append(454738) #adds to the end of the list
print(my_list2)
if 234 in my_list2:
    print('The value is in the list')
else:
    print('The value is not found')

my_list3 = [34,4341,94,72,2225,226,4341,72,8332,94]
print(my_list3.count(72))
print(max(my_list3))
print(min(my_list3))
print(sum(my_list3))
print(len(my_list3))
print(my_list3.index(72)) #used to show index on a list

my_list4 = ['Evans', 'Antony', 'Don Wicliff', 'Marshall', 'Weston']
print(my_list4)
my_list4.extend(['Kelly, Roy'])
print(my_list4)
if 'Evans' in my_list4:
    print('Present')
else:
    print('Not present')
my_list4.extend([345,2345,2345])
print(my_list4)