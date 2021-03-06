#! coding: utf-8
import time  # import time module
import datetime  # import datetime module

time.clock()  # Set clock start

print(time.ctime())  # print current time in format 'Tue May 24 14:09:17 2016’
print(time.localtime().tm_year)  # Current time year
print(time.localtime().tm_yday)  # Current year day

print(time.strftime("%d %m. %Y %H:M",time.gmtime()))
print(datetime.datetime.strptime("19 Sep. 2012 10:15", "%d %b. %Y %H:%M"))
time_1 = datetime.datetime.now() + datetime.timedelta(days = -1)   # Create datetime tuple with current day minus one day
now = datetime.datetime.now()
print('Time delta', (now - time_1).days)  # Check the difference with time delta

print("Script execution time: %f4.2" % time.clock())
