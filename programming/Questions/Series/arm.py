

num = int(input("Enter the number:---> "))

temp = num
copy_num = num
summ = 0
count = 0


while temp > 0:
  count+=1
  temp//=10

print(count)

while copy_num > 0:
  digit = copy_num % 10
  power = 1
  for i in range(1, count+1):
    power *= digit
    
  summ += power
  copy_num//=10



print(summ)
if num == summ:
  print("Strong")
else:
  print("Not")
