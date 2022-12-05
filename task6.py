import numpy as np
import matplotlib.pyplot as plt

def main():
  arr = np.random.uniform(low=0.5, high=13.3, size=(5,))
  print("Random array: \n", arr)
  
  # Method 1
  result1 = arr.astype(int)
  print("Method 1 result array: ", result1)
  
  # Method 2
  result2 = np.int_(arr)
  print("Method 2 result array: ", result2)
  
  # Method 3
  result3 = np.array([int(a) for a in arr])
  print("Method 3 result array: ", result3)

  # Method 4
  result4 = np.array(list(map(int, arr)))
  print("Method 4 result array: ", result4)
  
  # Method 5
  result5 = np.array(arr, int)
  print("Method 5 result array: ", result5)

  plt.pie(arr, labels=["Number 1", "Number 2", "Number 3", "Number 4", "Number 5"], shadow = True)
  plt.show()
  

if __name__ == "__main__":
    main()
