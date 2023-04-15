import nub as nu
import dgraph
import course


class Scheduler:
    def __init__(self, term: str) -> None:
        """Args: term code in string format"""
        self.unavailable_times = []
        self.courses_being_taken = []
        self.nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
        self.nub.set_term("202309")
        self.nub.enable_search()
        self.dgraph = dgraph.Dgraph()
        courses_adjacancy_matrix = self.nub.make_adjancancy_mtrx()
        self.dgraph.graph.add_edges_from(courses_adjacancy_matrix)
        self.courses_queue = self.dgraph.make_priority_queue()

    def get_queue(self):
        """Returns the queue of courses needed in the order they should be taken."""
        return self.courses_queue

    def lecture_sections(self):
        """Parses out the lecture sections from a linked course."""
        pass

    def schedule_course(self, class_to_add: course) -> bool:
        """Insert a class to be included into the schedule."""
        if class_to_add.is_linked():
            return self.schedule_linked_class(class_to_add)
        else:
            pass

    def schedule_linked_class(self, class_to_add: course) -> bool:
        """Used to schedule classes with linked sections."""
        pass

    def schedule(self):
        """Create all possible schedules that satisfy filters.
            ARGS:
            None as of now but should support filters in the future
        """
        for courses in self.courses_queue:
            



def main():
    schedule = Scheduler("202309")

    print(schedule.get_queue())


if __name__ == "__main__":
    main()
