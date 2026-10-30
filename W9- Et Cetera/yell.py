#Yelling one phrase with upper()
def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()


#Yelling any number of words with *words and a loop
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()


#Yelling with map (applies a function to every item)
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()


#Yelling with a list comprehension (a one-line loop)
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
