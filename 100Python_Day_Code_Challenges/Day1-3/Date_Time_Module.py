import datetime
                            # Datetime.date #

# get the date format
d = datetime.date(2018, 8, 5)
print(d)

# today(): get today date
today = datetime.date.today()
print(today)
print(today.day)
print(today.year)
print(today.weekday())          # Monday 0 # Sunday 6
print(today.isoweekday())       # Monday 1 # Sunday 7
print("=====================================")
                        # Datetime.timedelta #
# timedelta = to make mathematical operations
timedleta = datetime.timedelta(days=7)
print(today + timedleta)
print("=====================================")
                         # My birthday is coming! #
birthday = datetime.date(2020, 8, 27)
tell_birthday = birthday - today
print(tell_birthday.days)
print("=====================================")
                            # datetime.time #
time = datetime.time(5, 34, 32)
print(time)

print("=====================================")
                            # datetime.datetime #
# datetime: get the date along with the time
dt = datetime.datetime(2020, 12, 5, 9, 2, 3)
print(dt)
print(dt.date())    # date only
print(dt.time())    # time only
print(dt + timedleta)


dt_today = datetime.datetime.today() # the currnet local time with no timezone
dt_now = datetime.datetime.now()    # the currnet local time with option to add timezone
dt_utcnow = datetime.datetime.utcnow() # # the currnet utc time

print(dt_today)
print(dt_now)
print(dt_utcnow)

                        # Using TimeZones #
import pytz

# Time zone aware
pytz1 = datetime.datetime.now(tz=pytz.UTC)
print(pytz1)

# Change TimeZones
change = pytz1.astimezone(pytz.timezone('US/Mountain'))
print(change)
                            # Convert datetime to str #
dt = datetime.datetime(2020, 12, 5, 9, 2, 3)
print(dt.strftime("%B %d, %Y"))


                            # Convert str to datetime format #
dt_str = 'July 26, 2020'

Convert = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(Convert)
