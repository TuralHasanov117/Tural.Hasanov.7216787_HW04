import numpy as np

def main():
  matrix1 = np.arange(15).reshape(5, 3) 
  print("Matrix 5x3: \n", matrix1)
  matrix2 = np.arange(6).reshape(3, 2) 
  print("\nMatrix 3x2: \n",matrix2)
  product = np.dot(matrix1, matrix2)
  print("\nMatrix product: \n", product)
  

if __name__ == "__main__":
    main()
