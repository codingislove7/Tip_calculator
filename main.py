# Welcome Message
print("Welcome to tip calculator :)\n")
# Get the total Bill
bill = input("What was the total bill? $\n")
# Get the persentage 
persentage = input("How persentage tip would you like to give ? 10, 12 or 15\n")
# Get the amount of people that want to tip
people = input("How many people to split the tip ?\n")
# Doing some Math 
total_tip = ((int(persentage) * float(bill)) / 100) / int(people)
# Print the result
print(f"Each Person Should Pay ${total_tip}")

