class Solution():
    def count_stay_on_zero(self, sequence):
        current = 50
        see_zero = 0
        for step in sequence:
            direction, num = self._seperate_direction_and_step(step)
            num = self._mode_hundred(num)
            if direction == 'L':
                current = self._mode_hundred(current-num)
            else:
                current = self._mode_hundred(current+num)

            if current == 0:
                see_zero +=1
        print(f"saw zero: {see_zero}")
        return see_zero

    def count_pass_on_zero(self, sequence):
        current = 50
        pass_zero = 0
        for step in sequence:
            direction, num = self._seperate_direction_and_step(step)
            print(direction, num)
            print(current)
            moded_num = self._mode_hundred(num)
            if direction == 'L':
                need_to_see_zero = current
                if num>=need_to_see_zero:
                    pass_zero = pass_zero+1 if need_to_see_zero is not 0 else pass_zero
                    pass_zero += ((num-need_to_see_zero)//100)
                current = self._mode_hundred(current-moded_num)
            else:
                need_to_see_zero = 100-current
                if num>=need_to_see_zero:
                    pass_zero = pass_zero+1 if need_to_see_zero is not 0 else pass_zero
                    pass_zero += (num-need_to_see_zero)//100
                current = self._mode_hundred(current+moded_num)

        print(f"passed zero: {pass_zero}")
        return pass_zero
    
    def _seperate_direction_and_step(self, step):
        return step[0], int(step[1:])
    
    def _mode_hundred(self, num):
        return num % 100



with open('input', 'r') as file:
    directions = file.read().splitlines()
# Now `lines` is a Python list containing each line from the input
Solution().count_pass_on_zero(directions)
