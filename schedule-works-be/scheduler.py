import nub
import dgraph
class Scheduler:
    def __init__(self) -> None:
        unavailable_times = []
        courses_being_taken = []

