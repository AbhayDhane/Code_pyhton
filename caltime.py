import numpy as np
import time

# size of arrays and lists
size = 100000

# declaring lists
list1 = range(size)
list2 = range(size)

# declaring arrays
array1 = np.arange(size)
array2 = np.arange(size)

# capturing time before the multiplication of Python lists
initialTime = time.time()

# multiplying  elements of both the lists and stored in another list
resultantList = [(a * b) for a, b in zip(list1, list2)]

# calculating execution time
print("Time taken by Lists to perform multiplication:",
      (time.time() - initialTime),
      "seconds")

# capturing time before the multiplication of Numpy arrays
initialTime = time.time()

# multiplying  elements of both the Numpy arrays and stored in another Numpy array
resultantArray = array1 * array2

# calculating execution time
print("Time taken by NumPy Arrays to perform multiplication:",
      (time.time() - initialTime),
      "seconds")
