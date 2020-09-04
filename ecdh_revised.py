import math
import random
import sys
class Curve:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.descriminant = -16*(4*(pow(a,3))+27*(pow(b,2)))
        if not self.nonSingular():
            raise Exception("The curve is singular!")
    
    def nonSingular(self):
        return self.descriminant != 0

    def equalCurves(self, C):
        return (self.a, self.b)==(C.a, C.b)

    def pointOnCurve(self, x, y):
        return round(y*y) == round(x*x*x + (self.a)*x + self.b)

    def printCurve(self):
        signA, signB = None, None
        if( self.a >= 0):
            signA = '+'
        else:
            signA = ''
        if( self.b >= 0):
            signB = '+'
        else:
            signB = ''
        print(f"y^2 = x^3 {signA}{self.a}*x {signB}{self.b}")
    
class Point:
    def __init__(self,curve,x,y):
        self.x = x
        self.y = y
        self.curve = curve
    
    def onCurve(E,self):
        return (self.y)**2 == (self.x)**3+((self.curve).a)*x+(self.curve).b
    
    def neg(self):
        return Point(self.curve, self.x, -self.y)
    
    def printPoint(self):
        print(f"({self.x},{self.y})")
    
    def __add__(self, P):
        if not P.curve.equalCurves(self.curve):
            raise Exception ("Can't add points not on the same curve!")
        x1 = self.x
        y1 = self.y
        x2 = P.x
        y2 = P.y
        m = None #This is the gradient of the tangent
        #If the points are the same
        if (x1,y1) == (x2,y2):
            #this is the slope of the tangent line achieved by differentiating
            m = (3 * x1 * x1 + self.curve.a) / (2 * y1)
        #If the points aren't the same
        else:
            m = (y2 - y1) / (x2 - x1)

        #This is the x and y coordinates of the final point. -> This is how it is mathematically created. 
        x3 = m*m - x2 - x1
        y3 = m*(x3 - x1) + y1

        #return the reflected point
        return Point(self.curve, x3, -y3)

def getYValue(a, b, x):
    return pow(pow(x, 3) + x * a + b, 0.5)

def scale_point(n, P):
    res = P
    for i in range(0,n):
        res = res + P
    return res

class P1:
    def __init__(self, P):
        self.P = P
        #generate a private key
        self.N = int(random.randrange(1,15))
        print(f"\nAlice chooses the number: {self.N}")
    def gen_pub(self):
        self.pub = scale_point(self.N, self.P)
        self.pub.printPoint()
    def gen_key(self, MP):
        key_pt = scale_point(self.N, MP)
        self.key = round(key_pt.x,3)
class P2:
    def __init__(self, P):
        self.P = P
        #generate a private key
        self.M = random.randrange(1,15)
        print(f"\nBob chooses the number: {self.M}")
    def gen_pub(self):
        self.pub = scale_point(self.M, self.P)
        self.pub.printPoint()
    def gen_key(self, NP):
        key_pt = scale_point(self.M, NP)
        self.key = round(key_pt.x,3)

#Perform ECDH: passed the beginning point as an argument
def ecdh(P):
    print("\nBoth generate their private keys ")
    #Set up the people and their private keys
    Alice = P1(P)
    Bob = P2(P)

    #Generate public keys based on the point and private key
    print("\nAlice generates her public key: ")
    Alice.gen_pub()

    print("\nBob generates his public key: ")
    Bob.gen_pub()

    #Generate the shared secret
    print("\nBoth generate the secret key: ")
    Alice.gen_key(Bob.pub)
    Bob.gen_key(Alice.pub)

    print("\nThe key Alice generated was: ")
    print(Alice.key)

    print("\nThe key Bob generated was: ")
    print(Bob.key)

    if Bob.key != Alice.key:
        print("\nECDH FAILED")
    else:
        print("\nECDH SUCCESS")

if __name__ == "__main__":
    a = int(input("What curve would you like to use? Please input an a value: "))
    b = int(input("Please input a b value: "))
    c = Curve(a, b)
    print("\nThe curve we are using is:")
    c.printCurve()
    x = float(input("\nWhat point would you like to use? Please input an x value: "))
    p = Point(c,x, getYValue(a, b, x))
    if not c.pointOnCurve(p.x,p.y):
        print("\nINVALID POINT")
        sys.exit()
    ecdh(p)
