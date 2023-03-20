import networkx as nx
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    main()