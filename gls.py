import math

a = int(input())
b = int(input())

print(math.e)
def plus_e(a,b):
 return a+b+math.e*2

def mse_loss(a,b):
 return  (a-b)**2

def relu(a):
 return 0 if a < 0 else a

def sqr(a,b):
 return a**2, b**2
