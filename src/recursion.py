
# Count down with recusion
def countdown(x):
    if x==0:
        return
    else:
        print("Print value of x and execute countdown:", x)
        countdown(x-1)
        print("Pop element by element from stack after countdown() completion")

# Factorial with recusion 
def factorial(n):
    if n == 0:
        return 1  
    if n == 1:                
        return n
    else:           
        return n*factorial(n-1)

# Fibonacci with recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))  


countdown(5)
fact = factorial(5)
print("Factorial: ",fact)

n = 10
print("Fibonacce Series: ", n)
for i in range(n):
    fib = fibonacci(i)
    print(fib)