
class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        minutes=hour*60+minute
        seconds=minutes*60+second
        self.second=seconds

    def __str__(self):
        hour,minute,second=self.int_to_time()
        return '%.2d:%.2d:%.2d' % (hour,minute,second)

    def print_time(self):
        hours,minutes,seconds=self.int_to_time()
        print '%.2d:%.2d:%.2d' % (hours, minutes, seconds)

    def int_to_time(self):
        """Computes the number of seconds since midnight."""
        minutes,seconds=divmod(self.second,60)
        hours,minutes=divmod(minutes,60)
        return hours,minutes,seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.second > other.second

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.second + other.second
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.second
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        hour,minute,second=self.int_to_time()
        if hour < 0 or minute < 0 or second < 0:
            return False
        if minute >= 60 or second >= 60:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end

    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start

    print 'Example of polymorphism'
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total


if __name__ == '__main__':
    main()
