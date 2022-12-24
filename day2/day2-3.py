# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
intAgeLeft = 90 - int(age)
print("You have {days} days, {weeks} weeks, and {months} months left.".format(days=intAgeLeft * 365, weeks=intAgeLeft* 52, months=intAgeLeft*12))




