"""Занятие 4.2. Абстрактные типы данных.

Задачи 1-6 - обязательные, они встроены в конспект (docs/04-data-structures/note.md).
Задачи 7-16 - балльные (в task.md они пронумерованы 1-10).
"""

import operator
import random
from collections import deque

import pytest


class Counted:
    """Число, которое считает, сколько раз его сравнивали."""

    comparisons = 0

    def __init__(self, value):
        self.value = value

    def _compare(self, other, op):
        Counted.comparisons += 1
        return op(self.value, other.value)

    def __lt__(self, other):
        return self._compare(other, operator.lt)

    def __le__(self, other):
        return self._compare(other, operator.le)

    def __gt__(self, other):
        return self._compare(other, operator.gt)

    def __ge__(self, other):
        return self._compare(other, operator.ge)

    def __eq__(self, other):
        return self._compare(other, operator.eq)

    def __ne__(self, other):
        return self._compare(other, operator.ne)


class Key:
    """Ключ с заданным хешем, который считает вызовы `==`."""

    eq_calls = 0

    def __init__(self, n):
        self.n = n

    def __hash__(self):
        return self.n

    def __eq__(self, other):
        Key.eq_calls += 1
        return isinstance(other, Key) and self.n == other.n


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


def test_01_stack_basic(solution):
    Stack = solution("stack", "Stack")
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.is_empty() is False
    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.size() == 1
    assert s.pop() == 1
    assert s.is_empty() is True


def test_01_stack_empty_errors(solution):
    Stack = solution("stack", "Stack")
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


def test_02_dynamic_array_basic(solution):
    DynamicArray = solution("dynamic_array", "DynamicArray")
    a = DynamicArray()
    assert len(a) == 0
    assert a.capacity == 4
    for x in range(5):
        a.append(x * 10)
    assert len(a) == 5
    assert a.capacity == 8             # пятому элементу не хватило места
    assert [a[i] for i in range(5)] == [0, 10, 20, 30, 40]
    a[1] = 99
    assert a[1] == 99
    assert a.pop() == 40
    assert len(a) == 4
    assert a.capacity == 8             # при снятии ёмкость не уменьшается
    a.append(7)
    assert a[4] == 7


def test_02_dynamic_array_doubling(solution):
    DynamicArray = solution("dynamic_array", "DynamicArray")
    a = DynamicArray()
    capacities = []
    for x in range(100):
        a.append(x)
        capacities.append(a.capacity)
    expected = [max(4, 1 << (n - 1).bit_length()) for n in range(1, 101)]
    assert capacities == expected      # 4, 4, 4, 4, 8, ..., 8, 16, ...
    assert [a[i] for i in range(100)] == list(range(100))
    with pytest.raises(AttributeError):
        a.capacity = 1000


def test_02_dynamic_array_errors(solution):
    DynamicArray = solution("dynamic_array", "DynamicArray")
    a = DynamicArray()
    with pytest.raises(IndexError):
        a.pop()
    with pytest.raises(IndexError):
        a[0]
    a.append("x")
    for bad in (1, 3, -1):             # за концом, в запасе ёмкости, отрицательный
        with pytest.raises(IndexError):
            a[bad]
        with pytest.raises(IndexError):
            a[bad] = "y"
    assert a[0] == "x"
    assert len(a) == 1


def test_03_dll_basic(solution):
    DoublyLinkedList = solution("dll", "DoublyLinkedList")
    dll = DoublyLinkedList()
    assert dll.head is None and dll.tail is None
    assert dll.to_list() == [] and dll.to_list_reverse() == []
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    assert dll.to_list() == [0, 1, 2, 3]
    assert dll.to_list_reverse() == [3, 2, 1, 0]
    dll.delete(2)
    assert dll.to_list() == [0, 1, 3]
    assert dll.to_list_reverse() == [3, 1, 0]


def test_03_dll_head_and_tail(solution):
    DoublyLinkedList = solution("dll", "DoublyLinkedList")
    dll = DoublyLinkedList()
    dll.append(1)
    assert dll.head is dll.tail                        # один узел - и голова, и хвост
    dll.append(2)
    dll.prepend(0)
    assert (dll.head.data, dll.tail.data) == (0, 2)
    assert dll.head.prev is None and dll.tail.next is None
    assert dll.head.next.next is dll.tail
    assert dll.tail.prev.prev is dll.head
    dll.delete(2)                                      # хвост переезжает
    assert dll.tail.data == 1 and dll.tail.next is None
    dll.delete(0)                                      # голова переезжает
    assert dll.head is dll.tail and dll.head.prev is None
    dll.delete(1)
    assert dll.head is None and dll.tail is None


