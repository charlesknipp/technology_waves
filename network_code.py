import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_nodes_from([1,2,3,4,7,13,16,17,19])
G.add_edges_from([
    (1,16),(1,17),(1,19),
    (2,1),(2,3),(2,7),(2,16),(2,19),
    (3,4),(3,16),(3,19),
    (4,16),
    (7,4),
    (13,16),
    (19,16),
])

# nx.draw_shell(G,with_labels=True)
# plt.show()

n = list(nx.lexicographical_topological_sort(G))

adj = nx.adjacency_matrix(G,nodelist=n).todense()
adjT = np.transpose(adj)

hub = np.dot(adj,adjT)
auth = np.dot(adjT,adj)

w1,v1 = np.linalg.eig(hub)
w2,v2 = np.linalg.eig(auth)

print(hub,'\n')
print(auth,'\n')
print(w1,'\n',w2)