# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time 
#import cv2




def process(data,a,b,c_mat):
    
#    print("a:")
#    print(a)
    y_1 = np.zeros_like(data)
    y_2 = np.zeros_like(data)
    
    # left - right
    for x in range(2,data.shape[1]):
        for y in range(0,data.shape[1]):
            y_1[y,x] = a[0]*data[y,x]+a[1]*data[y,x-1]+b[0]*y_1[y,x-1]+b[1]*y_1[y,x-2]
    
    # right - left
    for x in range(data.shape[1]-3,0,-1):
        for y in range(0,data.shape[1]):
    #        print(x)
            y_2[y,x] = a[2]*data[y,x+1]+a[3]*data[y,x+2]+b[0]*y_2[y,x+1]+b[1]*y_2[y,x+2]

    return c_mat*(y_1+y_2)

def process_2(data,a,b,c_mat):
    
#    print("a:")
#    print(a)
    y_1 = np.zeros_like(data)
    y_2 = np.zeros_like(data)
    
    # left - right
    for x in range(2,data.shape[1]):
        y_1[:,x] = a[0]*data[:,x]+a[1]*data[:,x-1]+b[0]*y_1[:,x-1]+b[1]*y_1[:,x-2]
    
    # right - left
    for x in range(data.shape[1]-3,0,-1):
        y_2[:,x] = a[2]*data[:,x+1]+a[3]*data[:,x+2]+b[0]*y_2[:,x+1]+b[1]*y_2[:,x+2]

    return c_mat*(y_1+y_2)


file = "./data/p2.png"

data = plt.imread(file)[:,:,0]

data = int8(data*255)+128;
data2 = uint8(data*255);

print(np.min(data))
print(np.max(data))

#data[10:20,:]=0
#data[:,10:20]=0

# image index (y,X)





## based on the definition from wiki x axis
alpha = 10
k = np.power(1-np.exp(-alpha),2)/(1+2*alpha*np.exp(-alpha)-np.exp(-2*alpha))
a_full = [0,1,-1,0,
     k,k*np.exp(-alpha)*(alpha-1),k*np.exp(-alpha)*(alpha+1),-k*np.exp(-2*alpha)]

b = [2*np.exp(-alpha),-np.exp(-2*alpha)]
c = [-1*np.power(1-np.exp(-alpha),2),1]

print(a_full)
print(b)
print(c)

dt = time.time()

stage_1 = process(data,a_full[0:4],b,c[0])
stage_2 = process(stage_1,a_full[4:],b,c[1])
aa = np.abs(stage_2)>5 
stage_1 = process(np.transpose(data),a_full[0:4],b,c[0])
stage_2_a = process(stage_1,a_full[4:],b,c[1])

bb = np.transpose(np.abs(stage_2_a))>5



t = time.time() - dt
print('run time:{}'.format(t))

dt = time.time()
stage_1 = process_2(data,a_full[0:4],b,c[0])
stage_2 = process_2(stage_1,a_full[4:],b,c[1])
aa = np.abs(stage_2)>30
stage_1 = process_2(np.transpose(data),a_full[0:4],b,c[0])
stage_2_a = process_2(stage_1,a_full[4:],b,c[1])
bb = np.transpose(np.abs(stage_2_a))>30
final = aa+bb;
#
t = time.time() - dt
print('run time2:{}'.format(t))

plt.subplot(141)
plt.imshow(data)
plt.title('Original: uint8')

plt.subplot(142)
plt.imshow(aa)
plt.title('X sweep')


plt.subplot(143)
plt.imshow(bb)
plt.title('Y sweep')

plt.subplot(144)
plt.imshow(final)
plt.title('Final')