def test_03_dll_delete_edges(solution):
    DoublyLinkedList = solution("dll", "DoublyLinkedList")
    dll = DoublyLinkedList()
    dll.delete(1)                      # из пустого - ничего не происходит
    assert dll.to_list() == []
    for x in (1, 2, 1, 3):
        dll.append(x)
    dll.delete(1)                      # только первое вхождение
    assert dll.to_list() == [2, 1, 3]
    assert dll.to_list_reverse() == [3, 1, 2]
    dll.delete(999)                    # отсутствующий
    assert dll.to_list() == [2, 1, 3]
    dll.delete(3)                      # хвост
    dll.append(4)
    assert dll.to_list_reverse() == [4, 1, 2]


def test_04_deque_basic(solution):
    Deque = solution("ring_deque", "Deque")
    d = Deque()
    assert d.is_empty() is True and len(d) == 0
    assert d.capacity == 4
    d.push_back(1)
    d.push_back(2)
    d.push_front(0)                    # голова переехала в конец массива
    assert (d.front(), d.back()) == (0, 2)
    assert len(d) == 3
    assert d.pop_back() == 2
    assert d.pop_front() == 0
    assert len(d) == 1
    for x in range(10):
        d.push_back(x)
    assert len(d) == 11
    assert d.capacity == 16
    assert [d.pop_front() for _ in range(11)] == [1] + list(range(10))
    assert d.is_empty() is True


def test_04_deque_empty_errors(solution):
    Deque = solution("ring_deque", "Deque")
    d = Deque()
    for action in (d.pop_front, d.pop_back, d.front, d.back):
        with pytest.raises(IndexError):
            action()
    d.push_front("x")
    assert d.pop_back() == "x"
    with pytest.raises(IndexError):
        d.pop_front()
    with pytest.raises(AttributeError):
        d.capacity = 100


def test_04_deque_against_collections(solution):
    """Случайные операции на обоих концах сверяются с collections.deque."""
    Deque = solution("ring_deque", "Deque")
    rng = random.Random(4)
    d, model = Deque(), deque()
    for step in range(5000):
        op = rng.randrange(4)
        if op == 0:
            d.push_back(step)
            model.append(step)
        elif op == 1:
            d.push_front(step)
            model.appendleft(step)
        elif op == 2 and model:
            assert d.pop_back() == model.pop()
        elif op == 3 and model:
            assert d.pop_front() == model.popleft()
        assert len(d) == len(model)
        if model:
            assert (d.front(), d.back()) == (model[0], model[-1])
        assert d.capacity >= len(d) and d.capacity & (d.capacity - 1) == 0   # степень двойки


def test_05_hash_map_basic(solution):
    HashMap = solution("hash_map", "HashMap")
    m = HashMap()
    assert len(m) == 0
    m.put("яблоко", 50)
    m.put("груша", 70)
    m.put("яблоко", 55)                # ключ уже есть - значение заменяется
    assert len(m) == 2
    assert m.get("яблоко") == 55
    assert m.contains("груша") is True
    assert m.contains("слива") is False
    m.remove("груша")
    assert m.contains("груша") is False
    assert len(m) == 1
    with pytest.raises(KeyError):
        m.get("груша")
    with pytest.raises(KeyError):
        m.remove("груша")
    m.put("пусто", None)               # значение None - тоже значение
    assert m.contains("пусто") is True
    assert m.get("пусто") is None


def test_05_hash_map_collision(solution):
    """10 и 20 при размере 10 попадают в один кармашек."""
    HashMap = solution("hash_map", "HashMap")
    m = HashMap(size=10)
    m.put(10, "a")
    m.put(20, "b")
    assert len(m) == 2
    assert (m.get(10), m.get(20)) == ("a", "b")
    m.put(20, "c")
    assert (m.get(10), m.get(20)) == ("a", "c")
    m.remove(10)
    assert m.contains(10) is False
    assert m.get(20) == "c"
    assert len(m) == 1


