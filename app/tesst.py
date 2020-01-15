import random
import math

def hello_world(test=False):
    if test == True:
       print(hello_world())
    else: 
        return random.getrandbits(10000000)

