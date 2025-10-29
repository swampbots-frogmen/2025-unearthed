from tadpolebot import robot, rotation, square_up, wheel_diameter

'''
Run 2 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R2_run():
    robot.use_gyro(True)

    robot.settings(straight_acceleration=660,straight_speed=660)

    robot.straight(2.25 * wheel_diameter * 3.14159)
    #go towards sand 
    robot.straight(-1 * wheel_diameter * 3.14159)
    #pull back lever
    robot.turn(-45)
    #turn to boat lever
    robot.straight(1 * wheel_diameter * 3.14159)
    #push boat lever
    robot.turn(35)

    robot.straight(0.9 * wheel_diameter * 3.14159)
    #push boat lever
    robot.turn(-30)
    #turn away from boat
    robot.straight(1.5 * wheel_diameter * 3.14159)
    #go past boat
    robot.turn(90)
    #turn towards lift
    robot.straight(1.2 * wheel_diameter * 3.14159)
    #go towards lift
    robot.turn(30)
    #activate lift lever
    robot.turn(-30)

    robot.turn(30)

    robot.turn(-30)

    robot.turn(30)

    robot.turn(-30)
    #finish activating lever
    robot.straight(-1.5 * wheel_diameter * 3.14159)
    #back away from lift
    robot.turn(-99)
    #turn towards scale
    robot.straight(3.75 * wheel_diameter * 3.14159)
    #go towards scale
    robot.turn(92)
    #turn towards table lever
    robot.straight(1.35 * wheel_diameter * 3.14159)
    #push table lever
    robot.turn(-30)
    #turn away from table lever
    robot.straight(0.75 * wheel_diameter * 3.14159)
    #head towards home
    robot.turn(50)
    #turn towards home
    robot.straight(3.95 * wheel_diameter * 3.14159)
    #finish heading to blue home

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R2_run()