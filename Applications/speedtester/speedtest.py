
import speedtest
from datetime import datetime
import json

"""
Suit those variables to your situation
"""
### Variables
Database_json = "F:\database\speedtest-data.json"
Database_txt = "F:\database\speedtest-data-human-readable.txt"
Times_speedtest_is_performed = 2
###


def shift(num,n):
  return round((num / (10**n)),2)

def tester():
  date,hour = tuple(datetime.now().strftime("%b-%d-%Y,%H:%M:%S").split(","))
  date = date + " " + hour
  s = speedtest.Speedtest()
  upload = shift(s.upload(),6)
  download = shift(s.download(),6)
  ping = s.results.dict()["ping"]
  text = {"id": date ,"upload-speed": upload,"download-speed": download,"ping-latency": ping}
  with open(Database_json,"a") as f:
    json.dump(text,f)
  with open(Database_txt,"a") as f:
    f.write(str(text)+"\n")
  return 0


for i in range(Times_speedtest_is_performed):
  tester()
