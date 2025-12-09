import math


class Solution:
    def attach_closest_junctions(self, data: list[list[int]]) -> int:
        connections = 1000

        coords = [tuple(coord) for coord in data]

        distances = []
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dist = math.dist(coords[i], coords[j])
                distances.append((dist, (coords[i], coords[j])))

        distances.sort(key=lambda x: x[0])
        distances = distances[:connections]

        graph = {}
        for _, (a, b) in distances:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)

        for coord in coords:
            graph.setdefault(coord, set())

        visited = set()
        circuits = []
        for node in graph:
            if node not in visited:
                stack = [node]
                current_circuit = []

                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        current_circuit.append(current)
                        stack.extend(graph[current] - visited)

                circuits.append(current_circuit)

        circuits.sort(key=len, reverse=True)

        return math.prod(len(c) for c in circuits[:3])

    def connect_until_single_circuit(self, data: list[list[int]]) -> int:
        coords = [tuple(coord) for coord in data]

        distances = []
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dist = math.dist(coords[i], coords[j])
                distances.append((dist, (coords[i], coords[j])))

        distances.sort(key=lambda x: x[0])

        parent = {coord: coord for coord in coords}
        size = {coord: 1 for coord in coords}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]

        for dist, (a, b) in distances:
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                union(a, b)
                last_connection = (a, b)

                if len(set(find(coord) for coord in coords)) == 1:
                    return last_connection[0][0] * last_connection[1][0]

        return -1


if __name__ == "__main__":
    with open("input") as file:
        contents = file.read()
        data = [list(map(int, line.split(","))) for line in contents.strip().split("\n")]

    solution = Solution()
    print(solution.attach_closest_junctions(data))
    print(solution.connect_until_single_circuit(data))
