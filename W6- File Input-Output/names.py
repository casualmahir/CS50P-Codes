#Writing a name to a file (append mode adds to the end instead of overwriting)
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#Reading a file line by line
with open("names.txt", "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())

#Reading a file and sorting the lines
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello, ", line.rstrip())

#Storing names in a list first, then sorting
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
