import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        print("顶点  距离源点的最短距离")
        for v in range(self.V):
            print(v, "\t\t", dist[v])

# 创建一个示例图
graph = Graph(6)
graph.graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 2, 7, 0, 0],
    [4, 2, 0, 1, 5, 0],
    [0, 7, 1, 0, 3, 2],
    [0, 0, 5, 3, 0, 6],
    [0, 0, 0, 2, 6, 0],
]

# 在源点0上运行Dijkstra算法
graph.dijkstra(0)
