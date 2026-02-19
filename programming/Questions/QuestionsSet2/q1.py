# Find the count of 2 
n = 12

# for i in range(1,n):
#   if n % i == 0:
#     print(i)


count = 0
for i in range(1,(n//2)+1):
  if n % i == 0:
    print(i)
    count+=1

print("Counted Numbers:--->",count)