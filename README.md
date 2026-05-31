# metaheuristic-benchmark

![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-Metaheuristics-informational?style=flat-square)
![Problems](https://img.shields.io/badge/Problems-Knapsack%20%7C%20N--Queens-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

An empirical benchmark comparing four local search metaheuristics — **Hill Climbing**, **Tabu Search**, **Simulated Annealing**, and **Iterated Local Search** — on two classic NP-hard combinatorial problems. Each algorithm runs 20 independent trials per problem; results are reported as min / avg / max cost.

---

## Algorithms

| Algorithm | Key Idea |
|---|---|
| **Hill Climbing (HC)** | Greedy local search — always moves to a strictly better neighbor |
| **Tabu Search (TS)** | Maintains a fixed-size tabu list to escape local optima by forbidding recently visited states |
| **Simulated Annealing (SA)** | Accepts worse neighbors with a probability that decreases as temperature cools (Metropolis criterion) |
| **Iterated Local Search (ILS)** | Alternates between local search and random perturbation to escape local optima basins |

---

## Problems

### 0/1 Knapsack
Select items (binary vector) to **maximise total value** without exceeding weight capacity. Constraint violations are penalised heavily to guide the search back into the feasible region.

- 10 items, capacity 120
- Neighbor: toggle 1–2 bits (or up to `N/4` bits for ILS perturbation)

### N-Queens
Place N queens on an N×N board so that **no two queens attack each other**. Cost is the number of conflicts (row + diagonal).

- N = 8
- Neighbor: swap two column positions (or up to `N/4` swaps for ILS perturbation)

---

## Architecture

The project follows the **Template Method** pattern — a single abstract `Solution` interface decouples algorithms from problems:

```
Solution (ABC)
├── initialize()         # randomise starting point
├── evaluate()           # compute objective cost
├── generate_neighbor()  # produce a candidate move
└── clone()              # deep copy for state management

Knapsack(Solution)   NQueens(Solution)
```

Algorithms accept any `Solution` subclass, making it straightforward to plug in new problems or new algorithms.

```
algorithms.py   ←── operates on Solution interface
problems.py     ←── Knapsack, NQueens implementations
solution.py     ←── abstract base class
main.py         ←── runs benchmark and prints statistics
```

---

## Getting Started

**Requirements:** Python 3.14+, [uv](https://docs.astral.sh/uv/) (or plain pip)

```bash
# clone and run
git clone https://github.com/<your-username>/metaheuristic-benchmark.git
cd metaheuristic-benchmark
python main.py
```

### Sample output

```
--- Testare Empirica Problema Rucsacului (20 rulari) ---
Hill Climbing          | Min:   -435 | Avg:   -412.50 | Max:   -380
Tabu Search            | Min:   -435 | Avg:   -430.75 | Max:   -420
Simulated Annealing    | Min:   -435 | Avg:   -428.00 | Max:   -415
Iterated Local Search  | Min:   -435 | Avg:   -433.20 | Max:   -425

--- Testare Empirica Problema N-Regine N=8 (20 rulari) ---
Hill Climbing          | Min:      0 | Avg:     2.10 | Max:      5
Tabu Search            | Min:      0 | Avg:     0.40 | Max:      2
Simulated Annealing    | Min:      0 | Avg:     0.20 | Max:      1
Iterated Local Search  | Min:      0 | Avg:     0.05 | Max:      1
```

*(Costs for Knapsack are negative because the framework minimises; lower is better for both problems.)*

---

## Extending

Add a new problem by subclassing `Solution` and implementing four methods:

```python
class MyProblem(Solution):
    def initialize(self):   ...
    def evaluate(self):     ...
    def generate_neighbor(self, major_perturbation=False): ...
    def clone(self):        ...
```

Pass an instance to any algorithm function — no other changes required.
