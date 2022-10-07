#represent graph
graph = {
    "a":["b","c"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}
# implement depth first search on graph
def dfs(graph, source_node):
    print(source_node,end=" ")
    for neighbour_node in graph[source_node]:
        dfs(graph, neighbour_node)
    
# driver code
dfs(graph, "a")
