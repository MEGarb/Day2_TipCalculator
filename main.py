print("Welcome to the tip calculator!")
bill = float(input("What was the total price on the bill?  $"))
tip = int(input("What percentage would you like to tip?  ")) / 100
diners = int(input("How many people are splitting the bill?  "))
share = round((bill * (1 + tip) / diners), 2)
print(f"Each person should pay: ${share}")

