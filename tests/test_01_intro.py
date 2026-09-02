"""Занятие 1. Информация и её представление.

Задачи 1-16 - обязательные, они встроены в конспект (docs/01-intro/note.md).
Задачи 17-26 - балльные (в task.md они пронумерованы 1-10).
"""

import pytest


# --------------------------------------------------------------------------
# Обязательные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "meters, expected",
    [(5, 500), (0, 0), (1, 100), (2.5, 250), (0.5, 50)],
)
def test_01_meters_to_centimeters(solution, meters, expected):
    f = solution("task_01", "meters_to_centimeters")
    assert f(meters) == pytest.approx(expected)


@pytest.mark.parametrize(
    "km, m, expected",
    [(1, 500, 500), (0.2, 900, 200), (1, 1000, 1000), (0, 5, 0), (3, 4000, 3000)],
)
def test_12_shortest_distance(solution, km, m, expected):
    f = solution("task_12", "shortest_distance")
    assert f(km, m) == pytest.approx(expected)


def test_13_multiplication_table(solution):
    f = solution("task_13", "multiplication_table")
    result = f(7)
    assert len(result) == 10, "в таблице должно быть ровно 10 строк"
    assert result[0] == "7 x 1 = 7"
    assert result[2] == "7 x 3 = 21"
    assert result[9] == "7 x 10 = 70"
    assert f(0)[4] == "0 x 5 = 0"


@pytest.mark.parametrize(
    "a, b, expected",
    [(3, 12, True), (5, 12, False), (1, 7, True), (7, 7, True), (0, 12, False), (7, 0, True)],
)
def test_03_is_divisor(solution, a, b, expected):
    f = solution("task_03", "is_divisor")
    assert bool(f(a, b)) == expected


@pytest.mark.parametrize("number", [42, 0, -7])
def test_06_echo_number(solution, number):
    f = solution("task_06", "echo_number")
    assert f(number) == f"Thats the number you entered {number}"


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (5, 3, "Number m > n"),
        (3, 5, "Number m < n"),
        (4, 4, "The numbers are equal"),
        (-1, -2, "Number m > n"),
    ],
)
def test_07_compare(solution, m, n, expected):
    f = solution("task_07", "compare")
    assert f(m, n) == expected


def test_14_circle_diameter(solution):
    f = solution("task_14", "circle_diameter")
    assert f(5) == pytest.approx(10)
    assert f(0) == pytest.approx(0)
    assert f(2.5) == pytest.approx(5)


@pytest.mark.parametrize(
    "start, end, expected",
    [(100, 500, 120300), (1, 10, 55), (500, 500, 500), (1, 1, 1), (0, 100, 5050)],
)
def test_14_sum_range(solution, start, end, expected):
    f = solution("task_14", "sum_range")
    assert f(start, end) == expected


@pytest.mark.parametrize("name", ["Валерий", "Ann", "X"])
def test_05_greet(solution, name):
    f = solution("task_05", "greet")
    assert f(name) == f"Hello, {name}"


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, 3),
        (10, 2, 3, 10),
        (1, 10, 3, 10),
        (1, 1, 1, 1),
        (-5, -2, -9, -2),
        (0, 0, -1, 0),
    ],
)
def test_09_max_of_three(solution, a, b, c, expected):
    f = solution("task_09", "max_of_three")
    assert f(a, b, c) == expected


@pytest.mark.parametrize("a, b", [(1, 2), (0, 0), (-3, 7)])
def test_04_swap(solution, a, b):
    f = solution("task_04", "swap")
    assert tuple(f(a, b)) == (b, a)


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, -3, -5, 2, 5], 2),
        ([1, 2, 3], 0),
        ([4, 1, 1, 9], 1),
        ([7], 0),
        ([], -1),
        ([3, 3, 3], 0),
    ],
)
def test_10_index_of_min(solution, values, expected):
    f = solution("task_10", "index_of_min")
    assert f(list(values)) == expected


def test_02_byte_conversion(solution):
    to_kb = solution("task_02", "bytes_to_kilobytes")
    to_b = solution("task_02", "kilobytes_to_bytes")
    assert to_kb(2048) == pytest.approx(2)
    assert to_kb(1024) == pytest.approx(1)
    assert to_kb(0) == pytest.approx(0)
    assert to_b(2) == pytest.approx(2048)
    assert to_b(0) == pytest.approx(0)
    assert to_kb(to_b(7)) == pytest.approx(7)


@pytest.mark.parametrize(
    "name, age, year, expected_year",
    [("Аня", 20, 2025, 2105), ("Боб", 0, 2025, 2125), ("Ким", 100, 2025, 2025)],
)
def test_08_century_message(solution, name, age, year, expected_year):
    f = solution("task_08", "century_message")
    message = f(name, age, year)
    assert name in message, "в сообщении должно быть имя"
    assert str(expected_year) in message, f"ожидался год {expected_year}"


def test_16_month_calendar_sunday_31(solution):
    f = solution("task_16", "month_calendar")
    expected = "\n".join(
        [
            "                   1",
            " 2  3  4  5  6  7  8",
            " 9 10 11 12 13 14 15",
            "16 17 18 19 20 21 22",
            "23 24 25 26 27 28 29",
            "30 31",
        ]
    )
    assert f(6, 31) == expected


def test_16_month_calendar_monday_28(solution):
    f = solution("task_16", "month_calendar")
    expected = "\n".join(
        [
            " 1  2  3  4  5  6  7",
            " 8  9 10 11 12 13 14",
            "15 16 17 18 19 20 21",
            "22 23 24 25 26 27 28",
        ]
    )
    assert f(0, 28) == expected


