from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask, run_task, run_motorC, drive_straight, turn, arc, Stop, motorC, run_motorD

async def R6_run():
    robot.settings(straight_acceleration=400,straight_speed=900)
    robot.use_gyro(True)
    await square_up()
    await multitask(run_motorC(900,-10), run_motorD(900,10), drive_straight(5.56))
    robot.settings(straight_acceleration=100,straight_speed=100)
    await drive_straight(-0.45)
    await turn(90)
    await drive_straight(-0.4)
    await multitask(run_motorC(300, 200), run_motorD(300,-130))
    await drive_straight(1.5)
    await multitask(run_motorC(800, -100), run_motorD(300,10))
    await drive_straight(-0.9)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R6_run())