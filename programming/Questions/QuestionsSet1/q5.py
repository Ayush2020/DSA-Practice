#Switch Case or match
day = "monday"

match (day):
  case "monday":
    print("Today is Monday")
    
  case "tuesday":
    print("Today is Tuesday")
    
  case "wednesday": 
    print("Today is Wednesday")
    
  case "thursday":
    print("Today is Thursday")
    
  case "friday":
    print("Today is Friday")
    
  case "saturday":
    print("Today is Saturday")
    
  case "sunday":
    print("Today is Sunday")
  case _:
    print("Invalid Day")
