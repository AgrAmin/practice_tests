from functools import lru_cache
#from fucntool module import a decorator Least Recent Used cache
#it allows a way to apply memoriztion to functions with one line

@lru_cache(maxsize=1000) #1000 value to cache
def fibonacci(n):
#check the input n
    if type(n)!=int:
        raise TypeError("n must be a positive integer")
    if n<1:
        raise ValueError("n must be a positive integer")
#the fibonacci magic : (aka defining the sequence)
    if n == 1 :
        return 1
    elif n==2 :
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)


for n in range (1,101):
    print(n," : ",fibonacci(n))
