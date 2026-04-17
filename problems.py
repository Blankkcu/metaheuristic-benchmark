from solution import Solution
import random

class Knapsack(Solution):
    def __init__(self, weights, values, max_capacity):
        super().__init__()
        self.weights = weights
        self.values = values
        self.max_capacity = max_capacity
        self.n = len(weights)
        self.initialize()

    def initialize(self):
        self.representation = [random.choice([0, 1]) for _ in range(self.n)]
        self.evaluate()

    def evaluate(self):
        total_weight = sum(self.representation[i] * self.weights[i] for i in range(self.n))
        total_value = sum(self.representation[i] * self.values[i] for i in range(self.n))

        if total_weight > self.max_capacity:
            penalty = (total_weight - self.max_capacity) * 1000
            self.cost = -(total_value - penalty)
        else:
            self.cost = -total_value

    def generate_neighbor(self, major_perturbation=False):
        neighbor = self.clone()
        num_changes = max(2, self.n // 4) if major_perturbation else 1

        indices = random.sample(range(self.n), num_changes)
        for index in indices:
            neighbor.representation[index] = 1 - neighbor.representation[index]

        neighbor.evaluate()
        return neighbor


class NQueens(Solution):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.initialize()

    def initialize(self):
        self.representation = list(range(self.n))
        random.shuffle(self.representation)
        self.evaluate()

    def evaluate(self):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.representation[i] == self.representation[j] or \
                        abs(self.representation[i] - self.representation[j]) == abs(i - j):
                    conflicts += 1
        self.cost = conflicts

    def generate_neighbor(self, major_perturbation=False):
        neighbor = self.clone()
        num_swaps = max(2, self.n // 4) if major_perturbation else 1

        for _ in range(num_swaps):
            i, j = random.sample(range(self.n), 2)
            neighbor.representation[i], neighbor.representation[j] = neighbor.representation[j], \
            neighbor.representation[i]

        neighbor.evaluate()
        return neighbor