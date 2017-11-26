import math


def distance(x=0, y=0, x1=0, y1=0):
    distance = math.sqrt(pow((x - x1), 2) + pow((y - y1), 2))
    return distance

def fslp(distance=0, frequency=0):
    FSPL = 20 * math.log10(distance) + 20 * math.log10(frequency) - 27.55
    return FSPL
