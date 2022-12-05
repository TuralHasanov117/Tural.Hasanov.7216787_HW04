import numpy as np

def main():
  arr1 = np.random.rand(10)
  arr2 = np.random.rand(10)
  print("Random array A", arr1)
  print("Random array B", arr2)
  if np.array_equal(arr1, arr2):
    print("Equal")
  else:
    print("Not equal")
  

if __name__ == "__main__":
    main()
