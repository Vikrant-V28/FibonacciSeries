<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/156916372-d8c1bbdd-5fe9-40d1-a250-5a1d4d454832.png">
</div>

<h1 align="center">Fibonacci Series</h1>

A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.
* In this program, we have to print the Fibonacci sequence using while loop.

### Prerequisites
`Python 3`

### Source Code
```python3
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
   print("Fibonacci sequence upto",nterms,":")
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
```

## Output
![Screenshot (153)](https://user-images.githubusercontent.com/85709371/147452665-71f070b5-27a6-419e-a2a8-f938ca271064.png)

Here, we store the number of terms in nterms. We initialize the first term to 0 and the second term to 1.

If the number of terms is more than 2, we use a while loop to find the next term in the sequence by adding the preceding two terms. We then interchange the variables (update it) and continue on with the process.

## You can also solve this problem using recursion:
### Source Code
```python3
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
```

## Output
![Screenshot (155)](https://user-images.githubusercontent.com/85709371/147453381-a5b622a3-8e49-4d73-803d-11e468acefb1.png)

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
