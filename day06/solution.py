class Solution:
    def cephalopod_math(self, homework):
        operations = homework.pop()
        sum_of_answers = 0
        for i in range(len(homework[0])):
            opr = operations[i]
            nums = [row[i] for row in homework]
            equation = opr.join([str(x) for x in nums])
            sum_of_answers += eval(equation)
        return sum_of_answers

    def cephalopod_math_vertical(self, homework):
        operations = homework.pop()
        sum_of_answers = 0
        next_operation = 0
        ended = False
        while ended is False:
            numbers = []
            start = next_operation
            opr = operations[start]
            print(opr)
            end = len(operations)
            for i, obj in enumerate(operations[start + 1 :]):
                if obj in ["*", "+"]:
                    end = i + start + 1
                    next_operation = min(i + start + 1, len(operations))
                    break
            if end == len(operations):
                ended = True
            print(start, end)
            for i in range(start, end):
                num = "".join([str(row[i]) for row in homework]).split()
                if num:
                    numbers.append(num[0])
                print(num)
            equation = opr.join([x for x in numbers if x])
            print(equation)
            sum_of_answers += eval(equation)
            print("***************************")
        return sum_of_answers


if __name__ == "__main__":
    homework = []
    with open("input") as file:
        for line in file:
            homework.append(line.split())
    print(Solution().cephalopod_math(homework))
    homework = []
    with open("input") as file:
        for line in file:
            homework.append(line)
    print(Solution().cephalopod_math_vertical(homework))
