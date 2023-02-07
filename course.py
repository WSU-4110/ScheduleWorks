"""Course class for easy information access."""
class Course:
    """An object used to store relevant class information manage them easily as nodes in a graph."""

    def __init__(self) -> None:
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
        self.attribute_list = list()
        self.passed = bool()
        self.name = str()
        self.credits = int()
        self.discipline = str()
        self.number = int()
        self.term = str()
        self.prerequisite_list = list()
        self.block_requirement_id = str()
        