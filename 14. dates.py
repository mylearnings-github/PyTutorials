import datetime

""" 1. About Dates """

''' Naive datetime doesn't have time zone information '''

d = datetime.date(2016, 6, 27)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) # Monday 0 Sunday 6
print(today.isoweekday()) # Monday 1 Sunday 7


''' Time delta difference b/w two dates/times '''

delta_days = datetime.timedelta(days = 7)
print(today + delta_days)

delta_minute = datetime.timedelta(minutes = 10)
print(today + delta_days)

""" 
    Hint:
    ----
    1) date2 = date 1 + timedelta
    2) timedelta = date1 + date2

"""
today = datetime.date.today()
b_day = datetime.date(2022, 9, 6)
till_bday = b_day - today # Returns a delta value, as shown in hint 2
print(till_bday.days)
print(till_bday.total_seconds())


""" 2. About Times """
t = datetime.time(9, 30, 00, 000)
print(t.hour)

""" 3. About Date & Time """
dt = datetime.datetime(2022, 9, 6, 6, 0, 0, 000)
print(dt)

tdelta = datetime.timedelta(hours = 6)
future_dt = dt + tdelta
print(future_dt)

""" 4. Alternatives constructors which comes with date/time """

''' 
    Hint:
    -----
    1) today - no time zone setting possible
    2) now - timezone setting possible
    3) utcnow - no timezone setting possible
'''
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


""" 5. Timezones using pytz """
import pytz
dt = datetime.datetime(2022, 3, 17, 12, 57, 0, 000, tzinfo= pytz.UTC)

''' To Get current UTC times '''
dt_now = datetime.datetime.now(tz=pytz.UTC) # Preferred way
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) # Possible, but not recommended
print(dt_utcnow)

""" 5. Convert UTC timezone to my timezone """

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_ind = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ind)

''' Reference: '''
print(pytz.all_timezones)

# Searching within pytz available timezone to find a tz relevant to India
for tz in pytz.all_timezones:
    if tz.lower().__contains__('us'):
        print(tz)


""" 6. Convert local/naive timezone to my specified timezone """

# System understands my time as India, even if I say it's australia
dt_aus = datetime.datetime.today()
print(dt_aus)

# But I can explicitly say Aus/Syd is my local timezone
aus_tz = pytz.timezone('Australia/Sydney')
dt_aus = aus_tz.localize(dt_aus)
print(dt_aus) # This result has aus timezone info at the end

# Trying to convert my aus time zone to US East
dt_us_east = dt_aus.astimezone(pytz.timezone('US/Eastern'))
print(dt_us_east)


""" 7. Standard & Custom Datetime Formats """

dt_ind = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt_ind)
print(dt_ind.isoformat())
print(dt_ind.strftime('%B %d, %Y - %I:%M:%S %p')) #String format time

''' 
    No need to remember these things, as you can always refer it from python documentation
    Refer: https://docs.python.org/3.9/library/datetime.html#strftime-and-strptime-behavior


    Note:
    -----
    1) strftime - Datetime to String
    2) strptime - String to Datetime

'''
# Convert datetime to our required string format
dt_ind_str = dt_ind.strftime('%B %d, %Y - %I:%M:%S %p')
print(dt_ind_str)
type(dt_ind_str)

# Convert string datetime to datetime format
dt = datetime.datetime.strptime(dt_ind_str, '%B %d, %Y - %I:%M:%S %p')
print(dt)
type(dt)