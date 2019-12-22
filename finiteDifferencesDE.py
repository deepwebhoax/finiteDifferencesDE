import numpy as np
import matplotlib.pyplot as plt

left, top, right, bottom = 75, 100, 50, 0
lenX, lenY = 1, 1

n, m = 3, 3
hx, hy = lenX/n, lenY/m
x = np.arange(0, lenX+hx, hx)
y = np.arange(0, lenY+hy, hy)
for xi in x:
    for yi in y:
        plt.scatter(xi,yi)
        
T = np.array(len(y)*[len(x)*[-1]])
T[:,0], T[0], T[:,n], T[m,:] = left, top, right, bottom

# for Ax=b
A = np.array((len(y)-2)*[(len(x)-2)*[0]])
b = np.array((len(x)-2)*[0])
print(A,b)
eqNum = 0
for i in range(1, len(T)-1):
    for j in range(1, len(T[0])-1):
        eqNum = (i-1)*(n-1)+j-1
        # middle
        A[eqNum, eqNum] = -2/hx**2 - 2/hy**2
        # left
        if T[i,j-1]==-1:
            A[eqNum, eqNum-1] = 1/hy**2
        else:
            b[eqNum]-=T[i,j-1]/hy**2
        # top
        if T[i-1,j]==-1:
            A[eqNum, eqNum-n-1] = 1/hx**2
        else:
            b[eqNum]-=T[i-1,j]/hx**2
        # right
        if T[i,j+1]==-1:
            A[eqNum, eqNum+1] = 1/hy**2
        else:
            b[eqNum]-=T[i,j+1]/hy**2
        # bottom
        if T[i+1,j]==-1:
            A[eqNum, eqNum+n-1] = 1/hx**2
        else:
            b[eqNum]-=T[i+1,j]/hx**2
        print(A,b)

print(A)        
np.linalg.solve(A,b)