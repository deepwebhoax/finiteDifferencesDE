import numpy as np
import matplotlib.pyplot as plt


def get_plate_temperature(size, left, top, right, bottom):
    lenX, lenY = size[0], size[1]
#     lenX, lenY = 1, 1

    # x and y segment count
    n, m = 5, 6
    
    # x and y segment lengths
    hx, hy = lenX/n, lenY/m
    # temperature matrix
    T = np.array((m+1)*[(n+1)*[-1]])
    T[:,0], T[0], T[:,n], T[m,:] = left, top, right, bottom

    # Creating A and b for future Ax=b system
    A = np.array((m-1)*(n-1)*[(n-1)*(m-1)*[0]], dtype='f')
    b = np.array((m-1)*(n-1)*[0], dtype='f')

    # Calculating coefficients of variables adding them to A, calculating b
    eqNum = 0
    for i in range(1, len(T)-1):
        for j in range(1, len(T[0])-1):
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
            eqNum+=1
            
    # Solving system of linear equations
    x = np.linalg.solve(A,b)
    # Make x into a matrix
    x = [list((x[(n-1)*i:(n-1)*(i+1)])) for i in range(m-1)]
    return x