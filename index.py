print("Hello World")
print("Welcome to my first project")
print("The girl in front of me is killing me, damn. I'm losing it")
# variables
age = 21
print(age)
print("The age of the boy is")

# data types
# string
# integer
# float 10.4  9.4
# boolean False or True
# list
# sets
# dictionary

name = "Felix"
print(name)

last_name = "Awino"
print(last_name)

# string
var1 = "Welcome to eMobilis tech institute"
print(var1)

# integer
var2 = 122
print(var2)
print(600)

# float
num_1 = 10.3456
print(num_1)

# boolean
student = False
print(student)

virgin = True
print(virgin)

former_school = ("St. Joseph's School Rapogi")
age = ("19")
print(age)
print(former_school)

# list
my_list= [234,123,1234,234,23,4234,123,123,  "Roysambu", 'felix',10.08]
print(my_list)
print(my_list[2:5])
print(my_list[9:11])

my_set= {"Ann", "Bob", "Charlie", "Joseph"}
print(my_set)

# dictionary
my_dictionary= {"name":"Ann",
                "age":24,
                "school":"eMobilis"}
print(my_dictionary)

my_dictionary["school"] = "Nairobi"
my_dictionary["Year"] = 2024
print(my_dictionary)

# create a dictionary 0f 4 key:pair values
# then add a fifth key
# pair value and print out the outpout

test_dictionary = {"name":"Benjamin Franklin", "age":19, "school":"St. Joseph's School Rapogi", "Gender":"Male"}
test_dictionary["Year of Birth"] = 2005
print(test_dictionary)

# name1 = input("What is your name? ")
# age1 = input("What is your age? ")
#
# print(name1)
# print(age1)
# print("Hello", name1)
#
# birth_year = input("What is your birth year? ")
# print(birth_year)
# age2 = 2024 - int(birth_year)
# print(age2)

# #get 2 inputs from the user and sum the input
# # sum the inputs then print
#
# cont = input("What is your name? ")
# cont1 = input("What is your monthly salary? ")
# cont2 = input("What is your monthly tax? ")
#
# bank_balance =int(cont1)-int(cont2)
# print(bank_balance)

print("This the registration form to apply as an internship")
print("Please provide the required details below")

q1 = input("What is your name? ")
q2 = input("Which year were you born? ")
q3 = input("Which school did you study in? ")

age = 2024-int(q2)
print(age)

q4 = input("How much do you earn every year? ")
q5 = input("How much is taxed from your account every year? ")

reamaining_income = int(q4)-int(q5)
print(reamaining_income)

print("Hello", q1 )