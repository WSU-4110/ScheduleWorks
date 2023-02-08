import networkx as nx
import matplotlib.pyplot as plt
# def topo_pos(G):
#     """Display in topological order, with simple offsetting for legibility"""
#     pos_dict = {}
#     for i, node_list in enumerate(nx.topological_generations(G)):
#         x_offset = len(node_list) / 2
#         y_offset = 0.1
#         for j, name in enumerate(node_list):
#             pos_dict[name] = (j - x_offset, -i + j * y_offset)
#     return pos_dict


def label_shift(pos, x_shift, y_shift):
    """pos is a numbered dict with (x,y) tuples for values, apply a shift to the cords and return it"""
    return {n:(x + x_shift, y + y_shift) for n,(x,y) in pos.items()}
# Same example data as top answer, but directed
G=nx.DiGraph()
G.add_edges_from([("CSC3100","CSC2200"),("CSC2200","CSC2110"),("CSC4410","CSC2200"),("CSC4410","CSC3100"),("CSC2200","CSC1500"),("CSC2110","CSC1500")])
pos = nx.circular_layout(G)
"""Notes: 
using G.degree() get node connections

following these nodes backwards create a new heiarchy by adding its requirement count
to its requirements.

Ie. 
[('CSC3100', 2), ('CSC2200', 4), ('CSC2110', 1), ('CSC4410', 2), ('CSC1500', 1)]
CSC 1500 is required to take 2200, so the four classes that require 2200 also require 1500
add 4 and 1 and make csc1500 at priority 1, with no preqs
"""

nodenames = {n:n[0:3]+"\n"+n[3:] for n in G.nodes()}

# print(pos)
print(G.nodes())
print(G.degree())
pos_nodes = label_shift(pos, 0.05, 0) 
print("out ",G.in_edges("CSC2200") )

nx.draw(G, pos,node_shape="s",node_size=600)
# nx.draw_networkx_labels(G, pos_nodes, horizontalalignment="right",labels=nodenames)
# plt.show()

def course_sum(dir_graph: nx.DiGraph,course:str):
    included_courses = []
    def course_summate(d_graph: nx.DiGraph,course_id:str) -> int:
        print(course_id, included_courses)
        if len(G.in_edges(course_id))<=0:
            return 1
        for pre_req in G.in_edges(course_id):
            if(pre_req[0] not in included_courses):
                included_courses.append(pre_req[0])
                return 1 + course_summate(G,pre_req[0])
    return course_summate(dir_graph,course)
        
print(course_sum(G,"CSC2200"))
# for node in G.nodes():
#     print(node, " ",course_summate(G,node,[]))

