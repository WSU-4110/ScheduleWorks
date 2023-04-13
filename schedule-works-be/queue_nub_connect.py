from typing import List
from dgraph import DGraph


class Scheduler:
    def __init__(self, graph: DGraph):
        self.graph = graph
        self.pq = self.make_priority_queue()

    def make_priority_queue(self) -> List[str]:
        """
        Produce a priority queue of courses from a directed graph.

        TODO:
        return numeric list.
        ensure priority when 2 classes are equal length.
        """
        sorted_by_level = sorted(
            list(self.graph.nodes()), key=lambda x: int(x[3:]), reverse=True
        )
        return sorted_by_level

    def check_course_in_pq(self, course: str) -> bool:
        """
        Check if a course is in the priority queue.
        """
        return course in self.pq

    def schedule(self, courses: List[str], available_courses: List[str]) -> List[str]:
        """
        Generate a course schedule from a list of courses.

        TODO:
        add code to handle circular dependencies.
        """
        schedule = []
        for course in self.pq:
            if course not in courses:
                continue

            # check if the course is available
            if course not in available_courses:
                continue

            # check if all dependencies are scheduled
            deps = self.graph.get_dependencies(course)
            if any(dep not in schedule for dep in deps):
                continue

            schedule.append(course)

        return schedule
