import numpy as np

def main():
  array = np.arange(256).reshape(16, 16)
  print(array)
  blockSize = 4
  blockSum = np.add.reduceat(np.add.reduceat(array, np.arange(0, array.shape[0], blockSize), axis=0), 
                             np.arange(0, array.shape[1], blockSize), axis=1)
  print(blockSum)
  
if __name__ == "__main__":
    main()
