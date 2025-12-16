from pybricks.tools import hub_menu
from tadpoleBot import run_task, multitask
from indy import march_twice

from run_1 import R1_run
from run_2 import R2_run
from run_3 import R3_run
from run_4 import R4_run
from run_5 import R5_run

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5")

# Based on the selection, run a program.
if selected == "1":
    run_task(multitask(R1_run(), march_twice()))
elif selected == "2":
    run_task(R2_run())
elif selected == "3":
    R3_run()
elif selected == "4":
    run_task(R4_run())
elif selected == "5":
    run_task(R5_run())
