print('Welcome to the tip calculator.')
a=float(input("What was the total bill? $"))
b=int(input("What percentage tip would you like to give? 10,12, or 15? "))
c=int(input("How many people to split the bill? "))
d=float(b/100)
e=a*d +a
print(f"Each person should pay: ${round((e/c),2)}")

