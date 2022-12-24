# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
evenOdd = "odd"
if number % 2 == 0:
    evenOdd = "even"

print("This is an {evenOdd} number.".format(evenOdd=evenOdd))

