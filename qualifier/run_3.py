from ..common.tadpoleBot import robot, rotation, square_up

'''
Run 3 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R3_run():
    robot.use_gyro(True)
    robot.settings(straight_acceleration=400, straight_speed=500)

    square_up()
    # move toward the boulders 
    robot.straight(2.8 * rotation)
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
    robot.arc(-450, 35)
    # leave the table 
    robot.straight(-0.5 * rotation)
    #turn away from the mat
    robot.turn(-43)
    # leave the mat
    robot.straight(-2 * rotation)
    # turn to the milstone 
    robot.turn(80)
    # go toward the milstone
    robot.straight(1.2 * rotation)
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




































              


                                                                                