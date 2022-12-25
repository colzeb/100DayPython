# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzaPrise = {'S': 15, 'M':20, 'L':25}
pepperoniYes = {'S': 2, 'M':3, 'L':3}
pepperoni = {'N': 0, 'Y': pepperoniYes.get(size)}
cheese = {'Y': 1, 'N': 0}

finalBill = pizzaPrise.get(size) + pepperoni.get(add_pepperoni) + cheese.get(extra_cheese)
print("Your final bill is: ${bill}.".format(bill=finalBill))
