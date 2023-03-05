def dfs(graph, visited, now):
    global connectivity, components
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            connectivity += 1
            components.append(neig)
            dfs(graph, visited, neig)


n, m = map(int, input().split())
adj_matrix = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
connectivity = 1
components = [1]
for _ in range(m):
    n_1, n_2 = map(int, input().split())
    adj_matrix[n_1].append(n_2)
    adj_matrix[n_2].append(n_1)
dfs(adj_matrix, visited, 1)
print(connectivity)
print(*sorted(components))
