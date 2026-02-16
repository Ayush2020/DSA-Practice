#iff teenager = discount 5%  if total price is above 5000  after discount gets additional 5% 
#if the customer is in 20s flat dis = 6%  if above 4000 additional 6%
#if customer aged above 29 flat discount 15% assume the age and total price purchase after the discount and display
#total price before discount price total price  discount discounted amount if any
#Assume the age and total price is given as input Write a program to calculate the total price of the purchase after the discount and display 
#Total price before discount.total_price after  discount.discounted price amount if any




total_price = int(input("Enter the amount you have purchased: --> "))
age = int(input("Enter the age:"))

teen_discount = 0.05
twenty_discount = 0.06
additional_discount = 0.05
additional_discount2 = 0.06
discount = 0.15

if age >= 13 and age <= 19:
    discounted_price = total_price - (total_price * teen_discount)
    if discounted_price > 5000:
      discounted_price = discounted_price - (discounted_price * additional_discount)
    discounted_price
elif 20 <= age <= 29:
    discounted_price = total_price - (total_price * twenty_discount)
    if discounted_price > 4000:
        discounted_price = discounted_price - (discounted_price * additional_discount2)
    discounted_price
    
elif age >= 30:
    discounted_price = total_price - (total_price * discount)
    discounted_price

discount = total_price - discounted_price
print(discounted_price)
print("Discounted ",discount)
