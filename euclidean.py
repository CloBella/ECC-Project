from math import *
def gcd(a,b):
    #This is an implementation of the Euclidean Algorithm
    #on each iteration, b becomes the remainder of a/b and a is set to the old value of b
    #when the remainder is 0, we're done.  
    while b:
        a, b = b, a%b
    return a

#An Implementation of the Ext. Euclidean Algorithm
#Using Bezout's identity gcd(a, b) = xa + yb
def ext_euclidean(a,b):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - *y, y
        a, b = b, a % b
    #This returns the gcd, a and b from Bezout's 
    return (a, prevx, prevy)

#returns the inverse of a number a, mod p
#i.e. finds b such that (a*b) == 1 (mod p)
def inverse(a,p):
    g, x, y = ext_euclidean(a,p)
    assert (x*a + y*p)%p == g
    if g != 1:
        raise Exception ("inverse does not exist!")
    else:
        return x % p 
