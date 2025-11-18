from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Button, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task

# Initialize the hub, motors, and drive base
hub = PrimeHub()

# This makes the menu program totally stop when the bluetooth button is pressed
hub.system.set_stop_button(Button.BLUETOOTH)

Tanner = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Grayson = Motor(Port.B, Direction.CLOCKWISE)
motorC = Motor(Port.C)
motorD = Motor(Port.D)
Tanner.dc(60)
Grayson.dc(60)
wheel_diameter = 56  # Adjust based on our robot's wheel diameter in mm
axle_track = 120  # Adjust based on our robot's axle track in mm
rotation = wheel_diameter * 3.14159

robot = DriveBase(Tanner, Grayson, wheel_diameter, axle_track)
robot.settings(turn_acceleration=200)

async def square_up():
    robot.drive(-300, 0)
    await wait(500)
    robot.stop()

async def run_motorC(speed, angle):
    await motorC.run_angle(speed, angle)

async def drive_straight(rotations):
    await robot.straight(rotations * rotation)

async def turn(degrees):
    await robot.turn(degrees)
