# Exercise 1
print("Bob ST1001 bob@gmail.com")

# Exercise 2
print("Bob\nST1001\nbob@gmail.com")

# Exercise 3
a = 14
b = 7
print(a, "+", b, "=", a + b)
print(a, "*", b, "=", a * b)
print(a, "-", b, "=", a - b)
print(a, "/", b, "=", a / b)

# Exercise 4
for i in range(1, 6):
    print(i)

# Exercise 5
print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")

# Exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
num = 23
textnum = "57"
decimal = 98.3

print(type(num))
print(type(textnum))
print(type(decimal))

# Converting textnum to int and calculating the sum
total = num + int(textnum) + decimal
print("Sum =", total)
print("Type of sum:", type(total))

# Exercise 8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

minutes_in_year = days_in_year * hours_in_day * minutes_in_hour

print("This program calculates the number of minutes in a year.")
print("Total minutes in a year:", minutes_in_year)

# Exercise 9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10
pounds = float(input("Please enter amount in pounds: "))
conversion_rate = 1.25  # Example rate
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars}")
