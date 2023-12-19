"""
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print b(a, b)


alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
"""

x = 12
def g(x):
	x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)