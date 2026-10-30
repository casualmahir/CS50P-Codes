#Unpacking a list into positional arguments with *
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")


#Unpacking a dictionary into named arguments with **
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")


#Collecting positional arguments with *args
def f(*args, **kwargs):
    print("Positional: ", args)

f(100, 50, 25)


#Collecting named arguments with **kwargs
def f(*args, **kwargs):
    print("Named: ", kwargs)

f(galleons=100, sickles=50, knuts=25)
