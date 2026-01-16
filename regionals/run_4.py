from tadpoleBot import robot, motorD, rotation, square_up, Stop, drive_straight, turn, arc, multitask, run_task, run_motorD

'''
Run 4 - Silo, Market Wares, Seal Statue
Home: Blue
Attachment: Wheelbarrow & Shovel
Engineer: Evan
Authors: Evan, Tanner, Grayson 
'''
async def release_preserved_pieces():
    await run_motorD(3000, -172)
    await run_motorD(3000, 170)

async def R4_run():
    # Basic robot settings for quick launch
    robot.settings(straight_acceleration=700, straight_speed=800)

    # Square up against wall to start & Lift the arm in preparation for silo
    await multitask(square_up(), run_motorD(700,180))

    # Go toward the silo
    await drive_straight(2.45)

    # Hit the preseved pieces out of the silo 3x
    await release_preserved_pieces()
    await release_preserved_pieces()
    # Backup from the silo
    await drive_straight(-1.35)
    # turn away from the silo
    await turn(-60)
    # turn away from the silo
    # go toward the table
    await drive_straight(2.4)
    robot.settings(straight_acceleration=600, straight_speed=600)
    # go toward the table
    await turn(-80)
    # Raise the table
    await drive_straight(2.5)
    # face away from scale pan
    await turn(-45)
    # Back up to scale pan
    await drive_straight(-1.3)
    # pull out scale pan
    await drive_straight(0.75)
    # Face the seal
    await turn(140)
    robot.settings(straight_acceleration=960, straight_speed=960)
    await multitask(drive_straight(2.35), run_motorD(700,-180))
    # go towards the seal
    await drive_straight(0.35)
    # raise the seal
    await run_motorD(1000, 60)
    await turn(20)
    # back up from the seal
    await drive_straight(-1)
    # turn away from the seal
    await turn(-70)
    # head home
    await drive_straight(5.5)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R4_run())
