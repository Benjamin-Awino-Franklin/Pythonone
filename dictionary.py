my_dictionary = {
    "Name":"Benjamin",
    "YOB":2005,
    "Gender":"Male",
    "Rank":"Alpha",
    "Squad":"Seal Team",
    "Salary":"300,000,000"}


my_dictionary = dict(
    Name="Benjamin",
    YOB=2005,
    Gender="Male",
    Rank="Alpha",
    Squad="Seal Team",
    Salary="300,000,000"
)

print(my_dictionary)
print(my_dictionary["Name"])
print(my_dictionary["YOB"])
print(my_dictionary["Gender"])
print(my_dictionary["Rank"])
print(my_dictionary["Squad"])

my_dictionary['Gender'] = "Female"
print(my_dictionary)
my_dictionary['YOB'] = 2006
print(my_dictionary)
my_dictionary2 = my_dictionary

print(len(my_dictionary))

my_dictionary.pop("Gender")  #removes a specific element
print(my_dictionary)

del(my_dictionary)

for value in my_dictionary2:
    print(my_dictionary2[value])

for key in my_dictionary2:
    print(key)              # prints the dictionary keys

for key, value in my_dictionary2.items():
    print(key, value)       # prints dict key & value