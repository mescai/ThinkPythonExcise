
class Time(object):
    """
    Reprensents the time of day.
    arrtibutes:hour,minute,second
    """
def print_time(time):
    print "%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second)

def is_after(t1,t2):
    return transfer_to_seconds(t1)-transfer_to_seconds(t2)>0

def transfer_to_seconds(t):
    return t.hour*3600+t.minute*60+t.second

def create_time(hour,minute,second):
    t=Time()
    t.hour=hour
    t.minute=minute
    t.second=second
    return t

def add_time(t1,t2):
    sum=Time()
    sum.hour=t1.hour+t2.hour
    sum.minute=t1.minute+t2.minute
    sum.second=t1.second+t2.second

    if sum.second>=60:
        sum.second-=60
        sum.minute+=1
    if sum.minute>=60:
        sum.minute-=60
        sum.hour+=1

    return sum

def increment(time,seconds):
    """
    add a given seconds to the time object
    :param time: the given time object
    :param seconds: a given second
    :return: new time
    """
    time.second+=seconds

    [m,s]=divmod(time.second,60)
    time.minute+=m
    time.second=s
    [ho,mi]=divmod(time.minute,60)
    time.hour+=ho
    time.minute=mi
    return time

def increment_pure_function(time,seconds):
    t=Time()
    t.second=time.second+seconds

    m,s=divmod(t.second,60)
    t.minute=time.minute+m
    t.second=s
    ho,mi=divmod(t.minute,60)
    t.hour=time.hour+ho
    t.minute=mi
    return t

def time_to_int(time):
    minutes=time.hour*60+time.minute
    seconds=minutes*60+time.second
    return seconds


def add_time1(t1,t2):
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)

def increment1(t1,seconds):
    sec=time_to_int(t1)+seconds
    return int_to_time(sec)

def valid_time(time):
    if time.hour<0 or time.minute<0 or time.second<0:
        return False
    if time.minute>=60 or time.second>=60:
        return False
    return True

def add_time2(t1,t2):
    assert valid_time(t1) and valid_time(t2)
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)

def mul_time(time,n):
    assert valid_time(time)
    seconds=time_to_int(time)
    seconds=seconds*n
    return int_to_time(seconds)

def eve_time(time,n):
    n=1/n
    return mul_time(time,n)

import datetime

def print_weekday():
    nowtime=datetime.datetime.now()
    print nowtime
    print "Today is %d" %(nowtime.isoweekday())

def print_age(birthday):
    today=datetime.datetime.today()
    birth=datetime.datetime.strptime(birthday,"%Y-%m-%d")
    nextbirth=datetime.datetime(today.year,birth.month,birth.day)

    age=today.year-birth.year
    if nextbirth<today:
        print "Age is %d." %(age)
        nextbirth.year+=1
    else:
        print "Age is %d." %(age-1)

    print "Days until next birthday is %d" %(nextbirth-today).days

def double_age(birthday1,birthday2,n):
    birth1=datetime.datetime.strptime(birthday1,"%Y-%m-%d")
    birth2=datetime.datetime.strptime(birthday2,"%Y-%m-%d")
    assert birth1>birth2
    delta=birth1-birth2
    delta1=datetime.timedelta(delta.days/((n-1)*1.0))
    return birth1+delta1


if __name__=="__main__":
    birthday1="2014-10-20"
    birthday2="2012-10-18"
    print double_age(birthday1,birthday2,10)