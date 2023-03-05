from sys import setrecursionlimit
setrecursionlimit(100000)


def dfs(graph, colored, now, color):
    global res
    colored[now] = color
    for neighbour in graph[now]:
        if not colored[neighbour]:
            dfs(graph, colored, neighbour, 3 - color)
        elif colored[neighbour] == color:
            res = 'NO'
            return


n, m = map(int, input().split())
adj_matrix = [[] for _ in range(n + 1)]
for _ in range(m):
    v_1, v_2 = map(int, input().split())
    adj_matrix[v_2].append(v_1)
    adj_matrix[v_1].append(v_2)
colored = [0] * (n + 1)
color = 2
res = 'YES'
for i in range(1, n + 1):
    if not colored[i]:
        dfs(adj_matrix, colored, i, 3 - color)
print(res)
