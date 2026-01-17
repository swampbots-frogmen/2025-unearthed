from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Button, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task, StopWatch

# Some useful variables
pi = 3.141592654

# Initialize the hub, motors, and drive base
hub = PrimeHub()

# This makes the menu program totally stop when the bluetooth button is pressed
hub.system.set_stop_button(Button.BLUETOOTH)

Tanner = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Grayson = Motor(Port.B, Direction.CLOCKWISE)
motorC = Motor(Port.C)
motorD = Motor(Port.D)
colorSensorLeft = ColorSensor(Port.E)
# colorSensorRight = ColorSensor(Port.F)
Tanner.dc(60)
Grayson.dc(60)
wheel_diameter = 56  # Adjust based on our robot's wheel diameter in mm
axle_track = 120  # Adjust based on our robot's axle track in mm
rotation = wheel_diameter * pi

robot = DriveBase(Tanner, Grayson, wheel_diameter, axle_track)
robot.settings(turn_acceleration=200, turn_rate=400)
robot.use_gyro(True)

async def square_up():
    robot.drive(-300, 0)
    await wait(500)
    robot.stop()

async def run_motorC(speed, angle):
    await motorC.run_angle(speed, angle)

async def run_motorD(speed, angle):
    await motorD.run_angle(speed, angle)

async def drive_straight(rotations, behavior=Stop.HOLD):
    await robot.straight(rotations * rotation, then=behavior)

async def turn(degrees):
    await robot.turn(degrees)

async def arc(radius, distance):
    await robot.arc(radius, distance)

