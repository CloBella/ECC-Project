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
    
class Point:
    def __init__(self,x,y, p):
        self.p = p
        self.x = x%p
        self.y = y%p
    
    def neg(self):
        return Point(self.x, -self.y, self.p)
    
    def printPoint(self):
        print(f"({self.x},{self.y})")
    
    def __add__(self, P):
        assert type(P) is Point
        x1, y1 = self.x, self.y
        x2 , y2 = P.x, P.y
        m = None #This is the gradient of the tangent
        #If the points are the same
        if (x1,y1) == (x2,y2):
            #this is the slope of the tangent line achieved by differentiating
            m = (3 * x1 * x1 + A) / (2 * y1)
        #If the points aren't the same
        else:
            m = (y2 - y1) / (x2 - x1)
        x3 = (m*m - x2 - x1)%self.p
        y3 = (m*(x3 - x1) + y1)%self.p
        #return the reflected point
        return Point(x3, -y3, self.p)
    def np(self):
        #np.array() a 'grid' of the x and y values
        return np.array([self.x, self.y])
    

