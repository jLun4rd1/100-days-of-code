#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
percentage = input("How much tip would you like to give? 10, 12 or 15? ")
total_with_tip = int(total) * (1 + int(percentage)/100)
round_total_with_tip = round(total_with_tip, 2)

print(f"Just so you know, the total with the tip will be: ${round_total_with_tip}")

people = input("How many people to split the bill? ")

amount = round(total_with_tip/int(people), 2)

print(f"Each person should pay: ${amount}")
print("I hope you had a nice dinner :D")

#Instead of changing each variables type on spot while using them to make calculations,
#it's possible to assign a type to an input function, as follows:

total = float(input("What was the total bill? $"))

#To guarantee the 0 will appear in the second decimal place, you'll need to use format:

final_amount = "{:.2f}".format(total)
print(final_amount)