#------Miscellaneous Variables--------
def advanced_arc(speed, radius, angle):
    """
    speed, radius, angle
    Drive a precise arc with forward/backward support, PD correction,
    and exponential speed ramp for smooth motion.
    
    Positive angle = right turn, negative = left turn.
    Positive radius = forward, negative radius = backward.
    """
    #-------Robot Variables-----------
    TRACK_WIDTH = axle_track  # mm, width of the robot, used in several calculations
    WHEEL_CIRC = rotation   # mm, circumfrence of wheel used in several calculations
    LEFT_MOTOR_FLIPPED = False

    #------PD Correction Variables-----------
    KP = 1.5
    KD = 0.5
    last_error = 0

    #---------Safety Check To Make Sure Your Doing An Arc And Not Just Going Straight-----------
    if abs(radius) < 1: # abs is absolute value for future use of the operation
        raise ValueError("Radius too small")

    #------More Miscellaneous Variables--------
    direction = 1 if radius > 0 else -1 # used to understand if its going forward or backwards
    radius = abs(radius)  # use magnitude for calculations

    #-------Reset sensors----------
    hub.imu.reset_heading(0) # resets gyro
    wait(100)
    Tanner.reset_angle(0) # resets degrees counted in the left motor
    Grayson.reset_angle(0) # resets degrees counted in the right motor
    wait(50)

    #-----------Arc Geometry Used To Calculate The Degrees Each Motor Must Go------------
    theta = abs(angle) * pi / 180 #important calculation used to convert angles in degrees to radians
    # takes the angle and * it by pi over 180 which is the formula to convert to radians
    # the radians in this case are used to measure angles using the circle itself.
    # One radian is the angle where the arc length equals the radius of the circle
    outer_radius = radius + TRACK_WIDTH / 2 
    # calculates the outer radius with the imputed radius from above and adding
    # the width of the robot divided by 2 because the outer radius is half the trackwidth added to the radius like so
    # outer radius, radius, inner radius
    # radius is measured from the center of the robot
    # the outer and inner radi make up an outline of the robots Trackwidth
    inner_radius = max(radius - TRACK_WIDTH / 2, 0) 
    # calculates the inner radius with the imputed radius from above and subtrabting the width of the robot divided by 2
    # same logic from the comment above
    outer_deg = (outer_radius * theta / WHEEL_CIRC) * 360 #outer degrees needed to travel in degrees form
    # calculates by the outer radius being multiplied by the angle converted into radians, the arc length formula, then dividing by wheel circumfrence
    # and finally * by 360 to convert to degrees
    inner_deg = (inner_radius * theta / WHEEL_CIRC) * 360 # inner degrees in degrees form
    # calculates by the inner radius being multiplied by the angle converted into radians, the arc length formula, then dividing by wheel circumfrence
    # and finally * by 360 to convert to degrees
    #--------Base speeds--------
    outer_speed_base = max(speed, 100) # outer wheel goes the fastest, overides speed if its less than 100
    inner_speed_base = outer_speed_base * (inner_deg / outer_deg) if outer_deg != 0 else outer_speed_base # inner wheel goes only a fraction of the outer 
    #wheels speed

    #-------Determine Outer/Inner Motors Based On Turn Direction------------
    if angle >= 0:  # right turn
        outer_motor = Tanner # the left motor is the outer and faster motor for a right turn
        inner_motor = Grayson # the right motor travals less or is stationary for a right arc
        pd_sign = 1 # compensates for turn direction wether forward or backward
    else:           # left turn
        outer_motor = Grayson # the right motor is the outer and faster motor for a left turn
        inner_motor = Tanner # the left motor travals less or is stationary for a left arc
        pd_sign = -1 # compensates for turn direction wether forward or backward

    #----- Motor flip --------
    left_factor = -1 if LEFT_MOTOR_FLIPPED else 1 # used to get the left motor to go the right direction during an arc

    # --- Before the loop, define base speeds ---
    outer_speed_base = max(speed, 100)
    inner_speed_base = outer_speed_base * (inner_deg / outer_deg) if outer_deg != 0 else outer_speed_base

    # --- True Hybrid / Gyro Drive Loop ---
    timer = StopWatch() # gets stopwatch
    last_time = timer.time() # gets last time
    last_error = 0 # sets up last error

    def signed_error(target, current): # defines a function to help tell right from left on correction
        error = target - current # gets error when functon is ran
        if error > 180: # tells the angle the error is - degrees instead of positive over 180
            error -= 360
        elif error < -180: # opposite of the above
            error += 360
        return error # returns error in its proper state

    # ---------------- Motor Assignment ----------------
    if direction == 1:  # forward
        if angle >= 0:  # right turn
            outer_motor = Tanner # sets outer wheel to left motor to turn right while moving forwards
            inner_motor = Grayson # sets inner wheel to right motor to turn right while moving forwards
            pd_sign = 1 # variable used later on to tell which direction to go based of positive or negative
        else:           # left turn
            outer_motor = Grayson # sets outer wheel to right motor to turn left while moving forwards
            inner_motor = Tanner # sets inner wheel to left motor to turn right while moving forwards
            pd_sign = -1 # variable used later on to tell which direction to go based of positive or negative
    else:  # backward
        if angle >= 0:  # right turn backward
            outer_motor = Grayson # inverts the motors of  the front right turn to go backwards right turn
            inner_motor = Tanner # inverts the motors of  the front right turn to go backwards right turn
            pd_sign = 1  # correction still inward
        else:           # left turn backward
            outer_motor = Tanner # inverts the motors of  the front left turn to go backwards left turn
            inner_motor = Grayson # inverts the motors of  the front left turn to go backwards left turn
            pd_sign = -1  # correction still inward

    # ---------------- Drive Loop ----------------
    while True: # starts the drive loop
        current_heading = hub.imu.heading() # makes a variable for the current gryro position
        left_angle = Tanner.angle() # gets the current degrees counted by left motor
        right_angle = Grayson.angle() # gets the current degrees counted by right motor

        # ---------------- Progress Calculation ----------------
        if direction == 1: # detects if moving forward
            # Forward: hybrid motor + gyro
            motor_progress = max(abs(left_angle)/outer_deg, abs(right_angle)/outer_deg) # calculates motor progress based off degrees counted
            motor_progress = min(motor_progress, 1.0) # calculates motor progress based off degrees counted
            gyro_progress = min(abs(current_heading)/abs(angle), 1.0) # calculates progress based off gyro
            progress = 0.7 * motor_progress + 0.3 * gyro_progress # uses a hybrid between the 2 progresses to make precise calculations
        else:
            # Backward: gyro only
            progress = min(abs(current_heading)/abs(angle), 1.0) # if moving backwards calculates only based on gyro because motor degrees causes issues
            # when moving backwards

        # ---------------- Target Heading & Error ----------------
        target_heading = angle * progress # target heading is based off progress, which is different for forwards and backwards
        error = signed_error(target_heading, current_heading) # gets error from signed error function

        # ---------------- PD Derivative ----------------
        now = timer.time() # sets the current time
        dt = max((now - last_time)/1000, 0.005) # helps calculate derivative
        derivative = (error - last_error)/dt # calculates derivative correction
        last_error = error # sets the last error
        last_time = now # gets the previous time

        # ---------------- PD Correction ----------------
        correction = (KP * error + KD * derivative) * pd_sign # gets the correction
        max_correction = 0.3 * speed # clamps the speed of correction
        correction = max(-max_correction, min(max_correction, correction)) # clamps the speed of correction

        # ---------------- Speed Ramp ----------------
        ramp = 0.3 + 0.7 * (4 * progress * (1 - progress))**0.5 # speed ramp is mad to accelerate and deccelerate
        outer_speed_ramped = outer_speed_base * ramp # applies ramp
        inner_speed_ramped = inner_speed_base * ramp # applies ramp

        # Scale speeds slightly based on correction
        speed_scale = max(0.2, 1.0 - abs(correction) / (0.3 * speed))
        outer_speed_ramped *= speed_scale
        inner_speed_ramped *= speed_scale

        # ---------------- Apply Motor Speeds ----------------
        outer_motor.run((outer_speed_ramped + correction) * (left_factor if outer_motor == Tanner else 1) * direction) # applies the motor speeds
        inner_motor.run((inner_speed_ramped - correction) * (left_factor if inner_motor == Tanner else 1) * direction) # applies the motor speeds

        # ---------------- Stop Condition ----------------
        if progress >= 1.0: # ounce progress is complete it stops
            outer_motor.run(0) # stops motor
            inner_motor.run(0) # stops other motor
            wait(20) # wait in ms added to prevent harming the cpu
            break # breaks the loop

        wait(5) # wait in ms added to prevent harming the cpu
