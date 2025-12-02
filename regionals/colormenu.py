from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait
from tadpoleBot import robot, Tanner, Grayson

# from A_fn_diagnostics import run_diagnostics
from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

hub = PrimeHub()
color_sensor = ColorSensor(Port.E)

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)

# ----------------------
# Program Functions
# ----------------------
def run_program_red():
    print("RUN RED")
    hub.light.on(Color.RED)
    R1_run()
    hub.light.off()

def run_program_blue():
    print("RUN BLUE")
    hub.light.on(Color.BLUE)
    R3_run()
    hub.light.off()

def run_program_yellow():
    print("RUN YELLOW")
    hub.light.on(Color.YELLOW)
    R2_run()
    hub.light.off()

def run_program_white():
    print("RUN WHITE")
    hub.light.on(Color.WHITE)
    R5_run()
    hub.light.off()

def run_program_green():
    print("RUN GREEN")
    hub.light.on(Color.GREEN)
    R4_run()
    hub.light.off()

# ----------------------
# Main Menu
# ----------------------
def main_menu():
    selected_program = None
    hub.light.on(Color.WHITE)

    while True:
        detected_color = color_sensor.color()

        # Select programs by color
        if detected_color == Color.RED:
            print("Red selected")
            selected_program = run_program_red
            hub.light.on(Color.RED)

        elif detected_color == Color.BLUE:
            print("Blue selected")
            selected_program = run_program_blue
            hub.light.on(Color.BLUE)

        elif detected_color == Color.YELLOW:
            print("Yellow selected")
            selected_program = run_program_yellow
            hub.light.on(Color.YELLOW)

        elif detected_color == Color.WHITE:
            print("White selected")
            selected_program = run_program_white
            hub.light.on(Color.WHITE)

        elif detected_color == Color.GREEN:
            print("Green selected")
            selected_program = run_program_green
            hub.light.on(Color.GREEN)

        # If center button is pressed, run selected program
        if Button.CENTER in hub.buttons.pressed():
            if selected_program is not None:

                # ---- IMPORTANT ----
                # Wait until the button is released to avoid SystemExit
                while Button.CENTER in hub.buttons.pressed():
                    wait(10)

                hub.system.set_stop_button(Button.CENTER)

                hub.light.on(Color.BROWN)

                selected_program()
    
                hub.system.set_stop_button(None)
                hub.light.on(Color.WHITE)
                selected_program = None  # require new color selection

        if Button.BLUETOOTH in hub.buttons.pressed():
            robot.stop()
            Tanner.stop()
            Grayson.stop()
            hub.speaker.beep(frequency=1, duration = 50)

        wait(50)


# Start menu
main_menu()
