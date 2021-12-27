# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    print(n1, ",", n2, end=', ')
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

# Fibonacci Sequence Using Recursion


def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))


nterms = int(input("Enter the number of Terms you want: "))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(fibo(i))
