from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button, Icon
from pybricks.tools import wait
from tadpoleBot import robot, Tanner, Grayson, run_task, multitask
from indy import march_twice

# Import your existing run files
from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

hub = PrimeHub()
color_sensor_r = ColorSensor(Port.E)
color_sensor_l = ColorSensor(Port.F)

# Disable system stop button (optional)
hub.system.set_stop_button(Button.BLUETOOTH)

# ----------------------
# Program functions
# ----------------------
def run_program_red():
    run_task(multitask(R1_run(), march_twice()))

def run_program_yellow():
    run_task(R2_run())

def run_program_blue():
    run_task(R3_run())

def run_program_green():
    run_task(R4_run())

def run_program_white():
    run_task(R5_run())

def run_program_blue_yellow():
    run_task(R6_run())

def get_program_info(left_sensor, right_sensor):
    if (left_sensor == Color.YELLOW and right_sensor == Color.YELLOW):
        return { "color": Color.YELLOW, "program": run_program_yellow, "number": "3" }
    elif (left_sensor == Color.RED and right_sensor == Color.RED):
        return { "color": Color.RED, "program": run_program_red, "number": "1" }
    elif (left_sensor == Color.BLUE and right_sensor == Color.YELLOW):
        return { "color": Color.ORANGE, "program": run_program_blue_yellow, "number": "2" }
    elif (left_sensor == Color.GREEN and right_sensor == Color.GREEN):
        return { "color": Color.GREEN, "program": run_program_blue_yellow, "number": "5" }
    elif (left_sensor == Color.WHITE and right_sensor == Color.WHITE):
        return { "color": Color.WHITE, "program": run_program_white, "number": "6" }
    elif (left_sensor == Color.BLUE and right_sensor == Color.BLUE):
        return { "color": Color.BLUE, "program": run_program_blue, "number": "4" }

    return None
# ----------------------
# Main Menu
# ----------------------
def main_menu():
    selected_program = None
    hub.light.on(Color.CYAN)

    pressed = ()

    while True:
        if (not pressed):
            pressed = hub.buttons.pressed()

            # Detect color
            detected_color_r = color_sensor_r.color()
            detected_color_l = color_sensor_l.color()
            print(f"Color: {detected_color_l} and {detected_color_r}")

            program_info = get_program_info(detected_color_l, detected_color_r)
        
            if (program_info != None):  
                hub.light.on(program_info["color"])
                hub.display.char(program_info["number"])
                selected_program = program_info["program"]
            else:
                hub.light.on(Color.CYAN)
                hub.display.icon(Icon.PAUSE)

        else:
            if Button.CENTER in pressed and selected_program is not None:
                # hub.system.set_stop_button(Button.CENTER)
                hub.display.icon(Icon.HAPPY)
                selected_program()
                selected_program = None
                pressed = ()
                hub.system.set_stop_button(Button.BLUETOOTH)

            elif Button.BLUETOOTH in pressed:
                break

            else:
                continue

            hub.system.set_stop_button(Button.CENTER)

            if (selected_program != None):
                selected_program()
        
            hub.system.set_stop_button(None)
            hub.light.on(Color.WHITE)
            # require new color selection
            selected_program = None 

            # Stop everything if BLUETOOTH pressed
            if Button.BLUETOOTH in hub.buttons.pressed():
                robot.stop()
                Tanner.stop()
                Grayson.stop()
                hub.speaker.beep(600, 50)
                break

        wait(50)

# ----------------------
# Start menu
# ----------------------
main_menu()