from datetime import datetime

def LCG(xo, m):
    a = datetime.now().microsecond
    b = datetime.now().second
    x = (a * xo + b) % m
    return x
