from tadpoleBot import hub
from pybricks.tools import wait
from pybricks.parameters import Icon

async def play_potc():
    await hub.speaker.play_notes(notes = [
      # Adventure Theme – Original Composition
      "E4/8", "B4/8", "E5/4", "R/8",
      "D5/8", "C5/8", "B4/8", "G4/4", "R/8",

      "C5/8", "E5/8", "G5/4", "R/8",
      "F5/8", "E5/8", "D5/8", "B4/4", "R/8",

      "E4/8", "G4/8", "B4/8", "E5/4", "R/8",
      "D5/8", "F5/8", "E5/8", "C5/4", "R/8",

      "G4/8", "A4/8", "C5/4", "R/8",
      "B4/8", "A4/8", "G4/8", "E4/4", "R/8",
    ], tempo=255)
    wait(3000)
