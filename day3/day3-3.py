# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
isLeapYear = False
if year % 4 == 0:
    isLeapYear = True
    if year % 100 == 0:
        isLeapYear = False
        if year % 400 == 0:
            isLeapYear = True

# isLeap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

isLeapYearString =  "Leap year." if isLeapYear else "Not leap year."
print(isLeapYearString)


