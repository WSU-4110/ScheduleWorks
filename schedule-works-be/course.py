"""Course class for easy information access."""
class Course:
    """An object used to store relevant class information manage them easily as nodes in a graph."""

    def __init__(self,
                 attribute_list:list,
                 passed:bool,
                 name:str,
                 credit:int,
                 discipline:str,
                 number:int,
                 term:str(),
                 block_requirement_id:str) -> None:
        """
        Initialize a course object.

        Attributes:
        attribute_list: displays for what the class offers, ie. SI, SS, GE.
        passed: boolean value that states if a course has been passed.
        name: course name or title.
        credits: credits offered by the course.
        discipline: the region that the class covers, ie. CSC, ECO, BIO.
        number: the course number.
        term: term that the course was taken.
        prerequisite_list: list of courses that are required before this course.
        block_requirement_id: the block that a class belongs to as an ID ie. GEN EDS, MATH REQS.
        """
        #these assignments are temporary until we decide implementation
        self.attribute_list = attribute_list
        self.passed = passed
        self.name = name
        self.credits = credit
        self.discipline = discipline
        self.number = number
        self.term = term
        self.prerequisite_list = []
        self.block_requirement_id = block_requirement_id

    def add_req(self,course: 'Course'):
        """Append a prerequisite course to a list."""
        self.prerequisite_list.append(course)

    def print(self)->None:
        """Verbose printing for easy viewing."""
        print(f"{self.discipline:<5}",
              f"{self.number:<5}",
              f"{self.credits:<3}",
              f"{self.name:<30}",
              f"'Passed:' {self.passed:<8}")
        