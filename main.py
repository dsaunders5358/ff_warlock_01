import random


class Adventurer():
    def __init__(self):
        self.skill, self.stamina, self.luck = self.__generate_stats()
        
    def __generate_stats(self):
        skill = random.randint(1, 6) + 6
        stamina = random.randint(2, 12) + 12
        luck = random.randint(1, 6) + 6
        return skill, stamina, luck


class Mechanics():
    def __init__(self):
        pass
    
    def roll_dice(self, num):
        total_rolled = 0
        for i in range(num):
            total_rolled += random.randint(1, 6)
        return total_rolled

class Luck(Mechanics):
    def __init__(self, luck):
        super().__init__()
        self.luck = luck
        self.passed_check = self.check_luck()
    
    def check_luck(self):
        luck_result = self.roll_dice(2)
        print(luck_result)
        if luck_result >= self.luck:
            return True
        return False
        

def main():
    test = Luck(12)

main()