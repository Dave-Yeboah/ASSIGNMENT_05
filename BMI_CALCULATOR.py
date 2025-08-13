print(" ")
print("Body Mass Index (BMI) CALCULATOR")
print("--------------------------------")
print(" ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")

elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi}. You are normal weight.")

elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi}. You are overweight.")

elif bmi >= 30:
    print(f"Your BMI is {bmi}. You are obese.")