@pytest.mark.parametrize(
    "month, year, expected",
    [
        (1, 2001, 31),
        (2, 2001, 28),
        (2, 2000, 29),
        (2, 1900, 28),
        (2, 2024, 29),
        (4, 2025, 30),
        (11, 2025, 30),
        (12, 2025, 31),
    ],
)
def test_15_days_in_month(solution, month, year, expected):
    f = solution("task_15", "days_in_month")
    assert f(month, year) == expected


@pytest.mark.parametrize(
    "seats, expected",
    [
        ([1, 2, 3, 5, 4], [1, 2, 3, 5, 4]),
        ([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5], [10, 4, 9, 7, 11, 2, 8, 3, 6, 5, 1]),
        ([1], [1]),
        ([3, 1, 2], [2, 3, 1]),
    ],
)
def test_11_guests_by_seat(solution, seats, expected):
    f = solution("task_11", "guests_by_seat")
    assert list(f(list(seats))) == expected


def test_11_guests_by_seat_is_fast(solution):
    """Решение за O(n^2) на 20000 элементах не уложится в разумное время."""
    f = solution("task_11", "guests_by_seat")
    n = 20000
    seats = list(range(n, 0, -1))
    result = list(f(seats))
    assert result == list(range(n, 0, -1))


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "v1, v2, g, expected",
    [
        (720, 850, 70, [0, 32, 18]),
        (820, 81, 550, None),
        (80, 91, 37, [3, 21, 49]),
        (80, 100, 40, [2, 0, 0]),
        (720, 850, 37, [0, 17, 4]),
        (720, 850, 370, [2, 50, 46]),
        (120, 850, 37, [0, 3, 2]),
        (820, 850, 550, [18, 20, 0]),
        (82, 50, 55, None),
        (100, 100, 50, None),
    ],
)
def test_25_race(solution, v1, v2, g, expected):
    f = solution("tortoise_racing", "race")
    result = f(v1, v2, g)
    if expected is None:
        assert result is None
    else:
        assert list(result) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("most trees are blue", "Most Trees Are Blue"),
        (
            "How can mirrors be real if our eyes aren't real",
            "How Can Mirrors Be Real If Our Eyes Aren't Real",
        ),
        ("When I die. then you will realize", "When I Die. Then You Will Realize"),
        ("Dying is mainstream", "Dying Is Mainstream"),
        (
            "You Can Discover Everything You Need to Know About Everything by Looking at your Hands",
            "You Can Discover Everything You Need To Know About Everything By Looking At Your Hands",
        ),
        (
            "Three men, six options, don't choose.",
            "Three Men, Six Options, Don't Choose.",
        ),
    ],
)
def test_17_jaden_case(solution, text, expected):
    f = solution("jaden", "to_jaden_case")
    assert f(text) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (3212, 9414),
        (2112, 4114),
        (0, 0),
        (999, 818181),
        (10001, 10001),
        (9119, 811181),
        (3210987654, 9410816449362516),
    ],
)
def test_21_square_digits(solution, n, expected):
    f = solution("square_digits", "square_digits")
    assert f(n) == expected


@pytest.mark.parametrize(
    "limit, expected",
    [(13, 10), (34, 44), (100, 44), (200, 188), (10000, 3382), (4000000, 4613732), (1, 0)],
)
def test_23_even_fib_sum(solution, limit, expected):
    f = solution("even_fib_sum", "even_fib_sum")
    assert f(limit) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("zero", 0),
        ("one", 1),
        ("twenty", 20),
        ("forty-six", 46),
        ("two hundred forty-six", 246),
        ("nine hundred and nineteen", 919),
        ("seven hundred eighty-three thousand nine hundred and nineteen", 783919),
        ("one million", 1000000),
        ("fifteen", 15),
        ("one hundred", 100),
    ],
)
def test_26_words_to_number(solution, text, expected):
    f = solution("words_to_number", "words_to_number")
    assert f(text) == expected


@pytest.mark.parametrize(
    "a0, a1, expected",
    [
        (1, 0, 1),
        (1, 2, 3),
        (-1, 2, 2),
        (5, 5, 5),
        (-3, -1, -6),
        (0, 0, 0),
        (1, 100, 5050),
    ],
)
def test_18_sum_interval(solution, a0, a1, expected):
    f = solution("sum_interval", "sum_interval")
    assert f(a0, a1) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (1, True),
        (2, True),
        (1024, True),
        (4096, True),
        (333, False),
        (0, False),
        (3, False),
        (1099511627776, True),
    ],
)
def test_19_is_power_of_two(solution, a0, expected):
    f = solution("power_of_two", "is_power_of_two")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([13, 27, 49], (62, 27)),
        ([50, 60, 70, 80], (120, 140)),
        ([], (0, 0)),
        ([5], (5, 0)),
        ([1, 2], (1, 2)),
    ],
)
def test_20_team_weights(solution, a0, expected):
    f = solution("teams", "team_weights")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (89, True),
        (135, True),
        (175, True),
        (518, True),
        (1, True),
        (564, False),
        (89, True),
        (50, False),
    ],
)
def test_22_is_disarium(solution, a0, expected):
    f = solution("disarium", "is_disarium")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (39, 3),
        (999, 4),
        (25, 2),
        (4, 0),
        (0, 0),
        (10, 1),
        (277777788888899, 11),
    ],
)
def test_24_persistence(solution, a0, expected):
    f = solution("persistence", "persistence")
    assert f(a0) == expected
