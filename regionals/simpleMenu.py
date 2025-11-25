from pybricks.tools import hub_menu

from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3")

# Based on the selection, run a program.
if selected == "1":
    R1_run()
elif selected == "2":
    R2_run()
elif selected == "3":
    R3_run()
