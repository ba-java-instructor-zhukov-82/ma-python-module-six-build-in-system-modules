##Laboratory Work 6.6.

Create a module with name my_time.py with next code implementation:

* Import time and datetime modules
* After import statement set clock count for checking script execution time
* Print current time in format 'Tue May 24 14:09:17 2016’
* Print current time year
* Print current time day from the year begining
* Use time tuple convertion into string and create string line with next
  format '24 Mar 2015 12:14‘
* Use time convertion from string into time tuple and create object from
  string '19 Sep. 2012 10:15'
* Create datetime tuple with cureent day minus one day
* Check the difference with datime delta
* Print script execution time

####Here is the solution code:

*solution_6_6.py*

```python
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
```
