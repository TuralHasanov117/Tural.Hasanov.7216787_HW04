import numpy as np

def main():
  matrix = np.random.rand(3, 4)
  print("Matrix: \n", matrix)
  result = matrix - matrix.mean(axis=1, keepdims=True)
  print("\nResult: \n", result)
  
  

if __name__ == "__main__":
    main()
