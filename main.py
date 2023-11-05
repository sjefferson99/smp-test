from time import gmtime
from multicore import Multicore_Weather_Wind

mw = Multicore_Weather_Wind()
mw.init_wind_poll_thread()

print("Waiting for wind_data to be ready")
while True:
  if mw.check_pending_wind_data_length() > 1:
    datapoints = mw.get_pending_data()
    for datapoint in datapoints:
      timestamp = datapoint["timestamp"]
      wind_speed = datapoint["avg_speed"]
      wind_gust = datapoint["gust_speed"]
      print("Wind speed for timestamp {} : {} m/s".format(timestamp, str(round(wind_speed, 2))))
      print("Wind gust for timestamp {} : {} m/s".format(timestamp, str(round(wind_gust, 2))))
    mw.clear_pending_data()