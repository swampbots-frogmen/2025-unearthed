from tadpoleBot import robot, rotation, run_motorC, wait, Stop, run_motorD, drive_straight, arc, run_task, turn, multitask

'''
Run 2 - Salvage Operation, Flag, Angler Artifacts, Scale, Roof
Home: Red
Attachment: Swiss Army Knife
Engineer: Grayson
Code Authors: Grayson
'''

async def R2_run():
    # Basic robot settings for quick launch
    robot.settings(straight_acceleration=350,straight_speed=660)

    # Go towards sand
    await drive_straight(2.6)
    
    # Slow down for backup
    robot.settings(straight_acceleration=350,straight_speed=350)
    # Pull back sand lever
    await drive_straight(-2.3)
    await arc(-150, 70)

    await arc(65, 65)

    await drive_straight(1.45)

    # Drop off flag
    await run_motorC(1000, -200)
    # Wait so we can let go of flag
    await wait(500)
    # Raise lever back up
    await run_motorC(400, 200)
    
    # Adjust speed back to normal
    robot.settings(straight_acceleration=660,straight_speed=660)
    # Turn away from boat
    await turn(-30)
    # Go past boat 
    await drive_straight(2.3)
    # Turn towards Angler Artifacts
    await turn(125)

    robot.settings(straight_acceleration=360,straight_speed=360)
    # Go towards Angler Artifacts    
    await drive_straight(1.7)
    # Turn into gears
    await turn(-25)
    # Activate Angler Artifacts 
    await run_motorD(1000, 1100)
    await turn(25)

    # Back out of Angler Artifacts
    await drive_straight(-1.8)
    # Turn towards the scale pan
    await multitask(turn(200), run_motorC(200, -180))
    # Drive towards opponent's minecart
    await drive_straight(2)
    await multitask(drive_straight(0.8), run_motorC(200, 180))
    # Turn towards roof
    await turn(110)
    await drive_straight(2)
    await turn(20)
    await drive_straight(-0.5)
    await turn(-25)
    robot.settings(straight_acceleration=660,straight_speed=660)
    await arc(800, 75)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R2_run())
