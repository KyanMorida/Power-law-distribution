import sys
import heapq
import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.weights = [[(sys.maxsize, 0)] * vertices for _ in range(vertices)]

    def update_weights(self, time_interval):
        # 假设每个时间单位的权重增加0.5
        for i in range(self.V):
            for j in range(self.V):
                current_weight, current_time = self.weights[i][j]
                new_weight = current_weight + 0.5
                new_time = current_time + time_interval
                self.weights[i][j] = (new_weight, new_time)

    def re_route(self, src, dest):
        # 创建优先队列用于存储顶点和对应的最短距离
        pq = [(0, src)]
        # 存储从源节点到各个节点的最短距离
        dist = [sys.maxsize] * self.V
        dist[src] = 0

        while pq:
            # 从优先队列中获取当前距离源节点最近的顶点
            curr_dist, curr_vertex = heapq.heappop(pq)

            # 如果当前顶点是目标节点，终止算法
            if curr_vertex == dest:
                break

            # 如果当前顶点已被处理过，跳过该顶点
            if curr_dist > dist[curr_vertex]:
                continue

            # 遍历与当前顶点相连的邻居顶点
            for v in range(self.V):
                weight, _ = self.weights[curr_vertex][v]

                # 计算从源节点经过当前顶点到达邻居顶点的距离
                new_dist = curr_dist + weight

                # 如果新距离比当前存储的距离小，则更新最短距离并加入优先队列
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist[dest]

    def periodic_recalculate(self, src, dest, time_interval, recal_interval):
        while True:
            # 更新权重矩阵
            self.update_weights(time_interval)

            # 执行最短路径计算
            shortest_dist = self.re_route(src, dest)
            print("源点到目标节点的最短距离：", shortest_dist)

            # 等待指定的重新计算时间间隔
            time.sleep(recal_interval)

# 创建一个示例图
graph = Graph(6)
graph.weights = [
    [(0, 0), (1, 0), (4, 0), (sys.maxsize, 0), (sys.maxsize, 0), (sys.maxsize, 0)],
    [(1, 0), (0, 0), (2, 0), (7, 0), (sys.maxsize, 0), (sys.maxsize, 0)],
    [(4, 0), (2, 0), (0, 0), (1, 0), (5, 0), (sys.maxsize, 0)],
    [(sys.maxsize, 0), (7, 0), (1, 0), (0, 0), (3, 0), (2, 0)],
    [(sys.maxsize, 0), (sys.maxsize, 0), (5, 0), (3, 0), (0, 0), (6, 0)],
    [(sys.maxsize, 0), (sys.maxsize, 0), (sys.maxsize, 0), (2, 0), (6, 0), (0, 0)],
]

# 在源点0和目标节点4之间以及每隔2秒重新计算最短路径
graph.periodic_recalculate(0, 4, 0.5, 2)
