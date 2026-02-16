
print("Welcome to the Calculator")

n1 = int(input("Enter n1:-->"))
n2 = int(input("Enter n2:-->"))

def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2
def div(n1,n2):
  return n1/n2


sign = input("Enter the action perform--> ")


match sign:
  case "+":
    print(add(n1,n2))
  case "-":
    print(sub(n1,n2))
  case "*":
    print(mul(n1,n2))
  case "/":
    print(div(n1,n2))
  case _:
    print("Invalid operation")

