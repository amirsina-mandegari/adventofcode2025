class Solution:
    def find_biggest_area(self, data):
        biggest_area = 0
        p1 = 0
        p2 = 1
        while p2 < len(data):
            for i in range(p1, len(data)):
                for j in range(p2, len(data)):
                    biggest_area = max(self._calculate_area(data[i], data[j]), biggest_area)
            p1 += 1
            p2 += 1
        return biggest_area

    def _calculate_area(self, point1, point2):
        return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

    def find_biggest_area_in_region(self, data):
        n = len(data)
        edges = []
        for i in range(n):
            p1 = tuple(data[i])
            p2 = tuple(data[(i + 1) % n])
            edges.append((p1, p2))

        vertices = [tuple(p) for p in data]

        biggest_area = 0

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                p1, p2 = data[i], data[j]

                min_x = min(p1[0], p2[0])
                max_x = max(p1[0], p2[0])
                min_y = min(p1[1], p2[1])
                max_y = max(p1[1], p2[1])

                if self._valid_rectangle(min_x, max_x, min_y, max_y, edges, vertices):
                    area = (max_x - min_x + 1) * (max_y - min_y + 1)
                    biggest_area = max(biggest_area, area)
        return biggest_area

    def _valid_rectangle(self, min_x, max_x, min_y, max_y, edges, vertices):
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        for cx, cy in corners:
            if not self._point_in_polygon(cx, cy, vertices):
                return False
        for p1, p2 in edges:
            if self._edge_cross_rectangle(p1, p2, min_x, max_x, min_y, max_y):
                return False

        return True

    def _point_in_polygon(self, cx, cy, vertices):
        n = len(vertices)
        crossings = 0
        for i in range(n):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % n]

            if p1[0] == p2[0] == cx:
                if min(p1[1], p2[1]) <= cy <= max(p1[1], p2[1]):
                    return True
            elif p1[1] == p2[1] == cy:
                if min(p1[0], p2[0]) <= cx <= max(p1[0], p2[0]):
                    return True

            if p1[0] == p2[0]:
                edge_x = p1[0]
                edge_min_y = min(p1[1], p2[1])
                edge_max_y = max(p1[1], p2[1])

                if edge_x < cx and edge_min_y < cy <= edge_max_y:
                    crossings += 1
        return crossings % 2 == 1

    def _edge_cross_rectangle(self, p1, p2, min_x, max_x, min_y, max_y):
        if p1[0] == p2[0]:
            edge_x = p1[0]
            edge_min_y = min(p1[1], p2[1])
            edge_max_y = max(p1[1], p2[1])

            if min_x < edge_x < max_x:
                if edge_min_y < max_y and edge_max_y > min_y:
                    return True

        else:
            edge_y = p1[1]
            edge_x_min = min(p1[0], p2[0])
            edge_x_max = max(p1[0], p2[0])

            if min_y < edge_y < max_y:
                if edge_x_min < max_x and edge_x_max > min_x:
                    return True

        return False


if __name__ == "__main__":
    data = []
    with open("input") as file:
        contents = file.read()
        data = [list(map(int, line.split(","))) for line in contents.strip().split("\n")]
    print(Solution().find_biggest_area(data))
    print(Solution().find_biggest_area_in_region(data))
