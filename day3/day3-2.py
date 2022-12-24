# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / ( height * height )
bmiRounded = int(round(bmi, 0))

bmiMeaning = "underweight"

if bmiRounded > 35:
    bmiMeaning = "are clinically obese"
elif bmi > 30 and bmi <= 35:
    bmiMeaning = "are obese"
elif bmi > 25 and bmi <=30:
    bmiMeaning = "are slightly overweight"
elif bmi > 18.5 and bmi <= 25:
    bmiMeaning = "have a normal weight"
else:
    bmiMeaning = "are underweight"

print("Your BMI is {bmi}, you {meaning}.".format(bmi=bmiRounded, meaning=bmiMeaning))

