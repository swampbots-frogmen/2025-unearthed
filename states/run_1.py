from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask, run_task, run_motorC, drive_straight, turn, arc, Stop, run_motorD
from indy import play_raiders_march

# Basic robot settings
robot.settings(straight_acceleration=600,straight_speed=800)
robot.use_gyro(True)
gear_ratio = -1.5

'''
Run 1 - Mineshaft, Map Reveal, Soild Deposits, Brush
Home: Red
Attachment: The Mammoth
Engineer: Camden and Tanner (alternate)
Code Authors: Camden, Tanner, Grayson
'''
async def R1_run():
    
    # Square up against wall to start
    await square_up()

    #await run_motorD(3000, gear_ratio * -70)
    
    #await drive_straight(3.15)

    await multitask(run_motorD(200, gear_ratio * -80), drive_straight(3.15))

    await run_motorD(800, gear_ratio * 70)

    await run_motorD(400, gear_ratio * -110)

    await drive_straight(0.75)

    await turn(-45)

    await drive_straight(1)

    await run_motorD(200, gear_ratio * 75)

    await drive_straight(-1)

    await turn(45)

    robot.settings(straight_acceleration=960,straight_speed=960)

    await drive_straight(-3.7)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R1_run())