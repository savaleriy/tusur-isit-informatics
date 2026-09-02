"""Занятие 2. Логика и комбинаторика.

Задачи 1-5 - обязательные, они встроены в конспект (docs/02-logic/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import pytest


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "wire, w, expected",
    [
        (100, 25, 1250 / 3),
        (100, 10, 800 / 3),
        (100, 50, 0.0),
        (60, 15, 150.0),
        (12, 3, 6.0),
    ],
)
def test_01_pasture_area(solution, wire, w, expected):
    f = solution("pasture", "pasture_area")
    assert f(wire, w) == pytest.approx(expected)


@pytest.mark.parametrize(
    "wire, w, l, area",
    [
        (100, 25.0, 100 / 6, 10000 / 24),
        (60, 15.0, 10.0, 150.0),
        (12, 3.0, 2.0, 6.0),
    ],
)
def test_01_best_pasture(solution, wire, w, l, area):
    f = solution("pasture", "best_pasture")
    got_w, got_l, got_area = f(wire)
    assert got_w == pytest.approx(w, rel=1e-3)
    assert got_l == pytest.approx(l, rel=1e-3)
    assert got_area == pytest.approx(area, rel=1e-3)


def test_01_best_pasture_uses_all_wire(solution):
    """В оптимуме проволока израсходована полностью: 2w + 3l = wire."""
    f = solution("pasture", "best_pasture")
    for wire in (100, 60, 12, 37):
        w, l, _ = f(wire)
        assert 2 * w + 3 * l == pytest.approx(wire, rel=1e-3)


def test_02_truth_table_sizes(solution):
    f = solution("truth_table", "truth_table")
    for n in range(6):
        rows = list(f(n))
        assert len(rows) == 2 ** n, f"для {n} переменных должно быть 2^{n} строк"
        assert len(set(map(tuple, rows))) == len(rows), "строки не должны повторяться"


def test_02_truth_table_values(solution):
    f = solution("truth_table", "truth_table")
    assert [tuple(r) for r in f(0)] == [()]
    assert [tuple(r) for r in f(1)] == [(0,), (1,)]
    assert [tuple(r) for r in f(2)] == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert [tuple(r) for r in f(3)] == [
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
    ]


def test_03_are_equivalent_de_morgan(solution):
    f = solution("equivalence", "are_equivalent")

    assert f(lambda a, b: not (a and b), lambda a, b: (not a) or (not b), 2) is True
    assert f(lambda a, b: not (a or b), lambda a, b: (not a) and (not b), 2) is True
    assert f(lambda a, b: (not a) or b, lambda a, b: not (a and not b), 2) is True


def test_03_are_equivalent_detects_difference(solution):
    f = solution("equivalence", "are_equivalent")

    assert f(lambda a, b: not (a and b), lambda a, b: (not a) and (not b), 2) is False
    assert f(lambda a: a, lambda a: not a, 1) is False
    # различие только в одной строке из восьми: перебор обязан его найти
    assert f(
        lambda a, b, c: a and b and c,
        lambda a, b, c: a and b,
        3,
    ) is False


def test_03_are_equivalent_contraposition(solution):
    """A -> B тождественно not B -> not A."""
    f = solution("equivalence", "are_equivalent")

    def implies(a, b):
        return (not a) or b

    assert f(implies, lambda a, b: implies(not b, not a), 2) is True


def test_03_are_equivalent_distributivity(solution):
    """Работает при любом числе переменных, не только при двух."""
    f = solution("equivalence", "are_equivalent")

    assert f(
        lambda a, b, c: a and (b or c),
        lambda a, b, c: (a and b) or (a and c),
        3,
    ) is True
    assert f(
        lambda a, b, c: a or (b and c),
        lambda a, b, c: (a or b) and (a or c),
        3,
    ) is True


@pytest.mark.parametrize(
    "n, expected",
    [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800), (20, 2432902008176640000)],
)
def test_04_factorial(solution, n, expected):
    f = solution("counting", "factorial")
    assert f(n) == expected


def test_04_factorial_negative(solution):
    f = solution("counting", "factorial")
    assert f(-1) is None
    assert f(-10) is None


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (13, 6, 1235520),
        (4, 2, 12),
        (5, 5, 120),
        (5, 0, 1),
        (3, 5, 0),
        (-1, 2, 0),
        (5, -1, 0),
    ],
)
def test_04_arrangements(solution, n, k, expected):
    f = solution("counting", "arrangements")
    assert f(n, k) == expected


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (13, 6, 1716),
        (4, 2, 6),
        (64, 8, 4426165368),
        (5, 0, 1),
        (5, 5, 1),
        (30, 2, 435),
        (3, 5, 0),
        (-1, 2, 0),
    ],
)
def test_04_combinations(solution, n, k, expected):
    f = solution("counting", "combinations")
    assert f(n, k) == expected


def test_04_relation_between_formulas(solution):
    """A(n,k) = C(n,k) * k! - связь размещений и сочетаний."""
    arrangements = solution("counting", "arrangements")
    combinations = solution("counting", "combinations")
    factorial = solution("counting", "factorial")
    for n in range(8):
        for k in range(n + 1):
            assert arrangements(n, k) == combinations(n, k) * factorial(k)


@pytest.mark.parametrize(
    "people, expected",
    [
        (0, 0.0),
        (1, 0.0),
        (2, 0.0027397260273972575),
        (10, 0.11694817771107768),
        (23, 0.5072972343239854),
        (50, 0.9703735795779884),
        (366, 1.0),
        (400, 1.0),
    ],
)
def test_05_birthday_probability(solution, people, expected):
    f = solution("birthday", "birthday_probability")
    assert f(people) == pytest.approx(expected, abs=1e-9)


def test_05_birthday_crosses_half_at_23(solution):
    f = solution("birthday", "birthday_probability")
    assert f(22) < 0.5 < f(23), "порог должен проходить между 22 и 23 людьми"


def test_05_simulate_birthday(solution):
    f = solution("birthday", "simulate_birthday")
    assert f(1, 500) == pytest.approx(0.0)
    assert f(400, 50) == pytest.approx(1.0)
    # статистика: на 20000 экспериментов отклонение почти наверняка мало
    assert f(23, 20000) == pytest.approx(0.507, abs=0.05)
    assert f(50, 20000) == pytest.approx(0.970, abs=0.03)


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text, code",
    [
        ("PYTHON 3", ".--. -.-- - .... --- -. / ...--"),
        ("SOS", "... --- ..."),
        ("A", ".-"),
        ("AB C", ".- -... / -.-."),
        ("2025", "..--- ----- ..--- ....."),
    ],
)
def test_06_to_morse(solution, text, code):
    f = solution("morse_code", "to_morse")
    assert f(text) == code


@pytest.mark.parametrize(
    "text, code",
    [
        ("PYTHON 3", ".--. -.-- - .... --- -. / ...--"),
        ("SOS", "... --- ..."),
        ("A", ".-"),
        ("AB C", ".- -... / -.-."),
        ("2025", "..--- ----- ..--- ....."),
    ],
)
def test_06_from_morse(solution, text, code):
    f = solution("morse_code", "from_morse")
    assert f(code) == text


def test_06_morse_roundtrip(solution):
    to_morse = solution("morse_code", "to_morse")
    from_morse = solution("morse_code", "from_morse")
    for text in ["HELLO WORLD", "TUSUR 2025", "X", "AAA BBB CCC"]:
        assert from_morse(to_morse(text)) == text


@pytest.mark.parametrize(
    "x, n, expected",
    [
        (2, 0, 1), (2, 1, 2), (2, 2, 4), (2, 3, 16), (2, 4, 65536),
        (3, 0, 1), (3, 1, 3), (3, 2, 27),
        (5, 2, 3125),
        (1, 5, 1),
        (7, 1, 7),
    ],
)
def test_10_tetration(solution, x, n, expected):
    f = solution("tetration", "tetration")
    assert f(x, n) == expected


def test_10_tetration_is_right_associative(solution):
    """Башня считается сверху вниз: 2^(2^(2^2)) = 65536, а не ((2^2)^2)^2 = 256."""
    f = solution("tetration", "tetration")
    assert f(2, 4) == 65536, "похоже, степень вычисляется снизу вверх"
    assert f(3, 3) == 3 ** 27


def test_12_read_sharks(solution, data_dir):
    f = solution("sharks", "read_sharks")
    sharks = f(str(data_dir("02-logic") / "shark-species.txt"))

    assert isinstance(sharks, dict)
    assert len(sharks) == 9, "в файле девять отрядов"
    assert sorted(sharks)[0] == "Carcharhiniformes"

    assert (
        sharks["Lamniformes"]["Lamnidae"]["Carcharodon"]["Carcharodon carcharias"]
        == "Great white shark"
    )
    assert (
        sharks["Lamniformes"]["Lamnidae"]["Isurus"]["Isurus oxyrinchus"]
        == "Shortfin mako"
    )
    assert (
        sharks["Lamniformes"]["Cetorhinidae"]["Cetorhinus"]["Cetorhinus maximus"]
        == "Basking shark"
    )


def test_12_sharks_structure(solution, data_dir):
    """Ровно четыре уровня: отряд, семейство, род, вид с общим названием."""
    f = solution("sharks", "read_sharks")
    sharks = f(str(data_dir("02-logic") / "shark-species.txt"))

    species_count = 0
    for order in sharks.values():
        assert isinstance(order, dict)
        for family in order.values():
            assert isinstance(family, dict)
            for genus in family.values():
                assert isinstance(genus, dict)
                for name, common in genus.items():
                    assert isinstance(common, str), f"{name} должен быть листом-строкой"
                    species_count += 1
    assert species_count > 400, "видов в файле заметно больше четырёхсот"


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (10, 2, 8),
        (10, 3, 4),
        (10, 5, 2),
        (5, 2, 3),
        (10, 10, 2),
        (25, 6, 10),
        (100, 12, 48),
        (1000, 7, 164),
        (1, 2, 0),
        (100, 97, 1),
    ],
)
def test_14_max_power(solution, n, k, expected):
    f = solution("legendre", "max_power")
    assert f(n, k) == expected


def test_14_max_power_is_fast(solution):
    """Факториал вычислять нельзя: при n = 10^9 он не поместится в память."""
    f = solution("legendre", "max_power")
    assert f(10 ** 9, 2) == 999999987
    assert f(10 ** 9, 10) == 249999998


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (2, 2, 8),
        (4, 5, 236),
        (1, 1, 1),
        (3, 1, 17),
        (1, 10, 1),
    ],
)
def test_15_count_paths(solution, n, k, expected):
    f = solution("lattice_paths", "count_paths")
    assert f(n, k) == expected


def test_15_count_paths_is_fast(solution):
    """Двойной цикл по N^2 парам при N = 200000 не уложится в разумное время."""
    f = solution("lattice_paths", "count_paths")
    result = f(200000, 3)
    assert 0 <= result < 10 ** 9 + 7


@pytest.mark.parametrize(
    "a0, expected",
    [
        (12, True),
        (32, False),
        (13579, True),
        (2335, True),
        (7, True),
        (21, False),
        (1111, True),
    ],
)
def test_07_is_tidy(solution, a0, expected):
    f = solution("tidy", "is_tidy")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (1, True),
        (2, True),
        (145, True),
        (40585, True),
        (123, False),
        (10, False),
        (3, False),
    ],
)
def test_08_is_strong(solution, a0, expected):
    f = solution("strong", "is_strong")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (25, True),
        (76, True),
        (5, True),
        (6, True),
        (1, True),
        (13, False),
        (7, False),
        (625, True),
    ],
)
def test_09_is_automorphic(solution, a0, expected):
    f = solution("automorphic", "is_automorphic")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (7, 'Balanced'),
        (59, 'Balanced'),
        (295591, 'Not Balanced'),
        (1, 'Balanced'),
        (1230, 'Not Balanced'),
        (56239814, 'Balanced'),
        (424, 'Balanced'),
    ],
)
def test_11_is_balanced_number(solution, a0, expected):
    f = solution("balanced_number", "is_balanced_number")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([3, 1, 2], 1),
        ([2, 12, 8, 4, 6], 5),
        ([5, 2], 0),
        ([1, 1, 1], 0),
        ([1], 1),
        ([2, 2], 1),
        ([10, 10], 3),
    ],
)
def test_13_min_to_prime(solution, a0, expected):
    f = solution("next_prime_sum", "min_to_prime")
    assert f(a0) == expected
