from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask
from tadpoleBot import run_task, run_motorC, drive_straight
from tadpoleBot import turn, arc, Stop, motorC, run_motorD

fatStick = run_motorC
redForks = run_motorD

redForkRatio = 3.1

'''
Run 6 - Mineshaft, Precious artifact
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
    # square up for preciseness
    await square_up()
    # lift and go foward to the oppsite wall
    await multitask(fatStick(900,-10), redForks(1500, 10 * redForkRatio), drive_straight(5.56))
    # slow way down
    robot.settings(straight_acceleration=100,straight_speed=100)
    # go back to turn toward the mineshaft 
    await drive_straight(-0.45)
    # turn toward the mineshafts
    await multitask(turn(90), fatStick(200, 230), redForks(300, -160 * redForkRatio))
    # go in to solve 
    await drive_straight(0.7)
    # lift minecart and artifact 
    await multitask(fatStick(200, -115), redForks(30, 19.5 * redForkRatio))
    # lower the thick stick to not break 
    await fatStick(200, 75)
    # drive away from mineshaft
    await drive_straight(-0.6)
    # turn from minshaft to go home 
    await multitask(turn(100),redForks(300, 30 * redForkRatio))

    # await redForks(300, 30 * redForkRatio)
    # await multitask(fatStick(400, -111), redForks(30, 17 * redForkRatio))
    # max speed to home 
    robot.settings(straight_acceleration=967,straight_speed=967)
    # turn away from minshaft

    # await drive_straight(-0.5)
    # await turn(100)
    # # drive home 
    await multitask(fatStick(800, -100) , drive_straight(5.5))

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R6_run())



