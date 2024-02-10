my_tuple = (16, 2765, 3765, 6543, 4567,'Benjamin Franklin')
print(my_tuple)
print(my_tuple[2])
print(my_tuple[1:4])
print(len(my_tuple))
del my_tuple

my_tuple2 = (12234,'Cooking',54234,432,3,4,5,234,43,2)
print(my_tuple2)
if 'Cooking' in my_tuple2:
    print('Cooking is prsesnt')
else:
    print('No cooking is found')

# print(max(my_tuple2)
# print(min(my_tuple2))
# print(sum(my_tuple2))

print(my_tuple2.count(123))

# print(sum(my_tuple2)/len(my_tuple2))

#my_tuple2[1] = 'Eating')         a tuple cannot be modified