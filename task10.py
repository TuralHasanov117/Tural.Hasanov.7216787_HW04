import numpy as np

def main():
  a = np.random.random((100,2))
  print("Random vector: \n", a)
  x,y = np.atleast_2d(a[:,0], a[:,1])
  d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
  print("Point by point distances: \n", d)
  

if __name__ == "__main__":
    main()
