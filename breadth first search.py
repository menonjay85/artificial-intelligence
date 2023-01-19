from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]

def edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def bfs(s, t, n):
    visited = [0] * n
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, s))

    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end = " ")
        if u == t:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
        print()



edge(0, 1, 3)
edge(0, 2, 6)
edge(0, 3, 5)
edge(1, 4, 9)
edge(1, 5, 8)
edge(2, 6, 12)
edge(2, 7, 14)
edge(3, 8, 7)
edge(8, 9, 5)
edge(8, 10, 6)
edge(9, 11, 1)
edge(9, 12, 10)
edge(9, 13, 2)
s = 0
t = 9
bfs(s, t, v)