def test_05_hash_map_looks_into_one_bucket(solution):
    """100 ключей в 10 кармашках: поиск сравнивает ключ только с соседями
    по кармашку, а не со всеми ключами подряд."""
    HashMap = solution("hash_map", "HashMap")
    m = HashMap(size=10)
    keys = [Key(i) for i in range(100)]
    for k in keys:
        m.put(k, k.n)
    assert len(m) == 100
    Key.eq_calls = 0
    for k in keys:
        assert m.get(Key(k.n)) == k.n
    assert Key.eq_calls <= 100 * 10


def test_06_priority_queue_basic(solution):
    PriorityQueue = solution("priority_queue", "PriorityQueue")
    er = PriorityQueue()
    assert er.is_empty() is True and len(er) == 0
    er.push("порез пальца", 3)
    er.push("перелом", 2)
    er.push("остановка сердца", 1)
    er.push("ушиб", 3)
    assert len(er) == 4
    assert er.peek() == "остановка сердца"
    assert len(er) == 4                # peek ничего не снимает
    assert er.pop() == "остановка сердца"
    assert er.pop() == "перелом"
    assert er.pop() == "порез пальца"  # пришёл раньше ушиба с тем же приоритетом
    assert er.pop() == "ушиб"
    assert er.is_empty() is True
    with pytest.raises(IndexError):
        er.pop()
    with pytest.raises(IndexError):
        er.peek()


def test_06_priority_queue_fifo_any_items(solution):
    """Элементы бывают несравнимыми (словари); при равном приоритете - кто раньше пришёл."""
    PriorityQueue = solution("priority_queue", "PriorityQueue")
    pq = PriorityQueue()
    for i in range(6):
        pq.push({"id": i}, 5)
    pq.push({"id": "срочно"}, 0)
    pq.push({"id": "потом"}, 9.5)
    assert pq.pop() == {"id": "срочно"}
    assert [pq.pop()["id"] for _ in range(6)] == list(range(6))
    assert pq.pop() == {"id": "потом"}


def test_06_priority_queue_random(solution):
    PriorityQueue = solution("priority_queue", "PriorityQueue")
    rng = random.Random(6)
    pq, model = PriorityQueue(), []    # model: (приоритет, номер прихода, элемент)
    for arrival in range(3000):
        if model and rng.random() < 0.4:
            model.sort()
            assert pq.pop() == model.pop(0)[2]
        else:
            priority = rng.randint(-10, 10)
            pq.push(f"x{arrival}", priority)
            model.append((priority, arrival, f"x{arrival}"))
        assert len(pq) == len(model)


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


def test_07_min_stack(solution):
    MinStack = solution("min_stack", "MinStack")
    s = MinStack()
    s.push(5)
    s.push(2)
    s.push(8)
    assert (s.get_min(), s.peek(), len(s)) == (2, 8, 3)
    assert s.pop() == 8
    assert s.get_min() == 2
    assert s.pop() == 2
    assert s.get_min() == 5
    s.push(5)                          # минимум повторяется
    s.push(1)
    assert s.pop() == 1
    assert s.pop() == 5
    assert s.get_min() == 5            # вторая пятёрка ещё в стеке
    assert s.pop() == 5
    assert len(s) == 0
    for action in (s.pop, s.peek, s.get_min):
        with pytest.raises(IndexError):
            action()


def test_07_min_stack_random(solution):
    MinStack = solution("min_stack", "MinStack")
    rng = random.Random(7)
    s, model = MinStack(), []
    for _ in range(3000):
        if model and rng.random() < 0.45:
            assert s.pop() == model.pop()
        else:
            x = rng.randint(-100, 100)
            s.push(x)
            model.append(x)
        if model:
            assert s.get_min() == min(model)


