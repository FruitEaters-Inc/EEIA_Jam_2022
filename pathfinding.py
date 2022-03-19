def dfs(start, end):
    road = list()
    visited, queue = set(), [start]
    while not queue.empty():
        point = queue.pop()
        if not point in visited:
            road.append(point)
            visited.append(point)
            if point == end:
                return road
            for n in point.neighbors:
                queue.append(n)