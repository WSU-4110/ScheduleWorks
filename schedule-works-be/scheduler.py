import nub as nu
import dgraph
import course as cour
import click


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
        self.possible_schedule = []
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
        """Builds courses_queue by searching for whats available."""
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
        removal_list = []
        for i, course in enumerate(self.courses_queue):
            if len(course[2]) == 0:
                removal_list.append(i)
        for i in sorted(removal_list, reverse=True):
            del self.courses_queue[i]

    def classes_conflict(self, course1: cour.Course, course2: cour.Course):
        course1_days = list(course1.get_days().values())
        course2_days = list(course2.get_days().values())
        # print(course1_days)
        # print(course2_days)
        possible_conflict = False
        for i, on_this_day in enumerate(course1_days):
            if on_this_day == True and course2_days[i] == True:
                possible_conflict = True

        if not possible_conflict:
            # print("?")
            # print()
            return False
        # print()

        course1_time = course1.get_times()
        course2_time = course2.get_times()

        if course2_time[0] >= course1_time[0] and course2_time[0] <= course1_time[1]:
            return True

        if course2_time[1] >= course1_time[0] and course2_time[1] <= course1_time[1]:
            return True

        return False

    def backtrack(self, course_index):
        """Given a list form all appends with the picking list"""
        if course_index == len(self.courses_queue):
            self.possible_schedules.append(self.possible_schedule.copy())
            return
        next_course = self.courses_queue[course_index]
        for section in next_course[2]:
            conflict = False
            for scheduled_course in self.possible_schedule:
                if self.classes_conflict(section, scheduled_course):
                    conflict = True
                    break

            if not conflict:
                self.possible_schedule.append(section)
                self.backtrack(course_index + 1)
                self.possible_schedule.pop()

    def output_to_file(self):
        try:
            with open(
                "C:/Program Files/ScheduleWorks/data/schedule.txt",
                "w+",
                encoding="utf-8",
            ) as outfile:
                for schedule in self.possible_schedules:
                    outfile.write("\n")
                    for course in schedule:
                        outfile.write(str(course))

        except FileNotFoundError as error:
            raise error

    def add_course(self, course_string, priority):
        self.courses_queue.append([course_string, priority])
        self.courses_queue.sort(key=lambda course: course[1], reverse=True)
        self.import_available_courses()

    def add_courses(self, course_array):
        """Adds multiple courses from an array formatted as [[CSC 5290, 5], [CSC 5830, 7], ...]."""
        for courses in course_array:
            self.add_course(courses[0], int(courses[1]))

    def schedule(self):
        """Create all possible schedules that satisfy filters and saves to file.
        ARGS:
        None as of now but should support filters in the future
        """
        """TODO:
            go in order of queue and slowly build a schedule, 
            backtrack if cant fill
        """
        self.backtrack(0)
        self.output_to_file()

    def __repr__(self):
        large_string = ""
        for schedule in self.possible_schedules:
            for course in schedule:
                large_string += str(course) + "|"
            large_string += "\n"
        return large_string


@click.command()
@click.option("--courses", "-m", default=(), required=False)
def main(courses):
    schedule = Scheduler("202309")
    if courses != None:
        courses_to_add = format_for_add(courses)
        schedule.add_courses(courses_to_add)

    # CSC 5290 and PS3080 cant be together

    # schedule.add_course("CSC 5290", 3)
    # schedule.add_course("PS 3080", 5)
    # schedule.add_course("CSC 3200", 3)
    # schedule.add_course("CSC 3400", 3)
    # schedule.add_course("ARB 1010", 3)

    schedule.schedule()
    print(schedule)


def format_for_add(source):
    source = str(source)
    source = source.split(" ")
    formatted_list = []
    temp = []
    for i, entry in enumerate(source):
        curr = i % 3
        if curr == 0:
            temp.append(entry)
        if curr == 1:
            temp[curr - 1] = temp[curr - 1] + " " + entry
        elif curr == 2:
            temp.append(entry)
            formatted_list.append(temp.copy())
            temp.clear()
    return formatted_list


if __name__ == "__main__":
    main()
