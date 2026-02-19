#Print series of prime number


start = int(input("Enter the starting range -->: "))
end = int(input("Enter the ending range: --> "))

# num = start

# while num <= end:
#   if num > 1:
#     i = 2
#     while i < num:
#       if num % i == 0:
#         break 
#       i+=1
#     else:
#       print(num)
#   num +=1



for num in range(start, end + 1):
  if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        break
    else:
      print(num)
      
      
    