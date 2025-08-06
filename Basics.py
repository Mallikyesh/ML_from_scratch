
#importing the library into a varible for easy instantiation in deeper parts of the code.
import numpy as np

#understanding why use numpy? 1. python lists are best suited for homo & heterogeneous uses, however when it comes to processing
#homogeneous data , Numpy is rewarding , esp when there are large quantities

#one dim array
'''
array1 = np.array([1,4,3])
print(array1)
print("1st element is" , array1[0], "2nd is", array1[1], "and lastly",array1[2])

print(array1[:1])
'''
'''
#higher dim (2D array) , matrix     #3D is called tensor
#[1,2,3,4]
#[5,6,7,8]
#[9,10,11,12]

arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#3 rows, 4 cols
#print(arr)
#print(arr[0]) #prints the first row
#print("cols",arr[0][0],arr[0][1],arr[0][2]) #prints elements in the first row, 0th, 1st and 2nd column

print(arr.ndim) #returns the array dimension
print(arr.shape) #returns the (rows,col)
print(arr.size) #row*cols technically the total elements in the matrix

print(arr.dtype) # data type, int64- integer, 64 bits

'''
'''
#creating a basic array
#1. np.zeros() : create an array filled with 0’s

zeroarr=np.zeros(5)     #[0. 0. 0. 0. 0.]
print(zeroarr) 

#2. np.ones() : create an array filled with 1’s

onearr=np.ones(4)       #[1. 1. 1. 1.]
print(onearr)

#3. np.empty() : even an empty array! The function empty 
#creates an array whose initial content is random and depends on the state of the memory.

emparr=np.empty(5)              #[ 1.    2.75  6.   10.75 17.  ]
print(emparr)                   #random one time assignment
q
#4. np.arange() : create an array with a range of elements:

arngarr=np.arange(7)            #[0 1 2 3 4 5 6]
print(arngarr)                  #initialises the array in order till the (input value-1)

arnggarr=np.arange(1,5,2)            #(start,stop,step)
print(arnggarr)                     #[1 3]

'''


