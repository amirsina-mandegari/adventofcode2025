class Solution:
    def get_paper_roles_less_than_four_adjacent(self, placements):
        count = 0
        col_num = len(placements)
        row_num = len(placements[0])
        for i, row in enumerate(placements):
            for j, obj in enumerate(row):
                if obj == ".":
                    continue
                paper = 0
                locations = self._create_adjacent_map(i, j, col_num, row_num)
                for location in locations:
                    if placements[location[0]][location[1]] == "@":
                        paper += 1
                if paper < 4:
                    count += 1
        return count

    def get_paper_roles_less_than_four_adjacent_amsp(self, placements):
        count = 0
        col_num = len(placements)
        row_num = len(placements[0])
        removed = True
        while removed:
            removed = False
            for i, row in enumerate(placements):
                for j, obj in enumerate(row):
                    if obj == ".":
                        continue
                    paper = 0
                    locations = self._create_adjacent_map(i, j, col_num, row_num)
                    for location in locations:
                        if placements[location[0]][location[1]] == "@":
                            paper += 1
                    if paper < 4:
                        placements[i][j] = "."
                        removed = True
                        count += 1
        return count

    def _create_adjacent_map(self, i, j, col_num, row_num):
        mapping = []
        for c in range(max(i - 1, 0), min(i + 2, col_num)):
            for r in range(max(j - 1, 0), min(j + 2, row_num)):
                if (c, r) == (i, j):
                    continue
                mapping.append((c, r))
        return mapping


if __name__ == "__main__":
    with open("input") as file:
        data = file.read().splitlines()
    placements = [list(i) for i in data]
    print(Solution().get_paper_roles_less_than_four_adjacent(placements))
    print(Solution().get_paper_roles_less_than_four_adjacent_amsp(placements))
