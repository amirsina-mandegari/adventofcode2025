class Solution():
    def open_the_lock(self, sequence):
        current = 50
        start = 0
        end = 99
        see_zero = 0
        for step in sequence:
            print(f"current:{current}")
            print(f"step:{step}")
            direction = step[0]
            num = self._clean_num(int(step[1:]))
            if direction == 'L':
                current = self._clean_num(current-num)
            else:
                current = self._clean_num(current+num)

            if current == 0:
                see_zero +=1
        return print(see_zero)

    def _clean_num(self,num):
        return num%100

with open('input', 'r') as file:
    directions = file.read().splitlines()
# Now `lines` is a Python list containing each line from the input
print(directions)
Solution().open_the_lock(directions)