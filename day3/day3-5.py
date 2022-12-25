# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedName = ( name1 + name2 ).lower()
love = combinedName.count('l') + combinedName.count('o') + combinedName.count('v') + combinedName.count('e')

true = combinedName.count('t') + combinedName.count('r') + combinedName.count('u') + combinedName.count('e')

finalScore = true * 10 + love
if finalScore < 10 or finalScore > 90:
    print("Your score is {score}, you go together like coke and mentos.".format(score=finalScore))
elif finalScore < 50 and finalScore > 40:
    print("Your score is {score}, you are alright together.".format(score=finalScore))
else:
    print("Your score is {score}.".format(score=finalScore))
