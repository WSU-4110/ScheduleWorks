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

    def topological_sort(self, graph: nx.DiGraph) -> list:
        """
        Return a list of nodes in topological order.
        Args:
            graph: A directed graph.
        Returns:
            A list of nodes in topological order.
        """
        topo_order = []
        zero_in_degree_nodes = [n for n, d in graph.in_degree() if d == 0]

        while zero_in_degree_nodes:
            node = zero_in_degree_nodes.pop(0)
            topo_order.append(node)

            for successor in list(graph.successors(node)):
                graph.remove_edge(node, successor)
                if graph.in_degree(successor) == 0:
                    zero_in_degree_nodes.append(successor)

        if graph.edges():
            raise ValueError("Graph is not acyclic")
        else:
            return topo_order

    def make_priority_queue(self) -> list:
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

        queue = []
        for entries in memo:
            queue.append([entries, len(memo[entries])])
        queue.sort(key=lambda course: course[1], reverse=True)
        return queue

    def topo_sort(self):
        """Topological sort of directed graph."""
        return

    def show_graph(self, dpi=100):
        """Print a graph out to show node connections."""

        def label_shift(pos, x_shift, y_shift):
            """Shift x and y values given pos tuple list."""
            return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}

        pos = nx.kamada_kawai_layout(self.graph)
        nodenames = {n: n[0:3] + "\n" + n[3:] for n in self.graph.nodes()}
        pos_nodes = label_shift(pos, 0.025, 0)
        nx.draw(self.graph, pos, node_shape="s", node_size=100)
        nx.draw_networkx_labels(
            self.graph,
            pos_nodes,
            horizontalalignment="right",
            labels=nodenames,
            font_size=2,
        )
        plt.show()

    def save_graph(self, filename, dpi=100):
        """Print a graph out to show node connections."""

        def label_shift(pos, x_shift, y_shift):
            """Shift x and y values given pos tuple list."""
            return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}

        pos = nx.circular_layout(self.graph)
        nodenames = {n: n[0:3] + "\n" + n[3:] for n in self.graph.nodes()}
        pos_nodes = label_shift(pos, 0.022, 0)
        plt.figure(figsize=(10, 10))
        nx.draw(self.graph, pos, node_shape="s")
        nx.draw_networkx_labels(
            self.graph,
            pos_nodes,
            horizontalalignment="right",
            labels=nodenames,
            font_size=7,
        )
        plt.savefig(
            "C:\\Program Files\\ScheduleWorks\\schedule-works-fe\\src\\main\\resources\\"
            + filename
            + ".png",
            dpi=dpi,
        )

    def add_edges_from(self, adj_mtrx):
        """Copy of add_edges_from from networkX."""
        self.graph.add_edges_from(adj_mtrx)


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

    courses_graph.save_graph("testing", dpi=200)
    # courses_graph.make_priority_queue()

    # courses_graph.show_graph()

    # topo_order = courses_graph.topological_sort()
    # print("Topological order:", topo_order)


if __name__ == "__main__":
    main()
