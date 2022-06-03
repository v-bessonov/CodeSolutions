import heapq


class MinCostToConnectAllPointsMstPrim:
    #  O(n^2logn)
    @staticmethod
    def min_cost_connect_points(points: list[list[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(len(points))}

        for i in range(N):  # i : list[cost, node]
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # Prim's
        res = 0
        visit = set()
        min_h = [[0, 0]]

        while len(visit) < N:
            cost, i = heapq.heappop(min_h)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_h, [neiCost, nei])
        return res
