from tadpoleBot import robot, rotation, motorC, wait, Stop, motorD

'''
Run 2 - Salvage Operation, Flag, Angler Artifacts, Scale, Roof
Home: Red
Attachment: Swiss Army Knife
Engineer: Grayson
Code Authors: Grayson
'''

def lift_angler_artifacts():
    robot.turn(25)
    robot.turn(-25)

def R2_run():
    # Basic robot settings for quick launch
    robot.use_gyro(True)
    robot.settings(straight_acceleration=660,straight_speed=660)

    # Go towards sand
    robot.straight(2.25 * rotation)
    # Slow down for backup
    robot.settings(straight_acceleration=350,straight_speed=350)
    # Pull back sand lever
    robot.straight(-1.2 * rotation)
    # Turn away from sand lever
    robot.turn(-45)
    # Drive to line up with boat lever
    robot.straight(1.1 * rotation)
    # Turn to face boat lever
    robot.turn(38)
    # Push boat lever
    robot.straight(1 * rotation)
    # Drop off flag
    motorC.run_angle(1000, -200)
    # Wait so we can let go of flag
    wait(500)
    # Raise lever back up
    motorC.run_angle(400, 120, then=Stop.HOLD)
    
    # Adjust speed back to normal
    robot.settings(straight_acceleration=660,straight_speed=660)
    # Turn away from boat
    robot.turn(-30)
    # Go past boat 
    robot.straight(2.3 * rotation)
    # Turn towards Angler Artifacts
    robot.turn(125)

    robot.settings(straight_acceleration=360,straight_speed=360)
    # Go towards Angler Artifacts    
    robot.straight(1.7 * rotation)
    # Turn into gears
    robot.turn(-10)
    # Activate Angler Artifacts 
    motorD.run_angle(1000, 1100)

    # Back out of Angler Artifacts
    robot.straight(-2 * rotation)
    robot.turn(230)
    robot.straight(3 * rotation)
    robot.turn(95)
    robot.straight(1.5 * rotation)
    robot.straight(-0.5 * rotation)
    robot.turn(-25)
    robot.arc(900, 200)
    #robot.straight(1.5 * rotation)
    #robot.turn(30)
    #robot.straight(5 * rotation, Stop.COAST)

    '''
    # Back away from Angler Artifacts
    robot.straight(-1.25 * rotation)
    # Turn towards scale
    robot.turn(-100)
    # Go towards scale    
    robot.straight(3.7 * rotation)
    # Turn towards roof lever
    robot.turn(90)
    # Push roof lever
    robot.straight(1.1 * rotation)
    # Back up from roof lever
    robot.straight(-0.2 * rotation)
    # Turn away from roof lever
    robot.turn(-30)
    # Pull away from roof lever  
    robot.straight(0.75 * rotation)
    # Turn towards home
    robot.turn(50)
    # Finish heading to blue home  
    robot.straight(3.95 * rotation)
    '''

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R2_run()
