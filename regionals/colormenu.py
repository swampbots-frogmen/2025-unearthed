from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait
from tadpoleBot import robot, Tanner, Grayson

# Import your existing run files
from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

hub = PrimeHub()
color_sensor = ColorSensor(Port.E)

# Disable system stop button (optional)
hub.system.set_stop_button(None)



# ----------------------
# Program functions
# ----------------------
def run_program_red():
    hub.light.on(Color.RED)
    hub.display.number(1)
    wait(200)  # show number briefly before starting run
    R1_run()
    hub.display.clear()
    hub.light.off()

def run_program_yellow():
    hub.light.on(Color.YELLOW)
    hub.display.number(2)
    wait(200)
    R2_run()
    hub.display.clear()
    hub.light.off()

def run_program_blue():
    hub.light.on(Color.BLUE)
    hub.display.number(3)
    wait(200)
    R3_run()
    hub.display.clear()
    hub.light.off()

def run_program_green():
    hub.light.on(Color.GREEN)
    hub.display.number(4)
    wait(200)
    R4_run()
    hub.display.clear()
    hub.light.off()

def run_program_white():
    hub.light.on(Color.WHITE)
    hub.display.number(5)
    wait(200)
    R5_run()
    hub.display.clear()
    hub.light.off()

# ----------------------
# Main Menu
# ----------------------
def main_menu():
    selected_program = None
    hub.light.on(Color.WHITE)

    while True:
        # Detect color
        detected_color = color_sensor.color()

        if detected_color == Color.RED:
            selected_program = run_program_red
            hub.light.on(Color.RED)
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

        hub.system.set_stop_button(Button.CENTER)

        hub.light.on(Color.BROWN)

        selected_program()
    
        hub.system.set_stop_button(None)
        hub.light.on(Color.WHITE)
        selected_program = None  # require new color selection
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