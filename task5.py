import numpy as np

def main():
  today = np.datetime64('today', 'D')
  yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  tomorrow =np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  print("Today: ", today)
  print("Yesterday: ", yesterday)
  print("Tomorrow: ", tomorrow)
  

if __name__ == "__main__":
    main()
