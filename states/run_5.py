from tadpoleBot import robot, square_up, rotation, drive_straight, turn, run_task, arc

'''
Run 5 - Deliver artifacts to the forum
Home: Red
Attachment: Bulldozer
Engineer: Chaz
Authors: Chaz and Tanner
'''
async def R5_run():
    # Basic robot settings for quick launch
    robot.settings(straight_acceleration=300, straight_speed=300)

    # Square up against wall to start
    await square_up()

    # --- FORUM DELIVERY MISSION --- #
    await drive_straight(1)
    await turn(45)
    await drive_straight(2)

    # Drive back home quickly!
    robot.settings(straight_acceleration=700, straight_speed=700)
    await arc(700, -40)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R5_run())
