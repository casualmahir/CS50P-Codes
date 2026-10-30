#Importing hello from own library (sayings.py)
import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

#Importing goodbye from own library (sayings.py)
import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
