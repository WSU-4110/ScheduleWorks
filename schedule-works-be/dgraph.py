"""Class for interacting with directed graph structure."""

import networkx as nx
import matplotlib.pyplot as plt


class Dgraph:
    """Wrapper adapater class for networkx Directed Graphs."""

    # graph = None

    def __init__(self):
        self.graph = nx.DiGraph()

    def course_sum(self, course: str, memo: dict) -> set:
        """
        Determine a given course's dependency list. See make_priority_queue() to use properly.

        Wrapper function to clarify args used during recursion.
        Functions best when courses are fed in order from least expected dependency to most.


        Args:
        G: A directed graph containing courses and edges that point towards a courses prequisite.
        course: The course that is being analysed for priority count.
        memo: Memoization dict to speed up complex prerequisties
        """

        included_courses = set()

        def course_summate(course_id: str) -> None:
            """Recursive function to return a list of prereq courses given a course."""

            if course_id not in included_courses:
                included_courses.update([course_id])
            if course_id in memo.keys():
                included_courses.update(memo[course_id])
                return
            if len(self.graph.in_edges(course_id)) == 0:
                included_courses.update([course_id])
                return
            for dependent_course in self.graph.in_edges(course_id):
                dependent_course = dependent_course[0]
                if dependent_course not in included_courses:
                    included_courses.update([dependent_course])
                    course_summate(dependent_course)
            return

        course_summate(course)
        return included_courses

    def make_priority_queue(self) -> dict:
        """
        Produce a priority queue of courses from a directed graph.

        TODO:
        return numeric list.
        ensure priority when 2 classes are equal length.
        """
        sorted_by_level = sorted(
            list(self.graph.nodes()), key=lambda x: int(x[3:]), reverse=True
        )

        memo = {}
        for node in sorted_by_level:
            dependent_courses = self.course_sum(node, memo)

            memo[node] = dependent_courses
            print(node, ": ", len(dependent_courses))

        return memo

    def topo_sort(self):
        pass

    def show_graph(self):
        """Print a graph out to show node connections."""

        def label_shift(pos, x_shift, y_shift):
            """Shift x and y values given pos tuple list."""
            return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}

        pos = nx.circular_layout(self.graph)
        nodenames = {n: n[0:3] + "\n" + n[3:] for n in self.graph.nodes()}
        pos_nodes = label_shift(pos, 0.06, 0)
        nx.draw(self.graph, pos, node_shape="s", node_size=600)
        nx.draw_networkx_labels(
            self.graph, pos_nodes, horizontalalignment="right", labels=nodenames
        )
        plt.show()


def main():
    """Example Usage."""
    courses_graph = Dgraph()
    courses_graph.graph.add_edges_from(
        [
            ["CSC3100", "CSC2200"],
            ("CSC2200", "CSC2110"),
            ("CSC4410", "CSC2200"),
            ("CSC4410", "CSC3100"),
            ("CSC2200", "CSC1500"),
            ("CSC2110", "CSC1500"),
            ("CSC5000", "CSC3100"),
            ("CSC1500", "CSC1100"),
            ("CSC4710", "CSC2200"),
            ("CSC4710", "CSC3020"),
        ]
    )
    courses_graph.show_graph()
    courses_graph.make_priority_queue()


if __name__ == "__main__":
    main()
