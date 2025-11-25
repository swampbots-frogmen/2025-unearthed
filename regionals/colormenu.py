# Coded with help from: https://github.com/coder-ella/lego/blob/main/pybricks/masterpiece/A_main_menu.py#L8
from pybricks.tools import wait
from pybricks.parameters import Button, Icon
from tadpoleBot import hub, robot, Tanner, Grayson
from colorDectector import detect_color

# from A_fn_diagnostics import run_diagnostics
from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

default_settings = robot.settings()

menu_map = { "RED": 0, "YELLOW": 1, "GREEN": 2, "ORANGE": 3, "BLUE": 4 }
menu_options = ("1", "2", "3", "4", "5")
menu_index = 0
num_options = len(menu_options)

def do_menu(hub):
    # menu_index is global, so that it can remember what the last menu-index was
    global menu_index

    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    hub.system.set_stop_button(None)

    while True:
        hub.display.char(menu_options[menu_index])

        color = detect_color()

        while color == "OPEN":
            wait(10)
            print("Detecting Color...")
            color = detect_color()
            if (color != "OPEN"):
                menu_index = menu_map[color]
                print(f"The Color: {color}. Menu Index: {menu_index}")

        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)

        # # and then wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

            print("Program stopped checking color")
            hub.system.set_stop_button(Button.CENTER)
            selected = menu_options[menu_index]

        if Button.BLUETOOTH in pressed:
            # This is the exit key!
            return "X"
        # Now check which button was pressed.
        # if Button.CENTER in pressed:
        #     # Center button, this is the selection button, so we can exit the
        #     # selection loop
        #     menu_index = 1
        #     break

        # elif Button.RIGHT in pressed:
        #     # Left button, so decrement menu menu_index.
        #     menu_index -= 1
        #     if (menu_index < 0): #roll over!
        #         menu_index = num_options - 1

        # elif Button.LEFT in pressed:
        #     # Right button, so increment menu menu_index.
        #     menu_index += 1
        #     if (menu_index >= num_options):
        #         menu_index = 0
    
    # Now we want to use the Center button as the stop button again.
    # print("Program stopped checking color")
    # hub.system.set_stop_button(Button.CENTER)
    # selected = menu_options[menu_index]
    
    return selected

if hub.imu.ready():
    hub.display.icon(Icon.HEART)
else:
    hub.speaker.play_notes(["C3/4","D3/4","C2/2"])
    hub.display.icon(Icon.FALSE)

selected = ""
while True:
    try:
        # Based on the selection, choose a program.
        selected = do_menu(hub)

        if selected == "1":
            R1_run()
        elif selected == "2":
            R2_run()
        elif selected == "3":
            R3_run()
        elif selected == "4":
            R4_run()
        elif selected == "5":
            R6_run()
        else:
            print(f"don't know selected value {selected}")
            selected = "X"
            # this is the only way to stop PyBricks
            raise SystemExit("Closing program..")

    except SystemExit:
        if selected == "X":
            raise SystemExit()
        robot.stop()
        Tanner.stop()
        Grayson.stop()
        hub.speaker.beep(frequency=1, duration = 50)
        while hub.buttons.pressed():
            wait(100) # wait for button to be released
