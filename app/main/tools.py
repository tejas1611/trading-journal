from enum import Enum

class CHECKLISTS(Enum):
    START_OF_DAY = 1
    BEFORE_TRADE = 2
    AFTER_TRADE = 3
    BP_3_4 = 4
    BUY_SETUP = 5


def read_checklist_file(fname) -> dict:
    read_dict = {}
    heading = ""
    with open(fname, encoding='utf-8') as f:
        for line in f:
            if not line.strip('\n'): continue
            if line.startswith('#'):
                heading = line.strip('# ')
                read_dict[heading] = []
            else:
                read_dict[heading].append(line.strip())

    return read_dict