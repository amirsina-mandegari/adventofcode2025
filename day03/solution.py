class Solution():
    def sum_of_highest_batteries(self, battery_banks):
        total = 0
        for bank in battery_banks:
            best = 0
            for i in range(len(bank) - 1):
                for j in range(i + 1, len(bank)):
                    value = int(bank[i]) * 10 + int(bank[j])
                    best = max(best, value)
            total += best
        return total

    def best12(self, bank):
        k = 12
        drop = len(bank) - k
        stack = []

        for digit in bank:
            while drop and stack and stack[-1] < digit:
                stack.pop()
                drop -= 1
            stack.append(digit)

        return int("".join(stack[:k]))

    def sum_of_highest_12_batteries(self, battery_banks):
        return sum(self.best12(bank) for bank in battery_banks)
    

if __name__ == "__main__":
    with open('input', 'r') as file:
        battery_banks = file.read().splitlines()
    print(Solution().sum_of_highest_batteries(battery_banks))
    print(Solution().sum_of_highest_12_batteries(battery_banks))

