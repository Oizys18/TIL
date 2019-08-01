f = open("C:/Python/newfile.txt", 'w')

def fib(n):
    if n == 0 : return 0 
    elif n == 1 : return 1 
    elif n >= 2 : return fib(n-2) + fib(n-1)

f.write(fib(5))

