import math
import random
from collections import deque


def hill_climbing(initial_solution, max_iterations):
    current_solution = initial_solution.clone()
    best_solution = current_solution.clone()

    for _ in range(max_iterations):
        neighbor = current_solution.generate_neighbor()

        if neighbor.cost < current_solution.cost:
            current_solution = neighbor

            if current_solution.cost < best_solution.cost:
                best_solution = current_solution.clone()

    return best_solution


def tabu_search(initial_solution, max_iterations, tabu_tenure, neighborhood_size=20):
    current_solution = initial_solution.clone()
    best_solution = current_solution.clone()
    tabu_list = deque(maxlen=tabu_tenure)
    tabu_list.append(tuple(current_solution.representation))

    for _ in range(max_iterations):
        best_neighbor = None

        for _ in range(neighborhood_size):
            neighbor = current_solution.generate_neighbor()
            if tuple(neighbor.representation) not in tabu_list:
                if best_neighbor is None or neighbor.cost < best_neighbor.cost:
                    best_neighbor = neighbor

        if best_neighbor is None:
            best_neighbor = current_solution.generate_neighbor()

        current_solution = best_neighbor
        tabu_list.append(tuple(current_solution.representation))

        if current_solution.cost < best_solution.cost:
            best_solution = current_solution.clone()

    return best_solution


def simulated_annealing(initial_solution, initial_temp, cooling_rate, min_temp):
    current_solution = initial_solution.clone()
    best_solution = current_solution.clone()
    current_temp = initial_temp

    while current_temp > min_temp:
        neighbor = current_solution.generate_neighbor()
        delta_e = neighbor.cost - current_solution.cost

        if delta_e < 0:
            current_solution = neighbor
            if current_solution.cost < best_solution.cost:
                best_solution = current_solution.clone()
        else:
            probability = math.exp(-delta_e / current_temp)
            if random.random() < probability:
                current_solution = neighbor

        current_temp *= cooling_rate

    return best_solution


def iterated_local_search(initial_solution, max_iterations, local_search_iterations):
    current_solution = hill_climbing(initial_solution, local_search_iterations)
    best_solution = current_solution.clone()

    for _ in range(max_iterations):
        perturbed_solution = current_solution.generate_neighbor(major_perturbation=True)
        local_optimum = hill_climbing(perturbed_solution, local_search_iterations)

        if local_optimum.cost < best_solution.cost:
            best_solution = local_optimum.clone()
            current_solution = local_optimum.clone()

    return best_solution