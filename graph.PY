import json
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_from_json(json_file_path):
    
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    
    image_data = data[0]

    
    G = nx.DiGraph()

    
    for obj in image_data["objects"]:
        G.add_node(obj["object_id"], label=obj["names"][0])

    
    for rel in image_data["relationships"]:
        G.add_edge(rel["subject"]["object_id"], rel["object"]["object_id"], label=rel["predicate"])

    
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)  

    
    nx.draw_networkx_nodes(G, pos, node_size=700)

    
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='black')

    
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12)

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.axis('off')
    plt.show()


draw_graph_from_json('8911.json')
