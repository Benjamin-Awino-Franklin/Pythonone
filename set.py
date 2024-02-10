my_set = {112,2345,98765,6756,5674,456}
print(my_set)
char = 112
if char in my_set:
    output = char
    print(output)

my_set.add(2345)
my_set.update([2223454,3345432,56543,567])
print(my_set)
# my_set.discard()
my_set2 = my_set.copy()
print(my_set2)
print(my_set)

print(len(my_set))
my_set.discard(456)
print(my_set)
print(my_set)
del my_set
print(my_set2)

print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))

if 112 in my_set2:
    print('Present')
else:
    print('absent')

