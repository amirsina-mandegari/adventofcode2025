class Solution:
    def count_beam_splitting_and_count_timelines(self, data):
        points = set()
        start = data[0].index("S")
        timeline = [0] * len(data[0])
        timeline[start] = 1
        points.add(start)
        splits = 0
        for line in data[1:]:
            new_points = set()
            for point in points:
                if line[point] == ".":
                    new_points.add(point)
                    continue
                if line[point] == "^":
                    splits += 1
                    if point != 0:
                        new_points.add(point - 1)
                        timeline[point - 1] += timeline[point]
                    if point != len(line) - 1:
                        new_points.add(point + 1)
                        timeline[point + 1] += timeline[point]
                    timeline[point] = 0
            points = new_points
        return splits, sum(timeline)


if __name__ == "__main__":
    with open("input") as file:
        data = file.read().splitlines()
    print(Solution().count_beam_splitting_and_count_timelines(data))
