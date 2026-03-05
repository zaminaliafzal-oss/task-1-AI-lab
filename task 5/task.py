def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor, cost in graph[current]:
            tentative_g = g_cost[current] + cost
            if tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))
    return None