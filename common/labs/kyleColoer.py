from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait
from umath import ceil

# Set up all devices.
prime_hub = PrimeHub()
color_sensor = ColorSensor(Port.E)
color_sensor2 = ColorSensor(Port.F)


# The main program starts here.
while True:
    wait(1000)
    sensor1_h = color_sensor.hsv().h
    sensor1_s = color_sensor.hsv().s
    sensor1_v = color_sensor.hsv().v

    sensor2_h = color_sensor2.hsv().h
    sensor2_s = color_sensor2.hsv().s
    sensor2_v = color_sensor2.hsv().v

    hueAvg = ceil((sensor1_h + sensor2_h) / 2)
    satAvg = ceil((sensor1_s + sensor2_s) / 2)
    valAvg = ceil((sensor1_v + sensor2_v) / 2)

    color = color_sensor.color()

    if (hueAvg >= 334 and hueAvg <= 338 and satAvg >= 78 and satAvg <= 80 and valAvg >= 61 and valAvg <= 65):
        color = 'MAGENTA'

    ## We only use sensor 1 for orange
    elif (sensor1_h >= 12 and sensor1_h <= 16 and sensor1_s >= 65 and sensor1_s <= 73 and sensor1_v >= 99 and sensor1_v <= 101):
        color = 'ORANGE'

    print("Sensor 1:", color, sensor1_h, sensor1_s, sensor1_v)
    print("Sensor 2:", color, sensor2_h, sensor2_s, sensor2_v)
