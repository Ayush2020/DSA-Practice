#Design an app to read the age of 3 sibs ramu, raghu, raju and store them in a variable 
#the app when executed should display the age of the youngest siblings

ramu = 23
raghu = 34
raju = 180

if ramu <  raghu :
  if ramu < raju:
    print(f"Ramu {ramu} is youngest")
  else:
    print(f"Raju{raju} is youngest")
else:
  if raghu < ramu :
    if raghu < raju:
      print(f"Raghu {raghu} is youngest")
    else:
      print(f"Raju{raju} is youngest")
