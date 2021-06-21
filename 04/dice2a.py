import numpy as np

class Dice:
    def __init__(self):
        np.random.seed(0)
        self.sum_ = 0

    def throw(self):
        self.sum_ += np.random.randint(1, 7)

    def get_sum(self):
        return self.sum_