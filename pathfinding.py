def sdfs(start, end):
    road = list()
    visited, queue = set(), [start]
    while len(queue) != 0:
        point = queue.pop()
        if point not in visited and point.is_safe and point.is_permitted:
            road.append(point)
            visited.add(point)
            if point == end:
                return road
            for n in point.neighbours.values():
                queue.append(n)
    return road

def dfs(start, end):
    open_list = set([start])
    closed_list = set()

    g = {}
    g[start] = 0

    pairs = {}
    pairs[start] = start

    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n == None or g[v] < g[n]:
                n = v

        if n == None:
            return None

        if n == end:
            reconst_path = []

            while pairs[n] != n:
                reconst_path.append(n)
                n = pairs[n]

            reconst_path.append(start)
            reconst_path.reverse()
            return reconst_path
        
        for m in list(filter(lambda x: x.is_safe and x.is_permitted, n.neighbours.values())):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                pairs[m] = n
                g[m] = g[n] + 1
            else:
                if g[m] > g[n] + 1:
                    g[m] = g[n] + 1
                    pairs[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        open_list.remove(n)
        closed_list.add(n)