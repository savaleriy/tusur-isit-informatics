"""Занятие 4. Структуры данных.

Задачи 1-5 - обязательные, они встроены в конспект (docs/04-data-structures/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import pytest


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


def test_02_queue_basic(solution):
    Queue = solution("my_queue", "Queue")
    q = Queue()
    assert q.is_empty() is True
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.size() == 3
    assert q.front() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.front() == "c"
    assert q.dequeue() == "c"
    assert q.is_empty() is True


def test_02_queue_empty_errors(solution):
    Queue = solution("my_queue", "Queue")
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.front()


def test_03_linked_list_basic(solution):
    LinkedList = solution("linked_list", "LinkedList")
    lst = LinkedList()
    assert lst.to_list() == []
    lst.append(1)
    lst.append(2)
    lst.prepend(0)
    assert lst.to_list() == [0, 1, 2]
    lst.append(3)
    assert lst.to_list() == [0, 1, 2, 3]
    lst.delete(1)
    assert lst.to_list() == [0, 2, 3]


def test_03_linked_list_delete_edges(solution):
    LinkedList = solution("linked_list", "LinkedList")
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.delete(1)          # удалить голову
    assert lst.to_list() == [2, 3]
    lst.delete(3)          # удалить хвост
    assert lst.to_list() == [2]
    lst.delete(999)        # удалить отсутствующий
    assert lst.to_list() == [2]


def test_04_hash_set_basic(solution):
    HashSet = solution("hash_set", "HashSet")
    s = HashSet()
    assert len(s) == 0
    s.add(1)
    s.add(2)
    s.add(2)               # дубликат не добавляется
    assert len(s) == 2
    assert s.contains(1) is True
    assert s.contains(2) is True
    assert s.contains(3) is False
    s.remove(1)
    assert s.contains(1) is False
    assert len(s) == 1


def test_04_hash_set_collision(solution):
    """10 и 20 при размере 10 попадают в один кармашек - коллизия не должна
    терять значения."""
    HashSet = solution("hash_set", "HashSet")
    s = HashSet(size=10)
    s.add(10)
    s.add(20)
    assert len(s) == 2
    assert s.contains(10) is True
    assert s.contains(20) is True
    s.remove(10)
    assert s.contains(10) is False
    assert s.contains(20) is True


def test_05_bfs(solution):
    bfs = solution("graph", "bfs")
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert bfs(graph, 1) == [1, 2, 3, 4]


def test_05_bfs_disconnected_and_cycle(solution):
    bfs = solution("graph", "bfs")
    assert bfs({1: [2], 2: [], 3: [4], 4: []}, 1) == [1, 2]
    assert bfs({1: [2], 2: [3], 3: [1]}, 1) == [1, 2, 3]
    assert bfs({1: []}, 1) == [1]


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


def test_06_doubly_linked_list(solution):
    DoublyLinkedList = solution("dll", "DoublyLinkedList")
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    assert dll.to_list() == [0, 1, 2, 3]
    assert dll.to_list_reverse() == [3, 2, 1, 0]
    dll.delete(2)
    assert dll.to_list() == [0, 1, 3]
    assert dll.to_list_reverse() == [3, 1, 0]


def test_06_doubly_linked_list_delete_edges(solution):
    DoublyLinkedList = solution("dll", "DoublyLinkedList")
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.delete(1)
    assert dll.to_list() == [2, 3]
    dll.delete(3)
    assert dll.to_list() == [2]
    assert dll.to_list_reverse() == [2]


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
def test_10_is_balanced(solution, s, expected):
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
def test_12_evaluate_rpn(solution, tokens, expected):
    f = solution("rpn", "evaluate_rpn")
    assert f(tokens) == pytest.approx(expected)


def test_14_shortest_path(solution):
    f = solution("graph_path", "shortest_path")
    graph = {0: [1], 1: [2, 3], 2: [3], 3: []}
    assert f(graph, 0, 3) == [0, 1, 3]


def test_14_shortest_path_no_path(solution):
    f = solution("graph_path", "shortest_path")
    graph = {0: [1], 1: [2, 3], 2: [3], 3: []}
    assert f(graph, 3, 0) is None
    assert f(graph, 0, 99) is None
    assert f(graph, 0, 0) == [0]


def test_14_shortest_path_longer_detour(solution):
    f = solution("graph_path", "shortest_path")
    graph = {0: [1], 1: [2, 4], 2: [3], 3: [4], 4: []}
    assert f(graph, 0, 4) == [0, 1, 4]


def test_15_lru_cache(solution):
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


def test_15_lru_cache_update_refreshes(solution):
    LRUCache = solution("lru", "LRUCache")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)         # обновить существующий ключ
    cache.put(3, 3)          # вытесняет ключ 2 (ключ 1 свежий)
    assert cache.get(1) == 10
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_15_lru_cache_large(solution):
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
def test_07_count_duplicates(solution, a0, expected):
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
def test_08_filter_numbers(solution, a0, expected):
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
def test_09_count_positives_sum_negatives(solution, a0, expected):
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
def test_11_duplicate_encode(solution, a0, expected):
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
def test_13_likes(solution, a0, expected):
    f = solution("likes", "likes")
    assert f(a0) == expected
