#represent graph
graph = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}
# implement depth first search on graph
def dfs(graph, source_node):
    stack = []
    stack.append(source_node)
    while(len(stack)>0):
        current_node = stack.pop()
        print(current_node, end=" ")
        for neighbour_node in graph[current_node]:
            stack.append(neighbour_node)
    

# driver code
dfs(graph, "a")
