#Restaurant menu selection 
#!  Idli
#!  Dosa
#!  Biryani
#!  Meals
#!  Ice Cream
#WAP that reads the menu number and displays if invalid coice 
#Display invalid choice 


choice = int(input("Enter the menu number: -->"))

match choice:
  case 1:
    print("You choose Idli")
    
  case 2:
    print("You choose Dosa")
    
  case 3:
    print("You choose Biryani")
  case 4:
    print("You choose Meals")
    
  case 5:
    print("You choose Ice Cream")
  case _:
    print("Invalid Choice")