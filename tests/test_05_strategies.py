"""Занятие 5. Стратегии решения задач.

Задачи 1-5 - обязательные, они встроены в конспект (docs/05-strategies/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import pytest


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (1, 1), (2, 1), (3, 2), (5, 5), (10, 55), (20, 6765)],
)
def test_01_fib(solution, n, expected):
    f = solution("fib", "fib")
    assert f(n) == expected


@pytest.mark.parametrize(
    "items, capacity, expected",
    [
        ([(2, 10), (3, 15), (5, 30)], 5, 30),
        ([(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)], 10, 55),
        ([(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)], 7, 60),
        ([], 5, 0),
    ],
)
def test_02_knapsack_bruteforce(solution, items, capacity, expected):
    f = solution("knapsack_bruteforce", "knapsack_bruteforce")
    assert f(items, capacity) == expected


@pytest.mark.parametrize(
    "items, capacity, expected",
    [
        ([(2, 10), (3, 15), (5, 30)], 5, 30),
        ([(6, 10), (5, 9), (5, 8)], 10, 10),   # жадный ошибается, оптимум 17
        ([(1, 5), (2, 6), (3, 10), (4, 15)], 7, 25),
        ([], 5, 0),
    ],
)
def test_03_greedy_knapsack(solution, items, capacity, expected):
    f = solution("greedy_knapsack", "greedy_knapsack")
    assert f(items, capacity) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (8, 92)],
)
def test_04_n_queens(solution, n, expected):
    f = solution("n_queens", "n_queens")
    assert f(n) == expected


@pytest.mark.parametrize(
    "items, capacity, expected",
    [
        ([(2, 10), (3, 15), (5, 30)], 5, 30),
        ([(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)], 7, 60),
        ([(6, 10), (5, 9), (5, 8)], 10, 17),   # оптимум, где жадный дал 10
        ([], 5, 0),
    ],
)
def test_05_knapsack_dp(solution, items, capacity, expected):
    f = solution("knapsack_dp", "knapsack_dp")
    assert f(items, capacity) == expected


def test_05_knapsack_dp_large(solution):
    """200 предметов: перебор за O(2^n) не уложится, только ДП."""
    f = solution("knapsack_dp", "knapsack_dp")
    items = [((i % 100) + 1, (i * 7) % 500 + 1) for i in range(200)]
    assert f(items, 5000) == 38103


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([100, 120, 140, 160, 180, 200, 220], 120),
        ([200, 180, 220, 160, 240, 260, 210], 100),
    ],
)
def test_06_best_deal(solution, prices, expected):
    f = solution("best_deal", "best_deal")
    assert f(prices) == expected


def test_10_power_set(solution):
    f = solution("power_set", "power_set")
    result = {frozenset(s) for s in f([1, 2, 3])}
    expected = {
        frozenset(), frozenset({1}), frozenset({2}), frozenset({3}),
        frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}), frozenset({1, 2, 3}),
    }
    assert result == expected
    assert len(f([1, 2, 3])) == 8


def test_10_power_set_edge(solution):
    f = solution("power_set", "power_set")
    assert [tuple(s) for s in f([])] == [()]


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 11, 3),
        ([1, 3, 4], 6, 2),
        ([2], 3, -1),
        ([1], 0, 0),
        ([2, 5], 8, 4),
        ([1, 5, 10, 25], 63, 6),
    ],
)
def test_12_coin_change(solution, coins, amount, expected):
    f = solution("coin_change", "coin_change")
    assert f(coins, amount) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([5, 4, 3, 2, 1], 1),
        ([], 0),
        ([1], 1),
    ],
)
def test_14_lis(solution, nums, expected):
    f = solution("lis", "longest_increasing_subsequence")
    assert f(nums) == expected


def test_15_grid_paths(solution):
    f = solution("grid_paths", "grid_paths")
    assert f(3, 3) == 6
    assert f(2, 7) == 7
    assert f(1, 1) == 1


def test_15_grid_paths_large(solution):
    """Рекурсия по двум направлениям здесь не уложится - нужна таблица ДП."""
    f = solution("grid_paths", "grid_paths")
    assert f(30, 30) == 30067266499541040
    assert f(100, 100) == 22750883079422934966181954039568885395604168260154104734000


@pytest.mark.parametrize(
    "a0, expected",
    [
        (5, 15),
        (8, 384),
        (0, 1),
        (1, 1),
        (2, 2),
        (7, 105),
        (10, 3840),
    ],
)
def test_07_double_factorial(solution, a0, expected):
    f = solution("double_factorial", "double_factorial")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (16, 7),
        (942, 6),
        (132189, 6),
        (493193, 2),
        (0, 0),
        (9, 9),
        (10, 1),
        (99999999999, 9),
    ],
)
def test_08_digital_root(solution, a0, expected):
    f = solution("digital_root", "digital_root")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], True),
        (['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'], False),
        (['w'], False),
        (['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], False),
        (['n', 'e', 'w', 's', 'n', 'e', 'w', 's', 'n', 's'], True),
        ([], False),
    ],
)
def test_09_is_valid_walk(solution, a0, expected):
    f = solution("walk", "is_valid_walk")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (5, 1),
        (10, 3),
        (15, 5),
        (0, 0),
        (3, 1),
        (4, 1),
        (20, 7),
    ],
)
def test_11_count_odd_pentafib(solution, a0, expected):
    f = solution("pentafib", "count_odd_pentafib")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ((45, 120), (3, 8)),
        ((10, 5), (2, 1)),
        ((7, 3), (7, 3)),
        ((1, 1), (1, 1)),
        ((100, 10), (10, 1)),
        ((13, 26), (1, 2)),
    ],
)
def test_13_reduce_fraction(solution, a0, expected):
    f = solution("fraction", "reduce_fraction")
    assert f(a0) == expected
