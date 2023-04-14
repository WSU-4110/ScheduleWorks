import nub as nu
import dgraph
import course
class Scheduler:
    def __init__(self,term) -> None:
        self.unavailable_times = []
        self.courses_being_taken = []
        nub =nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
        nub.set_term("202309")
        nub.enable_search()




    def lecture_sections(self):
        pass

    def schedule_course(self,class_to_add:course) -> bool:
        """Insert a class to be included into the schedule."""
        if class_to_add.is_linked():
            return self.schedule_linked_class(class_to_add)
        else:
            pass


    def schedule_linked_class(self,class_to_add:course) -> bool:
        pass


