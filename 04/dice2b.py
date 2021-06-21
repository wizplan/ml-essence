import numpy as np

# 생성자의 인수에 시드를 설정해 재현성을 보장
class Dice:
    def __init__(self, random_seed=None):
        self.random_state_ = np.random.RandomState(random_seed)
        self.sum_ = 0

    def throw(self):
        self.sum_ += self.random_state_.randint(1, 7)

    def get_sum(self):
        return self.sum_