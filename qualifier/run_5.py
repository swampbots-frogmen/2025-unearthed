from tadpoleBot import robot, rotation, square_up

robot.use_gyro(True)
robot.settings(straight_acceleration=300, straight_speed=300)

square_up()
robot.arc(500, 80)
robot.arc(500, -80)
