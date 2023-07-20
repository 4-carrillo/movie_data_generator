from random import random
from time import (
    mktime,
    strftime,
    strptime,
    localtime
)
    
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = mktime(strptime(start, time_format))
    etime = mktime(strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return strftime(time_format, localtime(ptime))


def random_date(start, end):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', random())