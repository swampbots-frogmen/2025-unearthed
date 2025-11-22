from tadpoleBot import robot, square_up, Stop

'''
Run 5 - Deliver artifacts to the forum
Home: Red
Attachment: Bulldozer
Engineer: Chaz
Authors: Chaz and Tanner
'''
def R5_run():
    # Basic robot settings for quick launch
    robot.use_gyro(True)
    robot.settings(straight_acceleration=300, straight_speed=300)

    # Square up against wall to start
    square_up()

    # Move toward the forum
    robot.arc(500, 80)
    # Pull away from the forum
    robot.arc(500, -80, then=Stop.COAST)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R5_run()
