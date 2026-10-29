#Checking even or odd with %
x = int(input("What's x? "))

if x % 2 == 0: #% gives the remainder after division
    print("Even")
else:
    print("Odd")

#Checking even or odd by creating a function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
