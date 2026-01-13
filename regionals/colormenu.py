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
color_sensor = ColorSensor(Port.E)

# Disable system stop button (optional)
hub.system.set_stop_button(Button.BLUETOOTH)

# Function Color Map
color_map = {
    Color.RED: 1,
    Color.YELLOW: 2,
    Color.BLUE: 3,
    Color.GREEN: 4,
    Color.WHITE: 5
}

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
            detected_color = color_sensor.color()
            if (detected_color in color_map):
                hub.light.on(detected_color)
                hub.display.char(str(color_map[detected_color]))
            else:
                hub.light.on(Color.CYAN)
                hub.display.icon(Icon.PAUSE)

            print(f"Color: {detected_color}")

            if detected_color == Color.RED:
                selected_program = run_program_red
                hub.light.on(Color.MAGENTA)
            elif detected_color == Color.YELLOW:
                selected_program = run_program_yellow
                hub.light.on(Color.YELLOW)
            elif detected_color == Color.BLUE:
                selected_program = run_program_blue
                hub.light.on(Color.BLUE)
            elif detected_color == Color.GREEN:
                selected_program = run_program_green
                hub.light.on(Color.GREEN)
            elif detected_color == Color.WHITE:
                selected_program = run_program_white
                hub.light.on(Color.WHITE)

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