import time 

class ScoreManager:
    def __init__(self, solution_str):
        self.solution = [int(c) for c in solution_str]
        self.score = 0
        self.start_time = time.time()
    
    def check_move(self, index, value):
        if value == self.solution[index]:
            self.score += 100
            return True
        else:
            self.score -= 25
            return False
        
    def elapsed_time(self):
        return int(time.time() - self.start_time)