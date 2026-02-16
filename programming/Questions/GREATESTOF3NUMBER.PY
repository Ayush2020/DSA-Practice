#Greatest of three numbers

a = 10
b = 20
c = 5

# if a > b:
#   if a > c:
#     print(f"{a} if greater")
#   else:
#     print("c is greater")
# else:
#   if b > c:
#     print("b is greater")
#   else:
#     print("c is greater")

#With conditional statements

if a > b and a >c:
  print("a is greater")
elif b > a and b > c:
  print("b is greater")
else:
  print("c is greater")