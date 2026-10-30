#Creating a hello function with a default value, so it can be tested
def main():
    name = input("What's your name? ")
    print(hello(name))

#Returns the greeting instead of printing it, so a test can check it
def hello(to="world"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
