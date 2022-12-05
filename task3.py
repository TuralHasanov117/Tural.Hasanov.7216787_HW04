import numpy as np

def main():
  matrix = np.arange(25).reshape(5, 5) 
  print("Random matrix: \n", matrix)
  row_sums = matrix.sum(axis=1)
  new_matrix = matrix / row_sums[:, np.newaxis]
  print("\nNormalized matrix: \n",new_matrix)
  

if __name__ == "__main__":
    main()
