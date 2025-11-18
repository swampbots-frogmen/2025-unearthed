from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask, run_task, run_motorC, drive_straight, turn

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

    # Raise lever to avoid hitting brush and go towards brush
    await multitask(run_motorC(3000, gear_ratio * 60), drive_straight(3))
    # Slight turn towards mineshaft
    await turn(15)
    # Slight movement to get away from brush
    await drive_straight(0.9)
    # Finish turn towards mineshaft and lower lever
    await multitask(turn(75), run_motorC(3000, gear_ratio * -50))

    # Lower the speed for more precise movement
    robot.settings(straight_acceleration=450, straight_speed=450)

    # Go towards mineshaft
    await drive_straight(2)

    # Lower the speed even more for precise alignment
    robot.settings(straight_acceleration=150, straight_speed=150)
    
    # Set some variables to help tweak adjustments easier
    total_rotation = gear_ratio * 80
    lift_rotation = 0.67 * total_rotation

    # Send minecart over the line
    await run_motorC(3000, lift_rotation)

    # Wait for a moment to let the cart go across
    await wait(1000)

    # Lift lever all the way back up to release track
    await run_motorC(3000, total_rotation - lift_rotation)

    # Speed the robot back up again
    robot.settings(straight_acceleration=550, straight_speed=600)

    # Back up towards map reveal & adjust lever to lift top soil
    await multitask(drive_straight(-1.55), run_motorC(3000, gear_ratio * 110))
   
    # Turn to begin map approach
    await turn(-90)
    # Back up to adjust entry angle
    await drive_straight(-0.85)
    # Turn towards map mission
    await robot.turn(-45)

    # Now we're going to slow down for precise movement
    robot.settings(straight_acceleration=150, straight_speed=150)

    # Move towards map reveal
    await drive_straight(2.1)
    # Lift Top soil
    await run_motorC(150, gear_ratio * -120)
    # Back up from map reveal
    await drive_straight(-0.9)
    # Turn towards brush
    await turn(45)
    # Back up from map reveal
    await drive_straight(-0.2)

    # Lower lever to grab brush
    await run_motorC(3000, gear_ratio * -80)

    # Speed back up for brush run
    robot.settings(straight_acceleration=450, straight_speed=550)
    
    # Knock down soil deposits
    await drive_straight(0.4)
    await drive_straight(-0.8)
    
    # Lift brush up
    await run_motorC(150, gear_ratio * 60)

    # Head home
    await drive_straight(-3.5)


# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R1_run())
