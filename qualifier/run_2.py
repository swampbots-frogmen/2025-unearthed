from tadpoleBot import robot, rotation, square_up, wheel_diameter

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

    # go towards sand
    robot.straight(2.25 * wheel_diameter * 3.14159)
    # pull back lever
    robot.straight(-1.2 * wheel_diameter * 3.14159)
    # turn to boat lever
    robot.turn(-45)

    robot.straight(1 * wheel_diameter * 3.14159)

    robot.turn(35)
    #push boat lever
    robot.straight(0.9 * wheel_diameter * 3.14159)
#turn away from boat
    robot.turn(-30)
#go past boat 
    robot.straight(1.5 * wheel_diameter * 3.14159)
#turn towards lift
    robot.turn(90)
#go towards lift    
    robot.straight(1.2 * wheel_diameter * 3.14159)
#activate lift lever
    robot.turn(25)

    robot.turn(-25)

    robot.turn(25)

    robot.turn(-25)

    robot.turn(25)
 #finish activating lever
    robot.turn(-25)

#back away from lift
    robot.straight(-1.5 * wheel_diameter * 3.14159)
    #turn towards scale
    robot.turn(-95)
    #go towards scale    
    robot.straight(3.8 * wheel_diameter * 3.14159)
#turn towards table lever
    robot.turn(90)
 #push table lever
    robot.straight(1.2 * wheel_diameter * 3.14159)
# back up from table lever
    robot.straight(-0.2 * wheel_diameter * 3.14159)
#turn away from table lever
    robot.turn(-30)
   #head towards home   
    robot.straight(0.75 * wheel_diameter * 3.14159)
 #turn towards home
    robot.turn(50)
 #finish heading to blue home  
    robot.straight(3.95 * wheel_diameter * 3.14159)
 

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R2_run()