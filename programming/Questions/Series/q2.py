# Kth fibonacci Number
k=6

def fibon_acci(n, k):
  a = 0
  b = 1
  
  for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
    
  
fibon_acci(10, 3)