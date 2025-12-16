from tadpoleBot import robot, motorD, rotation, square_up, Stop

'''
Run 4 - Silo, Market Wares, Seal Statue
Home: Blue
Attachment: Wheelbarrow & Shovel
Engineer: Evan
Authors: Evan, Tanner
'''

def release_preserved_pieces():
    motorD.run_angle(400, -162, then=Stop.HOLD)
    motorD.run_angle(400, 160, then=Stop.HOLD)

def R4_run():
    # Basic robot settings for quick launch
    robot.use_gyro(True)
    robot.settings(straight_acceleration=350, straight_speed=500)

    # Square up against wall to start
    square_up()

    # Lift the arm in preparation for silo
    motorD.run_angle(700
    ,180)
    # Go toward the silo
    robot.straight(2.45 * rotation)

    # Hit the preseved pieces out of the silo 3x
    release_preserved_pieces()
    release_preserved_pieces()
    release_preserved_pieces()

    # Slow down the robot for more precise movement
    robot.settings(straight_acceleration=400, straight_speed=500)
    # Backup from the silo
    robot.straight(-1.35 * rotation) 
    # Turn away from silo and flip market wares table
    robot.arc(-245, 190)
    #turn to get scale pan
    robot.turn(140)
    #go towards the scale pan
    robot.straight(1.35 * rotation) 
    #grab the scale pan
    robot.settings(straight_acceleration=50, straight_speed=100)
    robot.turn(-100)
    robot.settings(straight_acceleration=400, straight_speed=500)
    #turn away from the scale pan
    robot.arc(90, 90)
    #go toward the seal and lift it
    #robot.arc(20,25)
    motorD.run_angle(400, -162)
    robot.straight(2 * rotation)
    motorD.run_angle(400, 100)
    robot.straight(-0.7 * rotation)
    robot.turn(-90)
    robot.straight(2 * rotation)

    
    
    

    #robot.arc(200, 120)
    #robot.straight(0.5 * rotation)
    #get the scale pan
    #robot.turn(-50)
    #robot.straight(-0.5 * rotation)
    #robot.turn(-90)
    #turn towards the seal
    #robot.arc(100, 140)
    #move towards the seal
    #motorD.run_angle(2000, -190)
    #robot.straight(2 * rotation)
    #lift the seal
    #motor.run_angle(2000, 70)
    #robot.turn(20)


    # Pull away from the silo
    #robot.straight(1.7 * rotation)

    # Turn to face the market wares table
    #robot.turn(-45)
    
    # Go little slower past the market wares table
    #robot.settings(straight_acceleration=200, straight_speed=200)
    
    # Drive past table to lift wares
    #robot.straight(2.75 * rotation)

    # Change the speed back to normal
    #robot.settings(straight_acceleration=400, straight_speed=500)

    # Turn to solve the seal
    #robot.turn(87)
    # Drive toward the seal
    #robot.straight(2.4 * rotation)
    # Smack the lever on the statue to lift it
    #motorD.run_angle(2000, -190)

    # Back up a little to leave the seal
    #robot.straight(-0.5 * rotation)
    # Turn to go home
    #robot.turn(-80)
    # Lift lever up a little
    #motorD.run_angle(2000, 50)
    # Go home full speed
    #robot.settings(straight_acceleration=700, straight_speed=700)
    #robot.straight(5 * rotation)

# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R4_run()
