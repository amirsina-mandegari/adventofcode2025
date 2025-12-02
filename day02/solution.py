class Solution():
    def sum_of_invalid_id(self, sequence):
        sum = 0
        for range_str in sequence:
            print(range_str)
            start, stop = range_str.split("-")
            for i in range(int(start), int(stop)+1):
                p_id = str(i)
                size = len(p_id)
                if size % 2 != 0:
                    continue
                partition_size = int(size/2)
                if p_id[:partition_size] == p_id[partition_size:]:
                    sum += i
            print(sum)
        return sum




if __name__ == "__main__":
    with open('input', 'r') as file:
        id_ranges = file.read().split(',')
    Solution().sum_of_invalid_id(id_ranges)
