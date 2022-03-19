def dfs(start, end):
    road = list()
    visited, queue = set(), [start]
    while len(queue) != 0:
        point = queue.pop()
        if point not in visited and point.is_safe and point.is_permitted:
            road.append(point)
            visited.add(point)
            if point == end:
                return road
            for n in point.neighbors:
                queue.append(n)
    return road
