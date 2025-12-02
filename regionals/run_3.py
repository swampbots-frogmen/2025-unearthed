from tadpoleBot import robot, rotation, square_up

'''
Run 3 - Forge, Collect Stones, Flip Table, Grab millstone
Home: Blue
Attachment: American Eagle
Engineer: Anglique & Emaleigh (alternate)
Code Authors: Emaleigh, Anglique, Tanner
'''

def R3_run():
    # Basic robot settings for quick launch
    robot.use_gyro(True)
    robot.settings(straight_acceleration=400, straight_speed=500)

    # Square up against wall to start
    square_up()

    # Move toward the Forge (but not all the way)
    robot.straight(2.76 * rotation)
    # Push the wing in to catch boulders
    robot.arc(180, 55)
    robot.arc(309, -45)
    # Push the rocks off and back away from the forge
    robot.straight(1.61 * rotation)
    robot.straight(-0.5 * rotation)

    # Turn to Push the wing off
    robot.turn(60)
    # Push rocks and wing off table and return to table
    robot.straight(1.7 * rotation)
    robot.straight(-1.8 * rotation)

    # Turn to solve the table
    robot.turn(-71)
    # Solve the table 
    robot.arc(-300, 34)
    # Leave the table 
    robot.straight(-0.5 * rotation)

    # Turn away from the mat
    robot.turn(-50)
    # Leave the mat by going backwards
    robot.straight(-2.4 * rotation)
    # Turn to the millstone 
    robot.turn(80)
    # Go toward the millstone
    robot.straight(1.2 * rotation)
    # Turn and solve the millstone 
    robot.turn(-54)
    # Grab the millstone off the mat
    robot.arc(-200, -62)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R3_run()                                                           














                                                                                            
