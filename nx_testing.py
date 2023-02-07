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
G.add_edges_from([("CSC3100","CSC2200"),("CSC2200","CSC2110"),("CSC4410","CSC2200"),("CSC4410","CSC3100"),("CSC2200","CSC1500")])
pos = nx.circular_layout(G)
print(pos)
pos_nodes = label_shift(pos, 0.1, 0) 

nx.draw(G, pos,node_shape="s",node_size=600)
nx.draw_networkx_labels(G, pos_nodes, horizontalalignment="right")
plt.show()
#plt.savefig("testing.png")