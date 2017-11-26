import math


def distance(x=0, y=0, x1=0, y1=0):
    distance = math.sqrt(pow((x - x1), 2) + pow((y - y1), 2))
    return distance


def fspl(distance=0, frequency=0):
    FSPL = 20 * math.log10(distance) + 20 * math.log10(frequency) - 27.55
    return FSPL


def rssi_distance(tx_power=0, rssi=0):
    distance = pow(10, ((tx_power - rssi) / 20))
    return distance


def rssi(distance=0, tx_power=0):
    RSSI = -20 * math.log10(distance) + tx_power
    return RSSI
