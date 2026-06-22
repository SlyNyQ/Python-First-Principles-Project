print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_pay = ((bill * (100 + tip) / 100)/people)
print(tip_pay)
print(f"Each person should pay: ${round(tip_pay, 2)}")

#Alter method
#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_amount
#total_bill = bill + total_tip_amount
#bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)
#print(f"Each person should pay: ${round(tip_pay, 2)}"