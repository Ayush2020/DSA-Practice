#ATM MAchine options
#1 --> Check balance
#2 --> Withdraw
#3 --> Deposit
#4 --> Mini Statement
#5 --> Exit

select = int(input("Enter the number: -->"))

match select:
  case 1:
    print("Check balance")
  case 2:
    print("Withdraw")
  case 3:
    print("Deposit")
  case 4:
    print("Mini Statement")
  case 5:
    print("Exit")
  case _ :
    print("invalid number")

