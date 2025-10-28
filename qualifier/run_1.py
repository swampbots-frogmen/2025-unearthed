from tadpoleBot import robot, rotation, square_up, wheel_diameter, motorC, motorD, wait
from pybricks.parameters import Stop

robot.settings(straight_acceleration=550,straight_speed=600)
robot.use_gyro(True)

# Square up against wall to start
square_up()

#motorC.run_angle(3000,15)
# lower lever to start at 0
motorC.run_angle(3000,-60)
# raise lever to hit brush
robot.straight(3 * wheel_diameter * 3.14159)
# Go towards brush and hit one side
robot.turn(15)
# slight turn towards mineshaft
robot.straight(0.9 * wheel_diameter * 3.14159)
# slight movement to get away from brush
robot.turn(75)
# finish turn towards mineshaft
robot.settings(straight_acceleration=700,straight_speed=700)

motorC.run_angle(3000, 50)
# lower lever
robot.straight(2 * wheel_diameter * 3.14159)
# go towards miner
robot.settings(straight_acceleration=150,straight_speed=150)

# lift mineshaft
motorC.run_angle(3000,-80)

motorD.run_angle(3000, 90)

robot.settings(straight_acceleration=550,straight_speed=600)

robot.straight(-1.6 * wheel_diameter * 3.14159)
# back up towards map reveal
motorC.run_angle(3000,-110)
# adjust lever to reveal map
robot.turn(-90)
# turn to begin map approach
robot.straight(-0.75 * wheel_diameter * 3.14159)
# back up to adjust entry angle
robot.turn(-45)
# turn towards map mission
#motorC.run_angle(3000,-30)
# adjust lever arm to get map reveal
robot.settings(straight_acceleration=150,straight_speed=150)

robot.straight(2.1 * wheel_diameter * 3.14159)
# move towards map reveal
motorC.run_angle(150,120)
# lift map reveal
robot.straight(-0.9 * wheel_diameter * 3.14159)
# back up from map reveal
robot.turn(45)
# turn towards brush
motorC.run_angle(150,60)
# adjust lever for brush
robot.settings(straight_acceleration=550,straight_speed=600)
robot.straight(-1 * wheel_diameter * 3.14159)
robot.straight(1.5 * wheel_diameter * 3.14159)
robot.straight(-0.9 * wheel_diameter * 3.14159)
# back up and activate brush
motorC.run_angle(100,-40, then=Stop.HOLD)
# lift up brush
robot.straight(-3.3 * wheel_diameter * 3.14159)
# back up to red home
