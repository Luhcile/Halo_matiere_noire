from numpy import linspace
from scipy import pi,sin,cos,sqrt,arctan2
import pylab as p

def ellipse(a,b,ang,x0,y0):
    ca,sa=cos(ang),sin(ang)
    t = linspace(0,2*pi,73)
    X = x0 + a*cos(t)*ca - sa*b*sin(t)
    Y = y0 + a*cos(t)*sa + ca*b*sin(t)
    return X,Y

def decode_ee(e1,e2,scale=0.03):
    #from:    e = (a-b)/(a+b)
    #we have: a/b = (1+e)/(1-e)
    #below solution for: a+b=scale*2 (=const)
    e = sqrt(e1**2+e2**2)    
    a = (1+e)*scale
    b = (1-e)*scale
    ang = 0.5*(arctan2(e2,e1))
    return e,a,b,ang

if __name__ == '__main__':

    fig = p.figure(figsize=(10,10))
    p.axis([-1.11,1.11,-1.11,1.11])
    p.title('Plot for: e=(a-b)/(a+b)')
    p.xlabel('e1')
    p.ylabel('e2')

    es = linspace(-1,1,2**4+1)
    for e1 in es:
        for e2 in es:
            e,a,b,ang = decode_ee(e1,e2)
            if e > 1:
                continue #unphysical stuff
            X,Y=ellipse(a,b, ang, e1,e2)
            p.plot(X,Y,"b-",ms=1)
    p.grid(True)


    #Sky74,1,2302.13,3181.16,2302.13,3181.16,0.00,0.00,0.00,0.00
    #Galaxy59,1299.09,2236.58,-0.992288,-0.351086
    fig = p.figure(figsize=(10,10))
    p.title('Sky74, Galaxy59')
    x0,y0 = 2302.13,3181.16
    xg,yg,e1,e2 = 2299.09,3236.58,0.99,0.01

    p.axis('equal')
    p.plot(x0,y0,'g.',markersize=20.00, label='halo center')
    
    e,a,b,ang = decode_ee(e1,e2,25)
    X,Y=ellipse(a,b, ang, xg,yg)
    p.plot(X,Y,"b-",ms=1, label='galaxy shape')
    p.plot(xg,yg,'b.',markersize=20.0, label='galaxy center')

    ax = p.gca()
    ax.set_autoscale_on(False)
    
#   X,Y=ellipse(a*100,b*100, ang, xg,yg)
#    p.plot(X,Y,"r-",ms=1, label='galaxy shape mag 100x')

    p.legend()
    p.grid(True)
    p.show()
