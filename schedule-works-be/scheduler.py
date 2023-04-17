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
        self.possible_schedules = []

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

    def clean_courses_queue(self):
        """Remove classes that are not available for the semester. Internal function used by import avil courses."""
        removal_counter = 0
        for i, course in enumerate(self.courses_queue):
            print(course)
            if len(course[2]) == 0:
                del self.courses_queue[i - removal_counter]
                removal_counter += 1
        print("AFTER CLEAN: ", self.courses_queue)

    def classes_conflict(self, course1: cour.Course, course2: cour.Course):
        course1_days = course1.get_days()
        course2_days = course2.get_days()
        shared_days = [0, 0, 0, 0, 0]
        possible_conflict = False
        for i, on_this_day in enumerate(course1_days):
            if on_this_day == True and course2_days[i] == on_this_day:
                possible_conflict = True
                shared_days[i] = 1
        if not possible_conflict:
            return False

        course1_time = course1.get_times()
        course2_time = course2.get_times()

        if course2_time[0] > course1_time[0] and course2_time[0] < course1_time[1]:
            return True
        if course2_time[1] > course1_time[0] and course2_time[1] < course1_time[1]:
            return True

        return False

    def add_course(self, course):
        pass

    def backtrack(self, course_index):
        """Given a list form all appends with the picking list"""
        print(self.courses_queue)
        if course_index == len(self.courses_queue) or self.courses_queue == []:
            # All courses have been scheduled, we found a valid schedule
            print(self.possible_schedules)
            print("out")
            return
        next_course = self.courses_queue.pop(0)

        for section in next_course[2]:
            conflict = False
            for scheduled_course in self.possible_schedules:
                if self.classes_conflict(section, scheduled_course):
                    conflict = True
                    break

            if not conflict:
                self.possible_schedules.append(section)
                self.backtrack(course_index + 1)
                self.possible_schedules.pop()

    def schedule(self):
        """Create all possible schedules that satisfy filters.
        ARGS:
        None as of now but should support filters in the future
        """
        """TODO:
            go in order of queue and slowly build a schedule, 
            backtrack if cant fill
        """
        self.backtrack(0)


def main():
    schedule = Scheduler("202309")
    schedule.schedule()


if __name__ == "__main__":
    main()
