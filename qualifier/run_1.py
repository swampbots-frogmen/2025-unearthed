from tadpoleBot import robot, rotation, square_up, wheel_diameter, motorC, motorD, wait
from pybricks.parameters import Stop

'''
Run 1 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R1_run():
    robot.settings(straight_acceleration=450,straight_speed=600)
    robot.use_gyro(True)

    # Square up against wall to start
    square_up()

    # raise lever to hit brush
    motorC.run_angle(3000,-60)
    # Go towards brush and hit one side
    robot.straight(3 * wheel_diameter * 3.14159)
    # slight turn towards mineshaft
    robot.turn(15)
    # slight movement to get away from brush
    robot.straight(0.9 * wheel_diameter * 3.14159)
    # finish turn towards mineshaft
    robot.turn(75)
    robot.settings(straight_acceleration=450,straight_speed=450)

    # lower lever
    motorC.run_angle(3000, 50)
    # go towards miner
    robot.straight(2 * wheel_diameter * 3.14159)

    # 
    robot.settings(straight_acceleration=150,straight_speed=150)

    # lift mineshaft
    total_rotation = -80
    lift_rotation = 0.67 * total_rotation

    motorC.run_angle(3000, lift_rotation)

    wait(1000)

    motorC.run_angle(3000, total_rotation - lift_rotation)

    motorD.run_angle(3000, 90)

    # back up towards map reveal
    robot.settings(straight_acceleration=550,straight_speed=600)
    # adjust lever to reveal map 
    robot.straight(-1.55 * wheel_diameter * 3.14159)
    motorC.run_angle(3000,-110)
   
    # turn to begin map approach
    robot.turn(-90)
    # back up to adjust entry angle
    robot.straight(-0.85 * wheel_diameter * 3.14159)
    # turn towards map mission
    robot.turn(-45)
    # adjust lever arm to get map reveal
    robot.settings(straight_acceleration=150,straight_speed=150)

    # move towards map reveal
    robot.straight(2.1 * wheel_diameter * 3.14159)
    # lift map reveal
    motorC.run_angle(150,120)
    # back up from map reveal
    robot.straight(-0.9 * wheel_diameter * 3.14159)
    # turn towards brush
    robot.turn(45)
    # back up from map reveal
    robot.straight(-0.2 * wheel_diameter * 3.14159)

    motorC.run_angle(3000,80)

    robot.settings(straight_acceleration=450,straight_speed=550)
    
    robot.straight(0.4 * wheel_diameter * 3.14159)

    robot.straight(-0.8 * wheel_diameter * 3.14159)
    

    motorC.run_angle(150,-60)
    robot.straight(-3.5 * wheel_diameter * 3.14159)

    '''
    # adjust lever for brush
    motorC.run_angle(150,60)
    robot.settings(straight_acceleration=450,straight_speed=600)

    #robot.straight(1.5 * wheel_diameter * 3.14159)
    #robot.straight(-1 * wheel_diameter * 3.14159)
    #robot.straight(0.35 * wheel_diameter * 3.14159)
    # back up and activate brush
    motorC.run_angle(100,-40, then=Stop.HOLD)
    # lift up brush
    robot.straight(-3.4 * wheel_diameter * 3.14159)
    # back up to red home
    '''

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R1_run()