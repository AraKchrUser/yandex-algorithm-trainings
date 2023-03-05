def dfs(graph, visited, now):
    global count, items
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            count += 1
            items.append(neig)
            dfs(graph, visited, neig)


n, m = map(int, input().split())
adj_matrix = [[] for _ in range(n + 1)]
for _ in range(m):
    v_1, v_2 = map(int, input().split())
    adj_matrix[v_1].append(v_2)
    adj_matrix[v_2].append(v_1)
comp_ = 0
visited = [0] * (n + 1)
comp_dict = []
for i in range(1, n + 1):
    if not visited[i]:
        count = 1
        items = [i]
        dfs(adj_matrix, visited, i)
        comp_ += 1
        comp_dict.append([count, items])
print(comp_)
for k, v in comp_dict:
    print(k, ' '.join(map(str, v)), sep='\n')
