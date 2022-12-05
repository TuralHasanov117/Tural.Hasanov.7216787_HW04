from matplotlib import pyplot as plt
import numpy as np
import random

def integerGenerator():
  numbers = [random.randint(10, 100) for i in range(1,11)]
  return numbers

def main():
  arr = np.array(integerGenerator())
  print(arr)
  plt.pie(arr, labels=[str(i) for i in arr])
  plt.show()
  
if __name__ == "__main__":
    main()
