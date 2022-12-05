import numpy as np

def main():
  arr = np.random.rand(5,5) * 10
  print("Random 5x5 array: ", arr)
  minVal = np.amin(arr)
  print("Minimum value: ", minVal)
  maxVal = np.amax(arr)
  print("Maximum value: ",maxVal)
  

if __name__ == "__main__":
    main()
