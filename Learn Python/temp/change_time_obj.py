import time
import calendar

'''
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
'''

str_time = "15/Apr/2019:00:06:47".split("/")
str_time[1] = list(calendar.month_abbr).index(str_time[1])
print(str_time)

# for v in str_time:
#     print(v)
my_time_str = '-'.join([str(v) for v in str_time])
# print(my_time_str)
time_obj = time.strptime(my_time_str, "%d-%m-%Y:%H:%M:%S")
# print(time_obj)
str_time = time.strftime("%Y-%m-%d-%H", time_obj)
print(str_time)
# print(list(calendar.month_abbr).index("Apr"))
