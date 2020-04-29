
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
    else:           
        return n*factorial(n-1)

# Fibonacci with recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))  

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)



def main():
    countdown(5)

    n = 10
    print("Fibonacce Series: ", n)
    for i in range(n):
        fib = fibonacci(i)
        print(fib)

    print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
    print("{} to the power of {} is {}".format(1, 3, power(1, 5)))


    print("{}! is {}: ".format(5, factorial(5)))
    print("{}! is {}: ".format(0, factorial(0)))

if __name__ == "__main__":
    main()