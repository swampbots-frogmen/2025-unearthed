from tadpoleBot import robot, motorD, rotation, square_up, Stop

'''
Run 4 - Silo, Market Wares, Seal Statue
Home: Blue
Attachment: Wheelbarrow & Shovel
Engineer: Evan
Authors: Evan, Tanner, Grayson 
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
    motorD.run_angle(700,180)
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
    # turn away from the silo
    robot.turn(-60)
    # turn away from the silo
    # go toward the table
    robot.straight(2.3 * rotation)
    # go toward the table
    robot.turn(-80)
    # turn toward the table 
    robot.straight(1.3 * rotation)
    # turn away from the table
    robot.turn(80)
    # go towards the scale pan
    robot.straight(0.9 * rotation)
    # Pull scale pan out
    robot.turn(-90)
    # arc towards the seal
    robot.arc(90, 100)
    # go towards the seal
    robot.straight(1.35 * rotation)
    # lower level for the seal
    motorD.run_angle(700, -180)
    # go towards the seal
    robot.straight(0.6 * rotation)
    # raise the seal
    motorD.run_angle(700, 90)
    robot.turn(35)
    # back up from the seal
    robot.straight(-1 * rotation)
    # turn away from the seal
    robot.turn(-90)
    # head home
    robot.straight(8 * rotation)
    '''
    #turn to get scale pan
    #robot.turn(147)
    #go towards the scale pan
    robot.straight(1.45 * rotation) 
    #grab the scale pan
    robot.settings(straight_acceleration=50, straight_speed=100)
    robot.turn(-100)
    robot.settings(straight_acceleration=400, straight_speed=500)
    robot.straight(0.3 * rotation)
    #turn away from the scale pan
    robot.arc(90, 90)
    #go toward the seal and lift it
    robot.arc(30,15)
    motorD.run_angle(350, -162)
    robot.straight(2 * rotation)
    motorD.run_angle(400, 100)
    robot.straight(-0.7 * rotation)
    robot.turn(-60)
    robot.straight(4 * rotation)

    
    
    

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
    '''
# If we're running ONLY this run (without the menu)
if __name__ == '__main__':
    R4_run()
