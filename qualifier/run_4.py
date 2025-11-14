from tadpoleBot import robot, motorD, rotation, square_up
from pybricks.parameters import Stop

'''
Run 4 - Describe what it does
Home: Blue
Attachment: Name of the attachment
Engineer: Evan
Authors: Who coded this run (name all)
'''

def R4_run():
    robot.use_gyro(True)
    robot.settings(straight_acceleration=550, straight_speed=500)

    square_up()

    #prepare the arm
    motorD.run_angle(700,180)
    # go toward the silo
    robot.straight(2.5 * rotation)
    # hit the preseved pieces out of the silo
    motorD.run_angle(400,-162, then=Stop.HOLD)
    motorD.run_angle(400,160, then=Stop.HOLD)
    motorD.run_angle(400,-162, then=Stop.HOLD)
    motorD.run_angle(400,160, then=Stop.HOLD)
    motorD.run_angle(400,-162, then=Stop.HOLD)
    motorD.run_angle(400,160, then=Stop.HOLD)
    # make the 
    robot.settings(straight_acceleration=400, straight_speed=500)
    # leave the silo
    robot.straight(-0.3 * rotation) 
    # turn toward the market wares 
    robot.turn(-80)
    # Head toward the market wares
    robot.straight(1.7 * rotation)

    # turn to 
    robot.turn(-45)
    # Lift the market table 
    robot.settings(straight_acceleration=200, straight_speed=200)
    # adjust the speed to go slower
    robot.straight(2.75 * rotation)
    # change the speed back to normal
    robot.settings(straight_acceleration=400, straight_speed=500)
    # turn to solve the seal
    robot.turn(87)
    # drive toward the seal
    robot.straight(2.4 * rotation)
    # hit the seal
    motorD.run_angle(2000, -190)
    # leave the seal
    robot.straight(-0.5 * rotation)
    # turn to go home
    robot.turn(-80)
    # adjust lever
    motorD.run_angle(2000, 50)
    # go home
    robot.straight(5 * rotation)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R4_run()
