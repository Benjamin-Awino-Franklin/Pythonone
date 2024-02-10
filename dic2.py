my_dictionary = {
    "Name": "Benjamin",
    "YOB": 2005,
    "Gender": "Male",
    "Rank": "Alpha",
    "Squad": "Seal Team",
    "Salary": "300,000,000"}

print(my_dictionary)

my_dictionary = dict(
    Name="Benjamin",
    YOB=2005,
    Gender="Male",
    Rank="Alpha",
    Squad="Seal Team",
    Salary="300,000,000")

print(my_dictionary)
print(len(my_dictionary))

for key, value in my_dictionary.items():
    print(key, value)

# end of my dictionary


my_list = ["Benjamin", "Franklin", "Awino", "Euphaemiah", "Faith", "Ann"]
print(my_list)

print(my_list.index("Benjamin"))

my_list2 = my_list.copy()
print(my_list2)

del my_list

print(my_list2)

my_list = [123,3543,4543245,53,45,523,2343,45,3234,78]
my_list.append(1990)
print(my_list)
