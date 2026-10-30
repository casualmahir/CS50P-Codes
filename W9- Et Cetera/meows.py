#Meowing with a constant (uppercase name means "don't change this")
MEOWS = 3

for _ in range(MEOWS):
    print("meow")


#Meowing with a class constant and a method
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()


#Meowing with type hints
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)


#Returning the meows as one string instead of printing them
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


#Adding a docstring that documents the function
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


#Reading a -n option from the command line with sys.argv
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")


#Reading a -n option with argparse (it handles errors and --help for you)
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
