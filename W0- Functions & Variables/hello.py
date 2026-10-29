#One name
name = input("What's your name? ").strip().title()
print(f"Hello, {name}")

#Two names
name = input("What's your name? ").strip().title()
first, second = name.split(" ")
print(f"Hello, {first}")

#Creating hello function
def main():
    name = input("What's your name? ")
    hello(name)
def hello(to):
    print("Hello,", to)
main()
