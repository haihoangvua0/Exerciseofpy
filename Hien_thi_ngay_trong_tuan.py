a = int(input("Enter a number to predict date: "))
date = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if a == 2:
  print("The date is {}".format(date[0]))
elif a == 3:
  print("The date is {}".format(date[1]))
elif a == 4:
  print(f"The date is {date[2]}")
elif a == 5:
  print(f"The date is {date[3]}")
elif a == 6:
  print(f"The date is {date[4]}")
elif a == 7:
  print(f"The date is {date[5]}")
elif a == 8:
  print(f"The date is {date[6]}")
else:
  print("Error!!!")
