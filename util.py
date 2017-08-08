import signal
import requests
import time

class show:
 def heartBeat(self):
  print "Sending HeartBeat"
  response = requests.get("http://localhost:80/")
  print "Status : " + str(response.status_code)
  print response.text
  print "Heartbeat completed"
