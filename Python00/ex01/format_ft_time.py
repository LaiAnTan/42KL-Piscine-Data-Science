import time as time
import datetime as dt

curr_time = time.time()

date = dt.datetime.now()

print(f"Seconds since January 1, 1970: {curr_time:,.4f} or {curr_time:e}" +
      " in scientific notation")
print(date.strftime("%b %d %Y"))
