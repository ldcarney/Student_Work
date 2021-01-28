#Liam Carney
#Algorithms

import networkx as nx

"""
The function to generate the input graph
:return: Returns the NetworkX Graph for Q2
"""
def graph():
    #Create a directed graph
    G = nx.DiGraph()

    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)

    return G


"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: 1000 (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    pylab.title("Input Graph")
    pylab.show()

def shortestPath(G,s,t,k):
    
    #current edge weight from s to t, sets default if non existent
    edge = G.get_edge_data(s,t,default= 1000)
    
    #if edge has weight value
    if(edge != 1000):
        edge = edge.get('weight')
    
    #Base Cases
    if(k==0 and s==t):
        return 0

    if(k==1 and edge != 1000):
        return edge
    
    #set path to default
    path = 1000
    
    #checks each stop in G
    for i in G:
        #gets edqe weight from EC to current stop
        currPath = G.get_edge_data(s,i,default= 1000)

        #if edge exists, get weight
        if(currPath != 1000):
            currPath=currPath.get('weight')

        #if current stop is not EC or HUM and edge exists to current stop
        if(s!=i and t !=i and currPath!= 1000):
            #recursively find path to HUM
            newEdge = shortestPath(G,i,t,k-1)

            #if path exists
            if(newEdge != 1000):
                #find optimal path
                path = min(path, currPath + newEdge)
        
    #return path weight
    return path



def main():
    Graph = graph()
    draw_graph(Graph)

    # Function here takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)
    k = 6
    s ='EC'
    t = 'HUMN'
    weight = shortestPath(Graph,s,t,k)
    print("The shortest path weight with", k, "stops has a weight of", weight)




if __name__ == "__main__":
    # The driver function
    main()