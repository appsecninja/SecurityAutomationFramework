import signal
import requests
import time

def sigint_handler(signum, frame):
  print 'Handling CTRL+C!'
  exit()

def heartBeat():
  print "Sending HeartBeat"
  response = requests.get("http://localhost:80/")
  print "Status : " + str(response.status_code)
  print response.text
  print "Heartbeat completed"

def main():
  print "Client started"
  while True:
    heartBeat()
    time.sleep(10)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
  main()
