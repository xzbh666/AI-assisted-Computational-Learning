"""Dependency-free, deterministic newsvendor learning example.

Run: python skills/code-to-understanding/scripts/newsvendor_demo.py
The numbers are synthetic teaching inputs, NOT user/course dataset results.
"""
from __future__ import annotations

from typing import Dict

DEMAND_PROB: Dict[int, float] = {10: 0.2, 20: 0.5, 30: 0.3}
PRICE = 10.0
COST = 4.0
SALVAGE = 1.0


def payoff(order: int, demand: int) -> float:
    sold = min(order, demand)
    leftover = max(order - demand, 0)
    return PRICE * sold + SALVAGE * leftover - COST * order


def expected_profit(order: int) -> float:
    return sum(prob * payoff(order, demand) for demand, prob in DEMAND_PROB.items())


def critical_fractile() -> float:
    underage = PRICE - COST
    overage = COST - SALVAGE
    return underage / (underage + overage)


def optimal_order() -> int:
    target = critical_fractile()
    cumulative = 0.0
    for demand, probability in sorted(DEMAND_PROB.items()):
        cumulative += probability
        if cumulative >= target:
            return demand
    raise ValueError("Probabilities must sum to one")


if __name__ == "__main__":
    assert abs(sum(DEMAND_PROB.values()) - 1.0) < 1e-12
    print(f"Critical fractile: {critical_fractile():.6f}")
    for q in sorted(DEMAND_PROB):
        print(f"Q={q}, expected profit={expected_profit(q):.2f}")
    print(f"Optimal Q={optimal_order()}")
