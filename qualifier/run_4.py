from tadpoleBot import robot, motorD, rotation, square_up
from pybricks.parameters import Stop

'''
Run 4 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R4_run():
    robot.use_gyro(True)
    robot.settings(straight_acceleration=660, straight_speed=500)

    square_up()

    #prepare the arm
    motorD.run_angle(700,180)
    # go toward the silo
    robot.straight(2.5 * rotation)
    # hit the preseved pieces out of the sil
    motorD.run_angle(400,-162, then=Stop.HOLD)
    motorD.run_angle(400,160, then=Stop.HOLD)
    motorD.run_angle(400,-162, then=Stop.HOLD)
    motorD.run_angle(400,160, then=Stop.HOLD)
    # motorD.run_angle(400,-162)
    # motorD.run_angle(400,80)
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

    # robot.straight(-0.8 * rotation)
    # robot.turn(-40)
    # robot.straight(2 * rotation)
    # robot.turn(90)
    # robot.straight(3.3 * rotation)
    # robot.turn(41)

    # turn to solve the seal
    robot.turn(88)
    # drive toward the seal
    robot.straight(2.07 * rotation)
    motorD.run_angle(2000, -180)
    motorD.run_angle(2000, 50)
    # leave the seal
    robot.turn(-92)
    motorD.run_angle(2000, 50)
    robot.straight(5 * rotation)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R4_run()
