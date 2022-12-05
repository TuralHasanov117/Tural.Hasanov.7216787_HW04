import numpy as np

def main():
  arr = np.array([np.array([np.random.randint(0, high=20, size=2, dtype=int), np.random.randint(0, high=255, size=3, dtype=int)]) for x in range(1,10)])
  print(arr)
  

if __name__ == "__main__":
    main()
