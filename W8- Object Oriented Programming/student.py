# STUDENT EXAMPLES WITHOUT CLASSES
# The same task (store a student's name and house) using different data types.


# 1. Two separate functions
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()


# 2. Returning a tuple (name, house)
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()


# 3. Trying to change a tuple
# Tuples are immutable, so typing "Padma" crashes with a TypeError.
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()


# 4. Returning a list instead (lists can be changed)
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()


# 5. Using a dictionary, built step by step
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()


# 6. Using a dictionary, created in one line
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()


# 7. Changing a value inside a dictionary
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
