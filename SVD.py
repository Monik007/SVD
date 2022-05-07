import math
import numpy as np
arr = [[2, 4],
       [1, 3],]


def transpose(arr):
    m = len(arr[0])
    temp = []
    for k in range(m):
        temp.append([])
    for i in arr:
        for j in range(m):
            temp[j].append(i[j])
    return temp


def sigma(eigenV,A):
    t = []
    for i in range(len(A[0])):
        t.append(0)
    sigma = [[*t]for i in range(len(A))]
    for i in range(len(eigenV)):
        sigma[i][i%2] = (eigenV[i]**(1/2))
    return sigma


def Matrix_multiplication(A, B):
    ans = np.matmul(A, B)
    return ans.tolist()


def Eigen_values(A):
    return np.linalg.eig(A)

def V(U,At,eigv):
    V = []
    k = transpose(U)
    for i in range(len(eigv)- eigv.tolist().count(0)):
        V.append(Matrix_multiplication(At, k[i]))
    for g in range(len(V)):
        print((eigv[g])**(1/2))
        V[g][0] = V[g][0]/((eigv[g])**(1/2))
        V[g][1] = V[g][1] / ((eigv[g]) ** (1 / 2))

    return V
    


def SVD(arr):
    arrt = transpose(arr)
    A = Matrix_multiplication(arr, arrt)
    print("A is", *A)
    print("----------------")
    E, U = Eigen_values(A)
    print("eigen values :", E.tolist())
    print("----------------")
    print("U is:")
    print(U)
    print("----------------")
    sig = sigma(E,arr)
    print("E is: ",sig)
    print("----------------")
    Vt = V(U, arrt, E)
    Vt = transpose(Vt)
    print("V* is",*Vt)







SVD(arr)