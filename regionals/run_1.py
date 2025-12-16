from tadpoleBot import robot, rotation, square_up, motorC, wait, multitask, run_task, run_motorC, drive_straight, turn, arc, Stop
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

    # --- MINECART MISSION --- #

    # Raise lever to avoid hitting brush and go towards brush
    await multitask(run_motorC(3000, gear_ratio * 60), drive_straight(2))
    # Arc toward mineshaft and lower arm
    await multitask(arc(320, 90), run_motorC(50, gear_ratio * -70))
    # Get a little closer to the mineshaft
    #await drive_straight(0.05)
    
    # Set some variables to help tweak adjustments easier
    total_rotation = gear_ratio * 80
    lift_rotation = 0.72 * total_rotation

    # Send minecart over the line
    await run_motorC(200, lift_rotation)
    
    # Wait for a moment to let the cart go across
    await wait(1000)

    # Lift lever all the way back up to release track
    await run_motorC(1000, total_rotation - lift_rotation - 20)

    # --- MAP REVEAL MISSION --- #

    # Speed the robot back up again
    robot.settings(straight_acceleration=550, straight_speed=600)

    # Back up towards map reveal & adjust lever to lift top soil
    await multitask(drive_straight(-1.95), run_motorC(3000, gear_ratio * 110))

    # Turn to begin map approach
    await turn(-135)

    robot.settings(straight_acceleration=250, straight_speed=250)

    # complete map mission
    await drive_straight(1.25)
    # lift topsoil
    await run_motorC(150, gear_ratio * -120)

    # --- SOIL DEPOSITS MISSION --- #

    # back away from map
    await drive_straight(-0.7)
    # turn to be parallel to the surface brushing
    await turn(45)
    # line up to surface brushing
    await drive_straight(-0.5)

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
    await robot.straight(-3.5 * rotation, then=Stop.COAST)
    




    #await arc(350, -110)

    

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    run_task(R1_run())