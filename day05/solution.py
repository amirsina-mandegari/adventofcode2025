class Solution:
    def find_fresh_products(self, ids, ranges):
        fresh_count = 0
        for i in ids:
            int_id = int(i)
            seen = False
            for r in ranges:
                start, end = r.split("-")
                if int(start) <= int_id <= int(end):
                    seen = True
                    break
            if seen:
                fresh_count += 1
        return fresh_count

    def count_all_fresh_ids(self, ranges):
        ranges_in_int = []
        for r in ranges:
            s, e = r.split("-")
            ranges_in_int.append((int(s), int(e)))
        sorted_ranges = sorted(ranges_in_int, key=lambda x: x[0])
        merged_ranges = []
        for r in sorted_ranges:
            if not merged_ranges or merged_ranges[-1][1] < r[0]:
                merged_ranges.append(r)
            last_data = merged_ranges.pop()
            merged_ranges.append((last_data[0], max(last_data[1], r[1])))

        count = 0
        for start, end in merged_ranges:
            count += end - start + 1

        return count


if __name__ == "__main__":
    with open("input") as file:
        content = file.read().strip()

        sections = content.split("\n\n")

        ranges = sections[0].split("\n")
        ids = sections[1].split("\n")
    print(Solution().find_fresh_products(ids, ranges))
    print(Solution().count_all_fresh_ids(ranges))
