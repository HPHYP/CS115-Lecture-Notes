age = 22
age2 = 22
if age > 21:
  print("You are an adult.")
  print("You are old.")
else:
  print("You are young.")

difference = age - age2
if difference >= 0:
  print("Positive or zero.")
elif difference > 5: 
  print("Big number")
elif difference < 0:
  print("negative")

counter = 0 

while counter <= 10:
  print(counter)
  counter += 1

inventory = ['sword', 'shield', 'key']

for item in inventory:
  print(item)