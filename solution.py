from abc import ABC, abstractmethod
import copy

class Solution(ABC):
    def __init__(self):
        self.representation = None
        self.cost = None

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def generate_neighbor(self, major_perturbation=False):
        pass

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Cost: {self.cost} | Representation: {self.representation}"