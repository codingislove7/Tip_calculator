# Welcome Message
print("Welcome to tip calculator :)\n")
# Get the total Bill
bill = float(input("What was the total bill? $"))
# Get the persentage 
persentage = int(input("How persentage tip would you like to give ? 10, 12 or 15\n"))
# Get the amount of people that want to tip
people = int(input("How many people to split the bill ?\n"))
# Doing some Math 
total_bill = (persentage / 100 * bill + bill) / people
# Print the result
print(f"Each Person Should Pay ${round(total_bill, 2)}")

