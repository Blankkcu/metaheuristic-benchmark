from problems import Knapsack, NQueens
from algorithms import hill_climbing, tabu_search, simulated_annealing, iterated_local_search


def print_statistics(nume, rezultate):
    min_cost = min(rezultate)
    max_cost = max(rezultate)
    avg_cost = sum(rezultate) / len(rezultate)
    print(f"{nume:<22} | Min: {min_cost:>6} | Avg: {avg_cost:>8.2f} | Max: {max_cost:>6}")


def test_knapsack():
    greutati = [10, 20, 30, 15, 25, 5, 40, 35, 18, 22]
    valori = [60, 100, 120, 75, 90, 40, 150, 130, 80, 110]
    capacitate = 120
    numar_rulari = 20

    print(f"--- Testare Empirica Problema Rucsacului ({numar_rulari} rulari) ---")

    rez_hc, rez_ts, rez_sa, rez_ils = [], [], [], []

    for _ in range(numar_rulari):
        problema = Knapsack(greutati, valori, capacitate)

        rez_hc.append(hill_climbing(problema, 1000).cost)
        rez_ts.append(tabu_search(problema, 1000, tabu_tenure=15, neighborhood_size=20).cost)
        rez_sa.append(simulated_annealing(problema, initial_temp=1000.0, cooling_rate=0.95, min_temp=0.1).cost)
        rez_ils.append(iterated_local_search(problema, max_iterations=50, local_search_iterations=100).cost)

    print_statistics("Hill Climbing", rez_hc)
    print_statistics("Tabu Search", rez_ts)
    print_statistics("Simulated Annealing", rez_sa)
    print_statistics("Iterated Local Search", rez_ils)
    print("\n")


def test_queens():
    n = 8
    numar_rulari = 20

    print(f"--- Testare Empirica Problema N-Regine N=8 ({numar_rulari} rulari) ---")

    rez_hc, rez_ts, rez_sa, rez_ils = [], [], [], []

    for _ in range(numar_rulari):
        problema = NQueens(n)

        rez_hc.append(hill_climbing(problema, 1000).cost)
        rez_ts.append(tabu_search(problema, 1000, tabu_tenure=10, neighborhood_size=20).cost)
        rez_sa.append(simulated_annealing(problema, initial_temp=100.0, cooling_rate=0.99, min_temp=0.1).cost)
        rez_ils.append(iterated_local_search(problema, max_iterations=50, local_search_iterations=100).cost)

    print_statistics("Hill Climbing", rez_hc)
    print_statistics("Tabu Search", rez_ts)
    print_statistics("Simulated Annealing", rez_sa)
    print_statistics("Iterated Local Search", rez_ils)
    print("\n")


if __name__ == "__main__":
    test_knapsack()
    test_queens()