import nub as nu
import dgraph
import course as cour


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
        self.import_available_courses()

    def get_queue(self):
        """Returns the queue of courses needed in the order they should be taken."""
        return self.courses_queue

    def lecture_sections(self):
        """Parses out the lecture sections from a linked course."""
        pass

    def schedule_course(self, class_to_add) -> bool:
        """Insert a class to be included into the schedule."""
        if class_to_add.is_linked():
            return self.schedule_linked_class(class_to_add)
        else:
            pass

    def schedule_linked_class(self, class_to_add) -> bool:
        """Used to schedule classes with linked sections."""
        pass

    def import_available_courses(self):
        for i, course in enumerate(self.courses_queue):
            parsed_course = course[0].split(" ")
            courses_sections = self.nub.search_class(parsed_course[0], parsed_course[1])
            self.courses_queue[i].append([])
            if "Error" in courses_sections[0].keys():
                continue
            for section in courses_sections:
                self.courses_queue[i][2].append(cour.Course(section))
            self.clean_courses_queue()
            print(self.courses_queue)

    def clean_courses_queue(self):
        """Remove classes that are not available for the semester. Internal function used by import avil courses."""
        for i, course in enumerate(self.courses_queue):
            if course[2] == []:
                del self.courses_queue[i]

    def schedule(self):
        """Create all possible schedules that satisfy filters.
        ARGS:
        None as of now but should support filters in the future
        """
        """TODO:
            go in order of queue and slowly build a schedule, 
            backtrack if cant fill
           """


def main():
    schedule = Scheduler("202309")
    schedule.schedule()


if __name__ == "__main__":
    main()
