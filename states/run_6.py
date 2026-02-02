from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask
from tadpoleBot import run_task, run_motorC, drive_straight
from tadpoleBot import turn, arc, Stop, motorC, run_motorD

'''
Run 6 - Mineshaft, Perscouis artifact
Home: red
Attachment: Grill master
Engineer: TBD
Authors:Tanner
'''

async def R6_run():
    # setup max speed 
    robot.settings(straight_acceleration=500,straight_speed=500)
    # make sure gyro is used 
    robot.use_gyro(True)
    # square up for prcisenes
    await square_up()
    # lift and go foward to the oppsite wall
    await multitask(run_motorC(900,-10), run_motorD(900,10), drive_straight(5.56))
    # slow way down
    robot.settings(straight_acceleration=100,straight_speed=100)
    # go back to turn toward the mineshaft 
    await drive_straight(-0.45)
    # turn toward the mineshafts
    await turn(90)
    # lift the sticks to slove the precous artfact
    await multitask(run_motorC(300, 200), run_motorD(300,-150))
    # go in to solve 
    await drive_straight(0.7)
    # lift minecart and artifact 
    await multitask(run_motorC(800, -160), run_motorD(300,25))
    # lower the thick stick to not break 
    await run_motorC(800, 75)
    # drive away from mineshaft
    await drive_straight(-0.9)
    # max speed to home 
    robot.settings(straight_acceleration=960,straight_speed=960)
    # turn away from minshaft
    await turn(100)
    # drive home 
    await multitask(run_motorC(800, -100), run_motorD(300,60), drive_straight(5.5))

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R6_run())