import numpy as np

def matmult(A,B):
    if A.shape[1] != B.shape[0]:
        print ("Khong nhan ma tran")
    else:
        C = np.zeros((A.shape[0],B.shape[1]),dtype = np.int32)
        
        for i in range(C.shape[0]):
            for j in range (C.shape[1]):
                for k in range (A.shape[1]):
                    C[i][j] += A[i][k]*B[k][j]
        return C

A = np.zeros((3,2),dtype = np.int32)
B = np.zeros((2,1),dtype = np.int32)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i,j] = i+j

for i in range(B.shape[0]):
    for j in range(B.shape[1]):
        B[i,j] = i+j

C = matmult(A,B)

print (A.dot(B))
print (C)
