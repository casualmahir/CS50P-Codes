#Adding two integers
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

#Adding floats, rounding, and formatting with commas
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y) #round() rounds the sum to the nearest whole number
print(f"{z:,}") #{z:,} adds separators (comma in this case)

#Dividing with two decimal places
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(f"{z:.2f}") #{z:.2f} shows two decimal places (1/3 = 0.33)

#Creating a square function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()
