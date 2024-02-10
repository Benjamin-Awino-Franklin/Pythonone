height = input("What is your height? ")
weight = input("What is your weight? ")

BMI = float(weight) / float(height) ** 2
print(BMI)

if BMI < 18:
    print("You are under-weight")
elif 18 <= BMI <= 24:
    print("Your weight is normal")
elif 25 <= BMI <= 30:
    print("You are over-weight")
else:
    print("You have an abnormal over-weight")
