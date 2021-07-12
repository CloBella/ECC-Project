import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math
#configure screen dpi (dots per inch)
mpl.rcParams['figure.dpi'] = 180

#Adapted from: https://github.com/fangpenlin/elliptic-curve-explained/blob/master/elliptic-curve.ipynb

A = -3
B = 5


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def neg(self):
        return Point(self.x, -self.y)
    
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
        x3 = m*m - x2 - x1
        y3 = m*(x3 - x1) + y1
        #return the reflected point
        return Point(x3, -y3)
    def np(self):
        #np.array() a 'grid' of the x and y values
        return np.array([self.x, self.y])

def plot_curve():
    #ogrid = open grid: a way of acting on specific pixels given a row and column index
    #x and y are opposite in numpy
    #100j accounts for complex numbers
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    z = y**2 - x**3 - A*x - B
    
    #ravel() returns a contiguous flattened array. 
    #contour takes in: a grid of x values, a grid of y values and z values (the countour levels)
    #the [0] is the style?
    plt.contour(x.ravel(), y.ravel(), z, [0], colors = 'red')
    
    #This will plot two lines, the x and y axis
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

def getYValue(a, b, x):
    return pow(pow(x, 3) + x * a + b, 0.5)

def find_added_point(point0, point1, point0_annotation, point1_annotation, point2_annotation, sum_point_annotation):
    #first plot the curve
    plot_curve()
    point2 = point0 + point1
    
    line0 = np.array([point0.np(),point2.neg().np(), point1.np()])

    #This will create the end points of the line, mark them with an x
    plt.plot(line0[:,0], line0[:,1], marker='o', c = 'b')
    
    #Label the points:
    #arguments to annotate: The annotation, the point xy (x, y) you wish to annotate, the position to put the text, the coordinate system
    #that xytext is given in. 
    plt.annotate(point0_annotation, xy =line0[0], xytext=(-5, 5), textcoords='offset points')
    plt.annotate(point1_annotation, xy=line0[2], xytext=(-5, 5), textcoords='offset points')
    plt.annotate(point2_annotation, xy=line0[1], xytext=(-5, 5), textcoords='offset points')

    #Create a line between the result and the reflected result
    line1 = np.array([point2.neg().np(),point2.np()])
    plt.plot(line1[:,0], line1[:,1], marker='o', c = 'g')
    plt.annotate(sum_point_annotation, xy=line1[1], xytext=(0, 5), textcoords='offset points')
    plt.grid()
    plt.show()

def plot_scalar_mult(point, point_annotation, n, final_annotation):
    plot_curve()
    current_point = point;
    for i in range(0, n):
        current_point += point
    
    line = np.array([point.np(),current_point.np()])
    plt.plot(line[:,0], line[:,1], marker='o', c = 'b')
    plt.annotate(point_annotation, xy =line[0], xytext=(-5, 5), textcoords='offset points')
    plt.annotate(final_annotation, xy = line[1],xytext=(-5, 5), textcoords='offset points')
    plt.grid()
    plt.show()

def draw_line(point0, point1, point0_annotation, point1_annotation):
    plot_curve()
    neg_pt = point0 + point1
    int_pt = neg_pt.neg()
    
    line0 = np.array([point0.np(), point1.np(), int_pt.np()])
    plt.annotate(point0_annotation, xy =line0[0], xytext=(-5, 5), textcoords='offset points')
    plt.annotate(point1_annotation, xy=line0[1], xytext=(-5, 5), textcoords='offset points')
    plt.annotate('', xy=line0[2], xytext=(-5, 5), textcoords='offset points')
    plt.plot(line0[:,0], line0[:,1], marker='o', c = 'b')
    plt.grid()
    plt.show()

def find_pt_intersection(point0, point1):
    neg_pt = point0 + point1
    return neg_pt.neg()

if __name__ == "__main__":
    p = Point(-0.9, getYValue(A, B, -0.9))
    q = Point(0.2, getYValue(A, B, 0.2))
    r = Point(-2.2, getYValue(A, B, -2.2))
    a = Point(-0.9, getYValue(A, B, -0.9))
    a2 = a + a
    #find_added_point(p, q, 'P', 'Q', '', 'P + Q')
    plot_scalar_mult(p, 'P', 13, 'NP')
