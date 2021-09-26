import datetime
import random
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def odds_or_evens(check):
    result = ''
    for i in range(1,101):
        if i%2==0 and check:
            result += str(i) + ' '
        elif i%2!=0 and check==False:
            result += str(i) + ' '
    return result

def possible_error():
    x = random.randint(1,30)
    y = random.randint(0,1)
    print(f"Trying operation {x}/{y}...")
    try:
        result = x/y
    except ZeroDivisionError:
        return 0
    else:
        return  1