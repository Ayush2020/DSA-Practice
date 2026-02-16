#A Customer provides a total number of units consumed in a month 
# The billing rules are:
# 1. For thr first 100 units, charge 2 per unit 
# 2. For units between 101 and 300 charge 4 per unit
# 3. For units above 300 , charge 6 per unit 
#After calculating the total price 
#If the total amount exceeds 2000 apply a 10% surcharge on the total bill
# Write a  program to calculate and discount the first electricity bill amount
#Do this using fucntions 


unit = int(input("Enter the Units u have consumed : --> "))
surcharge = 0.1

def calculate_bill(unit):
  if unit <= 100:
    total_price = unit * 2
  elif 100 < unit <= 300:
    total_price = (100 * 2) + ((unit - 100) * 4)
  elif unit > 300:
    total_price = (100 * 2) + (200 * 4) + ((unit - 300) * 6)
  
  if total_price > 2000:
    total_price = total_price + (total_price * surcharge)
  return total_price

bill_amount = calculate_bill(unit)
print("Total Bill", bill_amount)
