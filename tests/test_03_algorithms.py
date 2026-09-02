"""Занятие 3. Алгоритмы и сложность.

Задачи 1-5 - обязательные, они встроены в конспект (docs/03-algorithms/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import random

import pytest


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([5, 3, 7, 1, 4], 1, 3),
        ([5, 3, 7, 1, 4], 6, -1),
        ([10, 20, 30, 40], 30, 2),
        ([1, 2, 2, 3], 2, 1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([], 1, -1),
    ],
)
def test_01_linear_search(solution, arr, target, expected):
    f = solution("linear_search", "linear_search")
    assert f(arr, target) == expected


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7], 8, -1),
        ([1, 2, 3, 4, 5, 6, 7], 0, -1),
        ([], 1, -1),
        ([1], 1, 0),
    ],
)
def test_02_binary_search(solution, arr, target, expected):
    f = solution("binary_search", "binary_search")
    assert f(arr, target) == expected


def test_02_binary_search_large(solution):
    """Бинарный поиск на миллионе элементов должен находить любой индекс."""
    f = solution("binary_search", "binary_search")
    arr = list(range(0, 10**6, 2))  # 500_000 чётных чисел
    assert f(arr, 999998) == 499999
    assert f(arr, 0) == 0
    assert f(arr, 999999) == -1  # нечётного в списке нет


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("heart", "earth", True),
        ("python", "typhon", True),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("aabb", "abab", True),
        ("aabb", "aabc", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "abc", False),
    ],
)
def test_03_is_anagram(solution, s1, s2, expected):
    f = solution("anagram", "is_anagram")
    assert f(s1, s2) is expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 2, 7, 1, 3, 5], [1, 2, 3, 4, 5, 7]),
        ([7, 3, 3, 4, 1], [1, 3, 3, 4, 7]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 5, 5], [5, 5, 5]),
    ],
)
def test_04_insertion_sort(solution, arr, expected):
    f = solution("insertion_sort", "insertion_sort")
    assert f(arr) == expected


def test_04_insertion_sort_does_not_mutate(solution):
    """Сортировка должна возвращать новый список, не меняя исходный."""
    f = solution("insertion_sort", "insertion_sort")
    arr = [4, 2, 7, 1, 3, 5]
    f(arr)
    assert arr == [4, 2, 7, 1, 3, 5]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 2, 7, 1, 3, 5], [1, 2, 3, 4, 5, 7]),
        ([7, 3, 3, 4, 1], [1, 3, 3, 4, 7]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 5, 5], [5, 5, 5]),
    ],
)
def test_05_quick_sort(solution, arr, expected):
    f = solution("quick_sort", "quick_sort")
    assert f(arr) == expected


def test_05_quick_sort_reverse_sorted(solution):
    """На отсортированном по убыванию списке опорный не должен быть крайним,
    иначе алгоритм вырождается в O(n^2) и падает по глубине рекурсии."""
    f = solution("quick_sort", "quick_sort")
    arr = list(range(2000, 0, -1))
    assert f(arr) == list(range(1, 2001))


def test_05_quick_sort_many_duplicates(solution):
    f = solution("quick_sort", "quick_sort")
    arr = [0, 1] * 500 + [0] * 1000
    assert f(arr) == sorted(arr)


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (15, 3),
        (16, 4),
        (100, 10),
        (101, 10),
        (10**12, 10**6),
    ],
)
def test_06_integer_square_root(solution, n, expected):
    f = solution("sqrt", "integer_square_root")
    assert f(n) == expected


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 9, (4, 5)),
        ([1, 2, 3, 4, 5], 10, None),
        ([1, 2, 3, 4, 5], 3, (1, 2)),
        ([1], 2, None),
        ([-3, -1, 0, 2, 4], 1, (-3, 4)),
        ([-3, -1, 0, 2, 4], 6, (2, 4)),
        ([-3, -1, 0, 2, 4], 100, None),
    ],
)
def test_10_two_sum_sorted(solution, arr, target, expected):
    f = solution("two_sum", "two_sum_sorted")
    assert f(arr, target) == expected


def test_10_two_sum_sorted_large(solution):
    """Наивный перебор пар здесь не уложится: список большой, нужны два указателя."""
    f = solution("two_sum", "two_sum_sorted")
    arr = list(range(200_000))
    target = 399_997  # 199_998 + 199_999
    a, b = f(arr, target)
    assert a + b == target and a <= b and a in arr and b in arr
    assert f(arr, -1) is None


def test_12_largest_anagram_group_small(solution):
    f = solution("anagram_groups", "largest_anagram_group")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert f(words) == ["ate", "eat", "tea"]


def test_12_largest_anagram_group_no_anagrams(solution):
    f = solution("anagram_groups", "largest_anagram_group")
    assert f(["apple", "banana", "cherry"]) == []
    assert f([]) == []


def test_12_largest_anagram_group_dictionary(solution, data_dir):
    f = solution("anagram_groups", "largest_anagram_group")
    path = data_dir("03-algorithms") / "words.csv"
    words = path.read_text(encoding="utf-8").splitlines()
    assert f(words) == [
        "capers", "escarp", "pacers", "parsec", "recaps", "scrape", "spacer",
    ]


@pytest.mark.parametrize(
    "k, expected",
    [
        (1, ["00", "01", "81"]),
        (2, ["0000", "0001", "2025", "3025", "9801"]),
        (3, ["000000", "000001", "088209", "494209", "998001"]),
        (
            4,
            [
                "00000000", "00000001", "04941729", "07441984", "24502500",
                "25502500", "52881984", "60481729", "99980001",
            ],
        ),
    ],
)
def test_14_quirky_numbers(solution, k, expected):
    f = solution("quirky", "quirky_numbers")
    assert f(k) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], 0),
        ([1], 0),
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
        ([2, 4, 1, 3, 5], 3),
        ([5, 4, 3, 2, 1], 10),
        ([1, 3, 2], 1),
    ],
)
def test_15_count_inversions(solution, arr, expected):
    f = solution("inversions", "count_inversions")
    assert f(arr) == expected


def test_15_count_inversions_large(solution):
    """Наивный O(n^2) перебор пар на 10^5 элементах не уложится в разумное время."""
    f = solution("inversions", "count_inversions")
    arr = list(range(10**5, 0, -1))  # полностью в обратном порядке
    assert f(arr) == 10**5 * (10**5 - 1) // 2


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([13, 10, 5, 2, 9], 4),
        ([-3, -27, -4, -2], 23),
        ([-54, 37, 0, 64, 640, 0, -15], 576),
        ([1, 2], 1),
        ([5], 0),
        ([], 0),
        ([7, 7, 7], 0),
    ],
)
def test_07_max_gap(solution, a0, expected):
    f = solution("max_gap", "max_gap")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
        ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
        ([1, 2, 2, 3, 3], [1, 2, 3]),
        ('', []),
        ([], []),
        ('A', ['A']),
    ],
)
def test_08_unique_in_order(solution, a0, expected):
    f = solution("unique_in_order", "unique_in_order")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([7, 6, 15, 8], [8, 6, 7, 15]),
        ([3, 8, 3, 6, 5, 7, 9, 1], [1, 8, 3, 3, 5, 6, 9, 7]),
        ([], []),
        ([0, 1], [0, 1]),
        ([10, 12], [10, 12]),
    ],
)
def test_09_sort_by_bits(solution, a0, expected):
    f = solution("sort_by_bits", "sort_by_bits")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([5, 4, 2, 3], 22),
        ([12, 6, 10, 26, 3, 24], 342),
        ([1, 1], 1),
        ([1, 2, 3, 4], 10),
        ([], 0),
    ],
)
def test_11_min_pair_sum(solution, a0, expected):
    f = solution("min_pair_sum", "min_pair_sum")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([1, 2, 3, 4, 3, 2, 1], 3),
        ([1, 100, 50, -51, 1, 1], 1),
        ([20, 10, -80, 10, 10, 15, 35], 0),
        ([1, 2, 3, 4, 5, 6], -1),
        ([1], 0),
        ([10, -10, 0], 2),
    ],
)
def test_13_find_even_index(solution, a0, expected):
    f = solution("even_index", "find_even_index")
    assert f(a0) == expected
