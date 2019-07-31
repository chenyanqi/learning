import julian
import datetime

mjd = 1564551630
dt = julian.from_jd(mjd, fmt='mjd')
print(dt)