# BBank application platform based on account type and selected type
#Input 1-> Account Type
#1. Savings
#2. Current

# Input 2 --> operations
#1--> Deposit
# 2 -->Withdraw
# 3--> Check Balance 


#Rules --> 
#1. If savings -> Withdrawal limit 25000
#2 Current --> No Withdrawal Limit  

#Design nested switch case where outer switch account type and inner switch operations


acc_type = input("Enter the Account type:-->").lower()
print("""
      Press 1 --> Deposit
      Press 2 --> Withdraw
      Press 3 --> Check Balance
      """)
operation = int(input("Enter the operation:-->"))


match acc_type:
  case "savings":
    match operation :
      case 1:
        print("Amount Depositing----")
      case 2:
        withdrawal_amount = int(input("Enter the amount to withdraw:-->"))
        if withdrawal_amount > 25000:
          print("Withdrawal limit exceeded, max amount --> 25000")
        else:
          print("Withdrawal Successfull")
      case 3:
        print("Checking balance")
  case "current":
    match operation:
      case 1:
        print("Amount Depositing----")
      case 2:
        print("Withdrawal Successfull")
      case 3:
        print("Checking balance")