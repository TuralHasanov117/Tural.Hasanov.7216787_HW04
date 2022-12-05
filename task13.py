import numpy as np

def main():
  matrix = np.arange(16).reshape(4, 4)
  print("Matrix: \n", matrix)
  rank = np.linalg.matrix_rank(matrix)
  print("Rank: \n", rank)
  

if __name__ == "__main__":
    main()
