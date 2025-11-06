from tadpoleBot import robot, rotation, square_up

'''
Run 3 - Describe what it does
Home: Blue
Attachment: Name of the attachment
Engineer: Emaleigh and Anglique
Authors: Emaleigh and Anglique
'''
def R3_run():
    robot.use_gyro(True)
    robot.settings(straight_acceleration=400, straight_speed=500)

    square_up()
    # move toward the boulders 
    robot.straight(2.76 * rotation)
    #Push the wing in
    robot.arc(200, 55)
    robot.arc(300, -49)
    # Push the rocks off
    robot.straight(2 * rotation)
    robot.straight(-0.7 * rotation)
    # Turn to Push the wing off
    robot.turn(70)
    # Push rocks and wing off table
    robot.straight(1.7 * rotation)
    #get ready to solve the table
    robot.straight(-1.8 * rotation)
    robot.turn(-80)
    # solve the table 
    robot.arc(-500, 35)
    # leave the table 
    robot.straight(-0.5 * rotation)
    #turn away from the mat
    robot.turn(-50)
    # leave the mat
    robot.straight(-2.7 * rotation)
    # turn to the milstone 
    robot.turn(85)
    # go toward the milstone
    robot.straight(1 * rotation)
    # turn to slove the milestone
    #robot.turn(-63)
    # foward to the milestone
    #robot.straight(2 * rotation)
    #turn and slove the milstone 
    robot.turn(-63)
    robot.arc(-200, -55)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R3_run()                                                           














                                                                                                                                                                                                                         