import networkx as nx
import matplotlib.pyplot as plt
import time


def label_shift(pos, x_shift, y_shift):
    """pos is a numbered dict with (x,y) tuples for values, apply a shift to the cords and return it"""
    return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}


# Same example data as top answer, but directed
G = nx.DiGraph()

G.add_edges_from(
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
pos = nx.circular_layout(G)

"""Notes: 
using G.degree() get node connections

following these nodes backwards create a new heiarchy by adding its requirement count
to its requirements.


A course should point towards its prerequisite

Ie. 
[('CSC3100', 2), ('CSC2200', 4), ('CSC2110', 1), ('CSC4410', 2), ('CSC1500', 1)]
CSC 1500 is required to take 2200, so the four classes that require 2200 also require 1500
add 4 and 1 and make csc1500 at priority 1, with no preqs

more notes:

courses are fed into recursion by dict
dict[course] = [pre-req1,pre-req2]

transform into choose 2 unique tuple ((course,prereq1),(course,prereq2))

"""

nodenames = {n: n[0:3] + "\n" + n[3:] for n in G.nodes()}
print(nodenames)

# print(pos)
print(G.nodes())
print(G.degree())
pos_nodes = label_shift(pos, 0.05, 0)
print("dependencies: ", G.in_edges("CSC1500"))
print(len(G.in_edges("CSC1500")))

for dependent_course in G.in_edges("CSC1500"):
    print(dependent_course[0])

nx.draw(G, pos, node_shape="s", node_size=600)
nx.draw_networkx_labels(G, pos_nodes, horizontalalignment="right", labels=nodenames)
plt.show()


def course_sum(dir_graph: nx.DiGraph, course: str) -> int:

    included_courses = set()

    def course_summate(d_graph: nx.DiGraph, course_id: str) -> int:
        if len(d_graph.in_edges(course_id)) == 0:
            return 1
        for dependent_course in d_graph.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                included_courses.add(dependent_course[0])
                continue_current_thread = course_summate(d_graph, course_id)
                advance_to_next_course = course_summate(d_graph, dependent_course[0])

                return 1 + continue_current_thread + advance_to_next_course
        return 0

    return course_summate(dir_graph, course)


def course_sum_memo(dir_graph: nx.DiGraph, course: str, memo: dict) -> int:
    included_courses = set()

    def course_summate(d_graph: nx.DiGraph, course_id: str) -> int:
        if len(d_graph.in_edges(course_id)) == 0:
            included_courses.add(course_id)
            return 1
        for dependent_course in d_graph.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                included_courses.add(dependent_course[0])
                if dependent_course[0] in memo.keys():
                    advance_to_next_course = len(memo[dependent_course[0]][1])
                    # print(course_id," seen: ",dependent_course[0], memo[dependent_course[0]])
                    included_courses.union(memo[dependent_course[0]][1])
                else:
                    advance_to_next_course = course_summate(
                        d_graph, dependent_course[0][0]
                    )

                continue_current_thread = course_summate(d_graph, course_id)

                return 1 + continue_current_thread + advance_to_next_course
        return 0

    return course_summate(dir_graph, course), included_courses


sorted_by_level = sorted(list(G.nodes()), key=lambda x: int(x[3:]), reverse=True)


# tic = time.perf_counter()
# for node in sorted_by_level:
#     print(node ,": ", course_sum(G,node))
# toc = time.perf_counter()
# print(f"Normal recursion in {toc - tic:0.4f} seconds")

# tic = time.perf_counter()

# saved_priority={}
# merge = set()

# for node in sorted_by_level:
#     priority,merge= course_sum_memo(G,node,saved_priority)
#     saved_priority[node] = (priority,merge)
#     print(node, ": ",priority)

# toc = time.perf_counter()

# print(f"Memoization in {toc - tic:0.4f} seconds")


def course_sum2(dir_graph: nx.DiGraph, course: str) -> list:
    def course_summate(
        d_graph: nx.DiGraph, course_id: str, included_courses=set()
    ) -> list:
        temp_courses = set()
        if len(d_graph.in_edges(course_id)) == 0:
            return [course_id]
        for dependent_course in d_graph.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                temp_courses.add(dependent_course[0])
        for course_not_reached in temp_courses:
            included_courses.add(course_not_reached)
            current_thread = course_summate(d_graph, course_id, included_courses)
            return course_summate(d_graph, course_not_reached, included_courses) + (
                current_thread
            )
        return [course_id]

    return course_summate(dir_graph, course)


def course_sum3(dir_graph: nx.DiGraph, course: str, memo: dict) -> list:
    def course_summate(
        d_graph: nx.DiGraph, course_id: str, included_courses=set()
    ) -> list:
        if course_id in memo.keys():
            return memo[course_id]
        temp_courses = set()
        if len(d_graph.in_edges(course_id)) == 0:
            return [course_id]
        for dependent_course in d_graph.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                temp_courses.add(dependent_course[0])
        for course_not_reached in temp_courses:
            included_courses.add(course_not_reached)
            current_thread = course_summate(d_graph, course_id, included_courses)
            return course_summate(d_graph, course_not_reached, included_courses) + (
                current_thread
            )
        return [course_id]

    return course_summate(dir_graph, course)


def working_course_sum(dir_graph: nx.DiGraph, course: str, memo: dict) -> list:
    def course_summate(
        d_graph: nx.DiGraph, course_id: str, included_courses=set()
    ) -> list:
        if course in memo.keys():
            included_courses.update(set(memo[course]))
            return memo[course]
        temp_courses = set()
        if len(d_graph.in_edges(course_id)) == 0:
            return [course_id]
        for dependent_course in d_graph.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                temp_courses.add(dependent_course[0])
        for course_not_reached in temp_courses:
            included_courses.add(course_not_reached)
            current_thread = course_summate(d_graph, course_id, included_courses)
            return course_summate(d_graph, course_not_reached, included_courses) + (
                current_thread
            )
        return [course_id]

    return course_summate(dir_graph, course)


def course_sum4(G: nx.DiGraph, course: str, memo: dict) -> list:
    """
    Determine a given courses dependency count. See make_priority_queue() to use properly.

    Wrapper function to clarify args used during recursion.
    Functions best when courses are fed in order from least expected dependency to most.


    Args:
    G: A directed graph containing courses and edges that point towards a courses prequisite.
    course: The course that is being analysed for priority count.
    memo: Memoization dict to speed up complex prerequisties
    """

    def course_summate(course_id: str, included_courses=set()) -> list:
        """Recursive function to return a list of prereq courses given a course."""
        if course_id in memo.keys():
            return memo[course_id]
        temp_courses = set()
        if len(G.in_edges(course_id)) == 0:
            return [course_id]
        for dependent_course in G.in_edges(course_id):
            if dependent_course[0] not in included_courses:
                temp_courses.add(dependent_course[0])
        for course_not_reached in temp_courses:
            included_courses.add(course_not_reached)
            current_thread = course_summate(course_id, included_courses)
            return course_summate(course_not_reached, included_courses) + (
                current_thread
            )
        return [course_id]

    return course_summate(course)


def make_priority_queue(G: nx.DiGraph) -> dict:
    """
    Produce a priority queue of courses from a directed graph.

    TODO:
    return numeric list.
    ensure priority when 2 classes are equal length.
    """

    memo = {}
    for node in sorted_by_level:
        dependent_courses = course_sum4(G, node, memo)
        memo[node] = dependent_courses

    return memo


print()
print()

tic = time.perf_counter()
for node in sorted_by_level:
    arr = course_sum2(G, node)
    print(node, ": ", len(arr))
toc = time.perf_counter()
print(f"     Normal in {toc - tic:0.5f} seconds")

# print()
# memo = {}
# tic = time.perf_counter()
# for node in sorted_by_level:
#     arr = course_sum4(G, node, memo)
#     memo[node] = arr
#     print(node, ": ", len(arr))
# toc = time.perf_counter()
# print(f"Memoization in {toc - tic:0.5f} seconds")
# print()

# memo = {}
# tic = time.perf_counter()
# for node in sorted_by_level:
#     arr = course_sum3(G, node, memo)
#     memo[node] = arr
#     print(node, ": ", len(arr))
# toc = time.perf_counter()
# print(f"Memoization in {toc - tic:0.5f} seconds")


# print(memo==make_priority_queue(G))
