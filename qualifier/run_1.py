from tadpoleBot import robot, rotation, square_up, motorC, wait

'''
Run 1 - Mineshaft, Map Reveal, Soild Deposits, Brush
Home: Red
Attachment: The Mammoth
Engineer: Camden and Tanner (alternate)
Code Authors: Camden, Tanner, Grayson
'''
def R1_run():
    # Basic robot settings
    robot.settings(straight_acceleration=400,straight_speed=600)
    robot.use_gyro(True)

    # Square up against wall to start
    square_up()

    # Raise lever to avoid hitting brush
    motorC.run_angle(3000, -60)
    # Go towards brush
    robot.straight(3 * rotation)
    # Slight turn towards mineshaft
    robot.turn(15)
    # Slight movement to get away from brush
    robot.straight(0.9 * rotation)
    # Finish turn towards mineshaft
    robot.turn(75)

    # Lower the speed for more precise movement
    robot.settings(straight_acceleration=450, straight_speed=450)

    # Lower lever
    motorC.run_angle(3000, 50)
    # Go towards mineshaft
    robot.straight(2 * rotation)

    # Lower the speed even more for precise alignment
    robot.settings(straight_acceleration=150, straight_speed=150)
    
    # Set some variables to help tweak adjustments easier
    total_rotation = -80
    lift_rotation = 0.67 * total_rotation

    # Send minecart over the line
    motorC.run_angle(3000, lift_rotation)

    # Wait for a moment to let the cart go across
    wait(1000)

    # Lift lever all the way back up to release track
    motorC.run_angle(3000, total_rotation - lift_rotation)

    # Speed the robot back up again
    robot.settings(straight_acceleration=550, straight_speed=600)

    # Back up towards map reveal
    robot.straight(-1.55 * rotation)
    # Adjust lever to lift top soil
    motorC.run_angle(3000, -110)
   
    # Turn to begin map approach
    robot.turn(-90)
    # Back up to adjust entry angle
    robot.straight(-0.85 * rotation)
    # Turn towards map mission
    robot.turn(-45)

    # Now we're going to slow down for precise movement
    robot.settings(straight_acceleration=150, straight_speed=150)

    # Move towards map reveal
    robot.straight(2.1 * rotation)
    # Lift Top soil
    motorC.run_angle(150,120)
    # Back up from map reveal
    robot.straight(-0.9 * rotation)
    # Turn towards brush
    robot.turn(45)
    # Back up from map reveal
    robot.straight(-0.2 * rotation)

    # Lower lever to grab brush
    motorC.run_angle(3000,80)

    # Speed back up for brush run
    robot.settings(straight_acceleration=450,straight_speed=550)
    
    # Knock down soil deposits
    robot.straight(0.4 * rotation)
    robot.straight(-0.8 * rotation)
    
    # Lift brush up
    motorC.run_angle(150,-60)

    # Head home
    robot.straight(-3.5 * rotation)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R1_run()
