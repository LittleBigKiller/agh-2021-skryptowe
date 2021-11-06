from enum import Enum

class Action(Enum):
    DAY_EARLIER = 'd-'
    DAY_LATER = 'd+'
    TIME_EARLIER = 't-'
    TIME_LATER = 't+'
