from tadpoleBot import robot, rotation, square_up, run_task, drive_straight, turn, arc

'''
Run 3 - Forge, Collect Stones, Flip Table, Grab millstone
Home: Blue
Attachment: American Eagle
Engineer: Anglique & Emaleigh (alternate)
Code Authors: Emaleigh, Anglique, Tanner
'''

async def R3_run():
    # Basic robot settings for quick launch
    robot.settings(straight_acceleration=400, straight_speed=500)

    # Square up against wall to start
    await square_up()

    # --- GET ROCKS OFF FORGE --- #

    # Move toward the Forge (but not all the way)
    await drive_straight(2.76)
    # Push the wing in to catch boulders
    await arc(180, 55)
    await arc(200, -49)
    # Push the rocks off and back away from the forge
    await drive_straight(1.3)
    await drive_straight(-0.5)

    # --- GET ROCKS OFF BOARD --- #

    # Turn to Push the wing off
    await turn(60)
    # Push rocks and wing off table and return to table
    await drive_straight(1.7)
    await drive_straight(-1.8)

    # --- FLIP THE TABLE MISSION --- #

    # Turn to solve the table
    await turn(-70)
    # Solve the table 
    await arc(-300, 34)
    # Leave the table 
    await drive_straight(-0.5)

    # --- GRAB THE MILLSTONE MISSION --- #

    # Turn away from the mat
    await turn(-50)
    # Leave the mat by going backwards
    await drive_straight(-2.5)
    # Turn to the millstone 
    await turn(80)
    # Go toward the millstone
    await drive_straight(1)
    # Turn and solve the millstone 
    await turn(-50)
    # Grab the millstone off the mat
    await arc(-235, -55)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R3_run())














                                                                                            
