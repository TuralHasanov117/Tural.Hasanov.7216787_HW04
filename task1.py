import numpy as np

def main():
  vector = np.arange(10, 50)
  print("Original vector: ",vector)
  vector = np.flip(vector)
  print("\nResulting vector: ", vector)

if __name__ == "__main__":
    main()
