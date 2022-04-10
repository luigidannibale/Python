
import speedtest
from datetime import datetime
import json

"""
Change those variables as you please
"""
### Variables
Database_json = "F:\database\speedtest-data.json"
Database_txt = "F:\database\speedtest-data-human-readable.txt"
Times_speedtest_is_performed = 2
###


def shift(numero,n):
  return round((numero / (10**n)),2)

def tester():
  data,ora = tuple(datetime.now().strftime("%b-%d-%Y,%H:%M:%S").split(","))
  data = data + " " + ora
  s = speedtest.Speedtest()
  upload = shift(s.upload(),6)
  download = shift(s.download(),6)
  ping = s.results.dict()["ping"]
  text = {"id": data ,"upload-speed": upload,"download-speed": download,"ping-latency": ping}
  with open(Database_json,"a") as f:
    json.dump(text,f)
  with open(Database_txt,"a") as f:
    f.write(str(text)+"\n")
  return 0


for i in range(Times_speedtest_is_performed):
  tester()
