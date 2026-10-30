#Tracking a balance with a global variable
balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

#"global" lets the function change the variable defined outside it
def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()


#Tracking a balance with a class (no global variable needed)
class Account:
    def __init__(self):
        self._balance = 0

    #@property lets you read account.balance without changing it directly
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()
