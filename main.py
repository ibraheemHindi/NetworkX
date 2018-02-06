
import csv
import networkx as nx
import matplotlib.pyplot as plt
import dzcnapy_plotlib as dzcnapy


with open("nutrients.csv") as f: 
	# ---------------------- Prepare the network ----------------------

	csv_data = csv.reader(f)
	G = nx.Graph(csv_data)
	G.remove_edges_from(G.selfloop_edges())

	nutrients = [
		"B12", "Zn", "D", "B6", "A", "Se", "Cu", "Folates", "Ca", 
		"Mn", "Thiamin", "Riboflavin", "C", "E", "Niacin"
	]

	for node in G:
		G.node[node]["nutrient"] = (node in nutrients)


	# ---------------------- Capitalize node names ----------------------

	# mapping = {}
	# for node in G:
	# 	if isinstance(node, str):
	# 		mapping[node] = node.title()

	# nx.relabel_nodes(G, mapping, copy=False)
	# print(G.node)


	# ---------------------- Add/Delete attributes ----------------------

	# G.node["carrots"]["someNodeAttribute"] = "Node Attribute"
	# G.edge["A"]["carrots"]["someEdgeAttribute"] = "Edge Attribute"

	# print(G.node["carrots"])
	# print(G.edge["A"]["carrots"])
	# print()

	# del G.node["carrots"]["someNodeAttribute"]

	# print(G.node["carrots"])
	# print(G.edge["A"]["carrots"])
	# print()


	# ---------------------- Draw the network ----------------------

	# colors = ["yellow" if G.node[current_node]["nutrient"] else "pink" for current_node in G]
	# dzcnapy.medium_attrs["node_color"] = colors

	# _, plot = plt.subplots(2, 2)
	# subplots = plot.reshape(1, 4)[0]
	# layouts = (nx.random_layout, nx.circular_layout, nx.spring_layout, nx.spectral_layout)
	# titles = ("Random", "Circular", "Force-Directed", "Spectral") 

	# for plot, layout, title in zip(subplots, layouts, titles):
	# 	pos = layout(G)
	# 	nx.draw_networkx(G, pos=pos, ax=plot, with_labels=False, **dzcnapy.medium_attrs)
	# 	plot.set_title(title)
	# 	dzcnapy.set_extent(pos, plot)

	# dzcnapy.plot("nutrients")


	# ---------------------- Read/Write graphs ----------------------

	# nx.write_graphml(G, "nutrientsGraph.graphml")
	# storedGraph = nx.read_graphml("nutrients.graphml")
	# print(storedGraph.node)















