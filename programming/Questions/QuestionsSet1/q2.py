marks = int(input("Enter the marks: "))
 
if 100 > marks < 0:
  print("Invalid marks")
else:
  if 90 <= marks <= 100:
    print(f"Grade = A")
  elif 75 <= marks < 90:
    print("Grade = B")
  elif 60 <= marks < 75:
    print("grade = C")
  else:
    print("Fail")