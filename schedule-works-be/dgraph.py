import networkx as nx
import matplotlib.pyplot as plt

def course_sum(graph: nx.DiGraph, course: str, memo: dict) -> set:
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
        if len(graph.in_edges(course_id)) == 0:
            included_courses.update([course_id])
            return
        for dependent_course in graph.in_edges(course_id):
            dependent_course = dependent_course[0]
            if dependent_course not in included_courses:
                included_courses.update([dependent_course])
                course_summate(dependent_course)
        return

    course_summate(course)
    return included_courses



def topological_sort(graph: nx.DiGraph) -> list:
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

        for successor in graph.successors(node):
            graph.remove_edge(node, successor)
            if graph.in_degree(successor) == 0:
                zero_in_degree_nodes.append(successor)

    if graph.edges():
        raise ValueError("Graph is not acyclic")
    else:
        return topo_order





def make_priority_queue(graph: nx.DiGraph) -> dict:
    """
    Produce a priority queue of courses from a directed graph.

    TODO:
    return numeric list.
    ensure priority when 2 classes are equal length.
    """
    sorted_by_level = sorted(
        list(graph.nodes()), key=lambda x: int(x[3:]), reverse=True
    )

    memo = {}
    for node in sorted_by_level:
        dependent_courses = course_sum(graph, node, memo)

        memo[node] = dependent_courses
        print(node, ": ", len(dependent_courses))

    return memo


def show_graph(graph):
    """Print a graph out to show node connections."""

    def label_shift(pos, x_shift, y_shift):
        """Shift x and y values given pos tuple list."""
        return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}

    pos = nx.circular_layout(graph)
    nodenames = {n: n[0:3] + "\n" + n[3:] for n in graph.nodes()}
    pos_nodes = label_shift(pos, 0.06, 0)
    nx.draw(graph, pos, node_shape="s", node_size=600)
    nx.draw_networkx_labels(
        graph, pos_nodes, horizontalalignment="right", labels=nodenames
    )
    plt.show()


def main():
    """Example Usage."""
    graph = nx.DiGraph()
    graph.add_edges_from(
        [
            ("CSC3100", "CSC2200"),
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
    show_graph(graph)

    topo_order = topological_sort(graph)
    print("Topological order:", topo_order)
