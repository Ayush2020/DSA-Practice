# Prime Numbers 

# i = 2
# num = 97
# count = 0
# while i <= num:
#   if num % i == 0:
#     count +=1
#     if count >2:
#       print("Not Prime")
#       break
#   i+=1
# else:
#   print("Prime")


num = 97
i = 2
count = 0
for i in range(1, num+1):
  if num % i == 0:
    count +=1
    if count > 2:
      print("Not Prime")
      break
else:
  print("Prime")