def fib(n):                 # write Fibonacci series up to n
    """ Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print("\t",a, end='')
        a,b = b, a+b
    print()

# Now call the function we just defined
fib_number = int(input("Please input a number that Fibonacci series up to: "))
print(fib(fib_number))