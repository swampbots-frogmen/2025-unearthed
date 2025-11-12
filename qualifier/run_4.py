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
    robot.settings(straight_acceleration=400, straight_speed=500)
    # leave the silo
    robot.straight(-0.3 * rotation) 
    # turn toward the market wares 
    robot.turn(-80)
    # Head toward the market wares
    robot.straight(1.8 * rotation)
    # Lift the market table
    robot.turn(-45)
    robot.straight(2.9 * rotation)
    # turn to solve the seal
    robot.turn(88)
    # drive toward the seal
    robot.straight(2.2 * rotation)
    motorD.run_angle(2000, -180)
    # leave the seal
    robot.straight(-0.5 * rotation)
    robot.turn(-80)
    motorD.run_angle(2000, 50)
    robot.straight(5 * rotation)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R4_run()
