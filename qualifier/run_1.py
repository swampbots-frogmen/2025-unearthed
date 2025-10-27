from tadpoleBot import robot, rotation, square_up, motorC
from pybricks.parameters import Stop

'''
Run 1 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R1_run():
    robot.settings(550, 600)
    robot.use_gyro(True)

    # Square up against wall to start
    square_up()

    #motorC.run_angle(3000,15)
    # lower lever to start at 0
    motorC.run_angle(3000, -60)
    # raise lever to hit brush
    robot.straight(3 * rotation)
    # Go towards brush and hit one side
    robot.turn(15)
    # slight turn towards mineshaft
    robot.straight(0.9 * rotation)
    # slight movement to get away from brush
    robot.turn(75)
    # finish turn towards mineshaft
    robot.settings(700, 700)

    motorC.run_angle(3000, 50)
    # lower lever
    robot.straight(2.1 * rotation)
    # go towards miner
    robot.settings(150, 150)

    motorC.run_angle(3000, -80)
    # lift mineshaft
    robot.settings(550, 600)

    robot.straight(-1.75 * rotation)
    # back up towards map reveal
    motorC.run_angle(3000, -110)
    # adjust lever to reveal map
    robot.turn(-90)
    # turn to begin map approach
    robot.straight(-0.75 * rotation)
    # back up to adjust entry angle
    robot.turn(-45)
    # turn towards map mission
    motorC.run_angle(3000, -30)
    # adjust lever arm to get map reveal
    robot.settings(150, 150)

    robot.straight(2.1 * rotation)
    # move towards map reveal
    motorC.run_angle(500,120)
    # lift map reveal
    robot.straight(-0.9 * rotation)
    # back up from map reveal
    robot.turn(45)
    # turn towards brush
    motorC.run_angle(250,70)
    # adjust lever for brush
    robot.settings(550, 600)
    robot.straight(-1 * rotation)
    robot.straight(1 * rotation)
    robot.straight(-0.5 * rotation)
    # back up and activate brush
    motorC.run_angle(100, -20, then=Stop.HOLD)
    # lift up brush
    robot.straight(-3 * rotation)
    # back up to red home

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R1_run()