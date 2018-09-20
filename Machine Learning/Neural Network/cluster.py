import numpy as np
import math
import matplotlib.pyplot as plt

def distance (a,c):
    return  np.sqrt( (a[0] - c[0])**2 + (a[1] - c[1])**2 ) 

def findCenter(vec_center):
    x_center = 0
    y_center = 0
    for i in range(len(vec_center)):
        x_center += vec_center[i][0]
        y_center += vec_center[i][1]
    if len(vec_center) > 0:
        return (x_center/len(vec_center),y_center/len(vec_center))
    else:
        return [x_center,y_center]

# Prepare data
x1 = np.random.randint(0,50,size = 50)
x2 = np.random.randint(50,100,size = 50)
x = np.zeros((1,100))
x[0,0:50] = x1
x[0,50:100] = x2

y1 = np.random.randint(0,50, size = 50)
y2 = np.random.randint(50,100, size = 50)
y = np.zeros((1,100))
y[0,0:50] = y1
y[0,50:100] = y2

plt.scatter(x,y)

# Chose random center
c1 = np.random.randint(1,100,size = 2)
c2 = np.random.randint(1,100,size = 2)

epsilon = 1
FLAG_EPSILON = True
N = 1000
iters = 0

# Calculate distance to center
while FLAG_EPSILON and iters < N:
    iters += 1
    vec_c1 = []
    vec_c2 = []
    for i in range(len(x[0])):
        [x_0,y_0] = [x[0][i],y[0][i]]
        d1 = distance([x_0,y_0], c1)
        d2 = distance([x_0,y_0], c2)
        if d1 < d2:
            vec_c1.append([x_0,y_0])
        else:
            vec_c2.append([x_0,y_0])
    c1_new = findCenter(vec_c1)
    c2_new = findCenter(vec_c2)
    if (distance(c1,c1_new) < epsilon) and (distance(c2,c2_new) < epsilon):
        FLAG_EPSILON = False
    else:
        c1 = c1_new
        c2 = c2_new
        
print (c1,c2)


plt.scatter([c1[0]],[c1[1]],color = "red")
plt.scatter([c2[0]],[c2[1]],color = "green")

plt.show()