def test_07_min_stack_no_scan(solution):
    """get_min не перебирает стек: на операцию - не больше пары сравнений."""
    MinStack = solution("min_stack", "MinStack")
    rng = random.Random(8)
    s = MinStack()
    values = [Counted(rng.randint(0, 10 ** 6)) for _ in range(1000)]
    Counted.comparisons = 0
    for v in values:
        s.push(v)
        s.get_min()
    while len(s):
        s.get_min()
        s.pop()
    assert Counted.comparisons <= 4 * len(values)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("([])", True),
        ("([{}])", True),
        ("(]", False),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("", True),
    ],
)
def test_11_is_balanced(solution, s, expected):
    f = solution("brackets", "is_balanced")
    assert f(s) is expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        ([2, 3, "+"], 5),
        ([2, 3, "*"], 6),
        ([5, 1, 2, "+", 4, "*", "+", 3, "-"], 14),
        ([6, 2, "/"], 3.0),
        ([4, 13, 5, "/", "+"], 6.6),
        ([9, 3, "-"], 6),
    ],
)
def test_13_evaluate_rpn(solution, tokens, expected):
    f = solution("rpn", "evaluate_rpn")
    assert f(tokens) == pytest.approx(expected)


def test_15_merge_k_sorted(solution):
    f = solution("merge_k", "merge_k_sorted")
    assert f([[1, 4, 7], [2, 5, 8], [0, 3, 6, 9]]) == list(range(10))
    assert f([[], [1], []]) == [1]
    assert f([]) == []
    assert f([[], []]) == []
    assert f([[1, 1, 3], [1, 2]]) == [1, 1, 1, 2, 3]
    assert f([[-5, 0, 5]]) == [-5, 0, 5]


def test_15_merge_k_sorted_random_and_inputs_untouched(solution):
    f = solution("merge_k", "merge_k_sorted")
    rng = random.Random(7)
    for _ in range(50):
        lists = [sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 30)))
                 for _ in range(rng.randint(1, 8))]
        snapshot = [lst[:] for lst in lists]
        assert f(lists) == sorted(x for lst in lists for x in lst)
        assert lists == snapshot           # исходные списки не испорчены


def test_15_merge_k_sorted_large(solution):
    f = solution("merge_k", "merge_k_sorted")
    lists = [list(range(i, 30_000, 10)) for i in range(10)]
    assert f(lists) == list(range(30_000))


def test_16_lru_cache(solution):
    LRUCache = solution("lru", "LRUCache")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)          # вытесняет ключ 2
    assert cache.get(2) == -1
    cache.put(4, 4)          # вытесняет ключ 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_16_lru_cache_update_refreshes(solution):
    LRUCache = solution("lru", "LRUCache")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)         # обновить существующий ключ
    cache.put(3, 3)          # вытесняет ключ 2 (ключ 1 свежий)
    assert cache.get(1) == 10
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_16_lru_cache_large(solution):
    """Сотня тысяч операций: решение с O(n) на операцию не уложится во время."""
    LRUCache = solution("lru", "LRUCache")
    cache = LRUCache(1000)
    for i in range(50_000):
        cache.put(i, i)
    assert cache.get(0) == -1        # давно вытеснен
    assert cache.get(49_000) == 49_000
    assert cache.get(49_999) == 49_999


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('abcde', 0),
        ('aabbcde', 2),
        ('aabBcde', 2),
        ('indivisibility', 1),
        ('Indivisibilities', 2),
        ('aA11', 2),
        ('ABBA', 2),
        ('', 0),
    ],
)
def test_08_count_duplicates(solution, a0, expected):
    f = solution("count_duplicates", "count_duplicates")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([1, 2, 'a', 'b'], [1, 2]),
        ([1, 'a', 'b', 0, 15], [1, 0, 15]),
        ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
        ([], []),
        (['a'], []),
    ],
)
def test_09_filter_numbers(solution, a0, expected):
    f = solution("filter_numbers", "filter_numbers")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]),
        ([0, 0, 0], [0, 0]),
        ([], []),
        ([1], [1, 0]),
        ([-1], [0, -1]),
    ],
)
def test_10_count_positives_sum_negatives(solution, a0, expected):
    f = solution("positives_negatives", "count_positives_sum_negatives")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('din', '((('),
        ('recede', '()()()'),
        ('Success', ')())())'),
        ('(( @', '))(('),
        ('', ''),
    ],
)
def test_12_duplicate_encode(solution, a0, expected):
    f = solution("duplicate_encode", "duplicate_encode")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ([], 'no one likes this'),
        (['Peter'], 'Peter likes this'),
        (['Jacob', 'Alex'], 'Jacob and Alex like this'),
        (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
        (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this'),
        (['A', 'B', 'C', 'D', 'E'], 'A, B and 3 others like this'),
    ],
)
def test_14_likes(solution, a0, expected):
    f = solution("likes", "likes")
    assert f(a0) == expected
