#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

billAmount = float(input("Enter the bill Amount: "))
eachPersonAmount = (billAmount/5)
eachPersonWithTip = eachPersonAmount * 0.12;
roundedAmount = round(eachPersonAmount+eachPersonWithTip, 2)
print("Your bill is {billAmount:>20.2f}\nSplit amount {splitAmount:>20.2f} \nTip amount {tipAmount:>22.2f}\nTotal amount {totalAmout:>20.2f}"
.format(billAmount=billAmount, 
splitAmount=eachPersonAmount, 
tipAmount=eachPersonWithTip, 
totalAmout=roundedAmount))
