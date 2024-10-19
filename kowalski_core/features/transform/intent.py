from enum import Enum

class Intent(str, Enum):
    POLISH     = 'POLISH'
    SUMMARIZE  = 'SUMMARIZE'
    ORGANIZE   = 'ORGANIZE'
    ELABORATE  = 'ELABORATE'
    BRAINSTOMR = 'BRAINSTORM'

    def __str__(self):
        return str(self.value)