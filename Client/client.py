import signal
import requests
import time
from util import show

def sigint_handler(signum, frame):
  print 'Handling CTRL+C!'
  exit()



def main():
  print "Client started"
  while True:
    Show= show()
    Show.heartBeat()
    time.sleep(10)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
  main()
