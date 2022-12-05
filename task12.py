import numpy as np

def main():
  arr = np.random.random((3,3)) * 10
  print("Original array: \n", arr)
  column = 1 # sort by column number 1
  arr = arr[arr[:,column].argsort()] 
  print("Sorted array: \n", arr)
  

  

if __name__ == "__main__":
    main()
