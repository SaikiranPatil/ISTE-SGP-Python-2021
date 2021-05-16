import math
# 1. Q: What is 7.3 plus 5+4j?
a=7.3
b=5+4j
print(a+b)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

# Q: Are 4e4 and 4E4 same? Check using a python operator.
print(4e4==4E4)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

"""if c = 3 + 5j, store it’s real and imaginary parts into r and i variables
 respectively."""
c=complex(3+5j)
r=c.real
i=c.imag
print(r,c)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

""" Q:Call the euler’s number e and truncate the decimal part of the number and store
that into a variable."""
d=math.trunc(math.e)
print(d)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

# 2. Pass a dictionary into a function and print the elements of the dictionary.
def print_dict(dict):
    for key in d:
        print("key:", key, "Value:", d[key])
e = {'A':6, 'D':8, 'F':3}
print(dict(e))

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

# 3. Print the factorial of a user input number
f=int(input("Enter a number to find its factorial:"))
fact=1
while f>0:
    fact*=f
    f-=1
print("factorial of the given nimber is",fact)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

# 4. Print a Fibonacci series upto the given number.
def fibo(n):
    if n==1:
        return (0)
    elif  n==2:
        return(1)
    else:
        return(fibo(n-1)+fibo(n-2))
g=int(input("Enter a number to Print a Fibonacci series:"))
for i in range(1,g+1):
    print(fibo(i))

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

"""5. Given an array of integers,find the sum of positive and negative numbers
separately and print "POSITIVE" if sum of positive numbers is greater than the
absolute value of the sum of negative numbers, else print "NEGATIVE"."""
array=[2,3,-5,6,-8,-7]
pos=0
neg=0
for key in array:
    if key>0:
        pos+=key
    else:
        neg+=-key
if pos>neg:
    print("POSITIVE")
else:
    print("NEGATIVE")

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")

"""6. Given a string, return a string of the same length where the vowels are in the first
and the consonants are in the last. But the inner order of vowels and consonants
should not change"""
h="hbefabjbaofb"
l=""
j=["a","e","i","o","u"]
k=""
for i in range(0,len(h)):
    if h[i] in j:
        l=l+h[i]
    else:
        k=k+h[i]
print(l+k)

print("\n--------------------------------------------------------------\t\t\t\t\t\t\n")

"""7. Write a code which returns the first m multiples of a natural number n, without
using any loop"""
m=int(input("Enter how many multiples"))
n=int(input("Enter the natural number"))
x = range(n, (m * n)+1, n)     
print(*x)

print("\n\t\t\t--------------------------------------------------------------\t\t\t\n")