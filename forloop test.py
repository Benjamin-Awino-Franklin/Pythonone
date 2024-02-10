my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summation = 0

for num in my_list:
    summation += num
print(summation)
print("Your total is", summation)

math = float(input("What is your score in math? "))

english = float(input("What is your score in english? "))

print(math, english)


if math < 30 or english < 30:
    print("You failed")
else:
    print("Your marks are not valid")
