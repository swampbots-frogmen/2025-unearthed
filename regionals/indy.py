from tadpoleBot import hub, run_task
from pybricks.tools import wait
from pybricks.parameters import Icon

async def play_raiders_march():    
    # The iconic part: bah-bah-bah-BAHHH bah-bah-bahh
    await hub.speaker.play_notes(notes = [
        # First phrase: bah-bah-bah-BAHHH
        "E4/16.", "F4/16", "G4/8", "C5/8_","C5/2",
        "D4/16.", "E4/16", "F4/2.",
        "G4/16.", "A4/16", "B4/8", "F5/8_", "F5/2",
        "A4/16.", "B4/16", "C5/4", "D5/4", "E5/4",

        "E4/16.", "F4/16", "G4/8", "C5/8_", "C5/2",
        "D5/16.", "E5/16", "F5/2",

        "G4/16.", "G4/16", 
        "E5/4_", "D5/16.", "G4/16",
        "E5/4_", "D5/16.", "G4/16",
        "E5/4_", "D5/16.", "G4/16",
        "E5/8", "D5/8"
    ], tempo=150)

if __name__ == '__main__':
    run_task(play_raiders_march())
