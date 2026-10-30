#Counting sheep by building a whole list first
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()


#Counting sheep with a generator (yield gives one value at a time)
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
