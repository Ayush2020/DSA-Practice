
def strong_num(num):
  num = 145
  temp = num
  summ = 0

  while temp > 0:
    digit = temp % 10
    fact = 1
    i = 1
    while i <= digit:
      fact *= i
      i+=1
    summ += fact
    temp //= 10
  print(summ)
    
  if summ == num:
    return "Strong num"
  else:
    return "not Strong"
    
print(strong_num(145))