from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask, run_task, run_motorC, drive_straight, turn, arc, Stop, run_motorD
from indy import play_raiders_march

# Basic robot settings
robot.settings(straight_acceleration=400,straight_speed=600)
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

    await run_motorD(3000, gear_ratio * -70)
    
    await drive_straight(3.15)

    # wait(500)

    await run_motorD(3000, gear_ratio * 70)

    await run_motorD(400, gear_ratio * -110)

    await drive_straight(0.75)

    await turn(-45)

    await drive_straight(1)

    await run_motorD(200, gear_ratio * 75)

    # await run_motorD(500, gear_ratio * -150)

    await drive_straight(-1)

    await turn(45)

    await drive_straight(-3.4)



    # await drive_straight(-3.15)
    

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R1_run())