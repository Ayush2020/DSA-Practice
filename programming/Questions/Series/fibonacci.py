# Fibonacci Series



prev1  = 0
prev2 = 1
print(prev1, end=" ")
for i in range(3, 100+1):
  curr = prev1 + prev2
  prev2 = prev1
  prev1 = curr
  print(curr, end = " ")
  

# def fibo(n):
#   a,b = 0,1
#   for i in range(n):
#     print(a, end=" ")
#     a,b = b,a+b
    
# fibo(7)