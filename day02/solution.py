class Solution():
    def sum_of_invalid_id(self, sequence):
        sum = 0
        for range_str in sequence:
            start, stop = range_str.split("-")
            for i in range(int(start), int(stop)+1):
                p_id = str(i)
                size = len(p_id)
                if size % 2 != 0:
                    continue
                partition_size = int(size/2)
                if p_id[:partition_size] == p_id[partition_size:]:
                    sum += i
        return sum

    def sum_invalid_ids_in_all_patterns(self, sequence):
        total = 0
        for range_str in sequence:
            start, stop = range_str.split("-")
            for i in range(int(start), int(stop)+1):
                if self._is_repeated(i):
                    total += i
        return total

    def _is_repeated(self, n: int) -> bool:
        s = str(n)
        if len(s) < 2:
            return False
        ss = s + s
        return s in ss[1:-1]


if __name__ == "__main__":
    with open('input', 'r') as file:
        id_ranges = file.read().split(',')
    print(Solution().sum_invalid_ids_from_ranges(id_ranges))
