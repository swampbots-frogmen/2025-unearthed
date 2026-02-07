from tadpoleBot import robot, rotation, square_up, run_task, drive_straight, turn, arc, multitask, run_motorC, run_motorD

'''
Run 3 - Forge, Collect Stones, Flip Table, Grab millstone
Home: Blue
Attachment: American Eagle
Engineer: Angelique & Emaleigh (alternate)
Code Authors: Emaleigh, Angelique, Tanner
'''

async def R3_run():
    # Basic robot settings for quick launch
    robot.settings(straight_acceleration=300, straight_speed=600)

    # Square up against wall to start
    await square_up()

    # --- GET ROCKS OFF FORGE --- #
    await drive_straight(4.6)
    await turn(-40)
    await drive_straight(-0.3)
    await run_motorC(600, 350)
    await run_motorC(600, -360)
    await drive_straight(-0.25)
    await turn(-45)
    await multitask(drive_straight(-2), run_motorC(600, -250))
    await turn(90)
    await drive_straight(-3)
    #await drive_straight(-1)
    #await arc(100, 88)
    #await drive_straight(1.1)
    #await arc(-92, 90)
    #await drive_straight(0.5)
    #await turn(-36)
    #await drive_straight(0.45)
    #await turn(50)
    #await arc(400, -30)



# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R3_run())

