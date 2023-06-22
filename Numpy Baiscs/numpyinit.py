import numpy as np

mylist = [1,2,3]

berkay = np.array(mylist)

print(berkay)
print(type(berkay))

two_d_array = np.zeros(shape=(5,5)) #ones would do it too

print(two_d_array)

np.random.seed(101)
some_array = np.random.randint(1,100,10)

print(some_array)

print(some_array.argmax())

print(some_array.argmin())

print(some_array.mean())

new_array = some_array.reshape((5,2))

print(new_array)

some_matrix = np.arange(0,100).reshape((10,10))

print(some_matrix)

print(some_matrix[4][2]) # can do [4,2]