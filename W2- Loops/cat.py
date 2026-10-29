#Meowing with a while loop
i = 0
while i < 3:
    print("meow")
    i += 1
  
#Meowing with a for loop (and validating input with while True)
while True:
    n = int(input("What's n? "))
    break

for _ in range(n):
    print("meow")

#Meowing with functions (get_number and meow)
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
