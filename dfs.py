# Adjacency List
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# Recursive DFS
def recursive_dfs(v, discovered=[]): # (first vertex, discovered vertex list)
    discovered.append(v)
    for w in graph[v]: # all vertexs adjacent to vertex v
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
        return discovered


# Iterative DFS using Stack
def Iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered