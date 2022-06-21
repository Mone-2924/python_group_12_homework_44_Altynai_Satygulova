secret_nums = [5, 1, 2, 9]
class Check():
    def __init__(self, num_str):
        self.num_str = num_str

    def check_len(self):
        if len(self.num_str) == 4:
            return True
        else:
            return False

    def checking_for_numbers(self):
        for i in self.num_str:
            if int(i) > 9 or int(i) < 1: 
                return False
        return True

    def checking_for_str(self):
        for i in range(len(self.num_str)):
            if self.num_str[i].isdigit():
                continue
            else:
                return False

    def digit_matching_check(self):
        unique = []
        for i in self.num_str:
            if int(i) in unique:
                return False
            else:
                unique.append(int(i))
        return True

class Game:
    def play(num_str, secret_nums):
        num_str = list(num_str)
        cow_numbers = 0
        bull_numbers = 0
        try:
            for i in range(len(num_str)):
                if secret_nums[i] == int(num_str[i]):
                    bull_numbers += 1
                elif int(num_str[i]) in secret_nums:
                    cow_numbers += 1
            return cow_numbers, bull_numbers

        except:
            return cow_numbers, bull_numbers
