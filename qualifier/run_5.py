from ..common.tadpoleBot import robot, square_up

'''
Run 5 - Describe what it does
Home: Blue or Red
Attachment: Name of the attachment
Engineer: Who runs this mission?
Authors: Who coded this run (name all)
'''
def R5_run():
    robot.use_gyro(True)
    robot.settings(straight_acceleration=300, straight_speed=300)

    square_up()
    robot.arc(500, 80)
    robot.arc(500, -80)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R5_run()

