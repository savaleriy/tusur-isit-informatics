"""Занятие 7. Деревья и сжатие данных.

Задачи 1-5 - обязательные, они встроены в конспект (docs/07-trees/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import math

import pytest


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def _inorder(root):
    if root is None:
        return []
    return _inorder(root.left) + [root.data] + _inorder(root.right)


def _height_iter(root):
    if root is None:
        return 0
    height = 0
    level = [root]
    while level:
        height += 1
        nxt = []
        for node in level:
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        level = nxt
    return height


def _inorder_iter(root):
    result = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.data)
        cur = cur.right
    return result


def _decode(bits, codes):
    reverse = {code: ch for ch, code in codes.items()}
    result = []
    acc = ""
    for b in bits:
        acc += b
        if acc in reverse:
            result.append(reverse[acc])
            acc = ""
    return "".join(result)


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


def test_01_traversals(solution):
    mod = solution("traversals", None)
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert mod.preorder(root) == [1, 2, 4, 5, 3]
    assert mod.inorder(root) == [4, 2, 5, 1, 3]
    assert mod.postorder(root) == [4, 5, 2, 3, 1]


def test_01_traversals_empty(solution):
    mod = solution("traversals", None)
    assert mod.inorder(None) == []
    assert mod.preorder(None) == []
    assert mod.postorder(None) == []


def test_02_bst(solution):
    BST = solution("bst", "BinarySearchTree")
    tree = BST()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    assert tree.search(7) is True
    assert tree.search(8) is False
    assert tree.search(10) is True
    assert tree.inorder() == [5, 7, 10, 15]


def test_02_bst_duplicates_and_many(solution):
    BST = solution("bst", "BinarySearchTree")
    tree = BST()
    for key in [4, 2, 6, 1, 3, 5, 7, 2, 4]:
        tree.insert(key)
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7]
    assert tree.search(7) is True


def test_03_height(solution):
    height = solution("balance", "height")
    assert height(None) == 0
    assert height(Node(1)) == 1
    assert height(Node(1, Node(2))) == 2
    assert height(Node(1, Node(2), Node(3))) == 2
    assert height(Node(1, None, Node(2, None, Node(3)))) == 3


def test_03_is_balanced(solution):
    is_balanced = solution("balance", "is_balanced")
    assert is_balanced(None) is True
    assert is_balanced(Node(1)) is True
    assert is_balanced(Node(1, Node(2), Node(3))) is True
    assert is_balanced(Node(1, None, Node(2, None, Node(3)))) is False
    assert is_balanced(Node(1, Node(2, Node(3)), None)) is False


def test_04_min_heap(solution):
    MinHeap = solution("heap", "MinHeap")
    h = MinHeap()
    h.push(5)
    h.push(2)
    h.push(8)
    h.push(1)
    assert len(h) == 4
    assert h.peek() == 1
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 5
    assert h.pop() == 8
    assert len(h) == 0


def test_04_min_heap_many(solution):
    MinHeap = solution("heap", "MinHeap")
    h = MinHeap()
    values = [42, 17, 3, 99, 7, 1, 25, 0, 8]
    for v in values:
        h.push(v)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)


def test_05_huffman_codes(solution):
    huffman_codes = solution("huffman", "huffman_codes")
    text = "aabbbcccccddddddd"
    codes = huffman_codes(text)
    assert set(codes) == set(text)
    code_list = list(codes.values())
    for i in range(len(code_list)):
        for j in range(len(code_list)):
            if i != j:
                assert not code_list[i].startswith(code_list[j]), "коды не префиксные"
    bits = "".join(codes[ch] for ch in text)
    assert _decode(bits, codes) == text


def test_05_huffman_single_char(solution):
    huffman_codes = solution("huffman", "huffman_codes")
    assert huffman_codes("aaaa") == {"a": "0"}
    assert huffman_codes("") == {}


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


def test_06_is_bst(solution):
    is_bst = solution("is_bst", "is_bst")
    assert is_bst(None) is True
    assert is_bst(Node(2, Node(1), Node(3))) is True
    assert is_bst(Node(1, Node(2), Node(3))) is False
    assert is_bst(Node(5, Node(3), Node(7, Node(6), Node(9)))) is True
    assert is_bst(Node(5, Node(3), Node(7, Node(4), Node(9)))) is False
    assert is_bst(Node(2, Node(2), Node(3))) is False


def _delete_tree():
    return Node(5, Node(3, Node(2)), Node(8, Node(7), Node(9)))


@pytest.mark.parametrize(
    "key, expected",
    [
        (2, [3, 5, 7, 8, 9]),    # лист
        (8, [2, 3, 5, 7, 9]),    # два потомка
        (5, [2, 3, 7, 8, 9]),    # корень, два потомка
        (7, [2, 3, 5, 8, 9]),    # лист
        (99, [2, 3, 5, 7, 8, 9]),  # нет такого ключа
    ],
)
def test_10_bst_delete(solution, key, expected):
    delete = solution("bst_delete", "delete")
    root = delete(_delete_tree(), key)
    assert _inorder(root) == expected


def test_12_top_k_frequent(solution):
    f = solution("top_k", "top_k_frequent")
    words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    assert f(words, 2) == ["apple", "banana"]
    assert f(words, 3) == ["apple", "banana", "cherry"]


def test_12_top_k_frequent_ties_and_large(solution):
    f = solution("top_k", "top_k_frequent")
    assert f(["a", "b", "c"], 2) == ["a", "b"]
    assert f([], 3) == []
    words = [f"w{i % 100}" for i in range(10_000)]
    top = f(words, 3)
    assert len(top) == 3
    # все 100 слов встречаются поровну, поэтому берём три первых по алфавиту
    assert top == ["w0", "w1", "w10"]


def test_14_huffman_encode_decode(solution):
    encode = solution("huffman_codec", "encode")
    decode = solution("huffman_codec", "decode")
    codes = {"t": "0", "i": "10", "l": "11"}
    assert encode("tilt", codes) == "010110"
    assert decode("010110", codes) == "tilt"
    assert encode("til", codes) == "01011"
    assert decode("01011", codes) == "til"


def test_14_huffman_roundtrip(solution):
    encode = solution("huffman_codec", "encode")
    decode = solution("huffman_codec", "decode")
    codes = {"a": "0", "b": "10", "c": "110", "d": "111"}
    for text in ["a", "bb", "cab", "abcd", "ddddca"]:
        assert decode(encode(text, codes), codes) == text


def test_15_balanced_bst_small(solution):
    build = solution("balanced_bst", "build_balanced_bst")
    root = build([1, 2, 3, 4, 5, 6, 7])
    assert root.data == 4
    assert _inorder(root) == [1, 2, 3, 4, 5, 6, 7]
    assert _height_iter(root) == 3


def test_15_balanced_bst_large(solution):
    """Наивная вставка по одному даёт вырожденное дерево высотой n - не пройдёт
    ни по времени, ни по высоте."""
    build = solution("balanced_bst", "build_balanced_bst")
    n = 100_000
    root = build(list(range(1, n + 1)))
    assert _height_iter(root) <= 2 * math.ceil(math.log2(n + 1))
    assert _inorder_iter(root) == list(range(1, n + 1))


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('Hey fellow warriors', 'Hey wollef sroirraw'),
        ('This is a test', 'This is a test'),
        ('This is another test', 'This is rehtona test'),
        ('Just kidding there is still one more', 'Just gniddik ereht is llits one more'),
        ('abcde', 'edcba'),
    ],
)
def test_07_spin_words(solution, a0, expected):
    f = solution("spin_words", "spin_words")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (9, True),
        (23, True),
        (4343456, True),
        (79, False),
        (1, True),
        (10, True),
        (32, True),
        (22, False),
    ],
)
def test_08_is_jumping(solution, a0, expected):
    f = solution("jumping", "is_jumping")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('is2 Thi1s T4est 3a', 'Thi1s is2 3a T4est'),
        ('4of Fo1r pe6ople g3ood th5e the2', 'Fo1r the2 g3ood 4of th5e pe6ople'),
        ('', ''),
        ('a1', 'a1'),
    ],
)
def test_09_order_words(solution, a0, expected):
    f = solution("order_words", "order_words")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (3, [1, 3]),
        (7, [1, 3, 5, 7]),
        (1, [1]),
        (10, [1, 3, 5, 7, 9]),
        (0, []),
    ],
)
def test_11_extra_perfect(solution, a0, expected):
    f = solution("extra_perfect", "extra_perfect")
    assert f(a0) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        (['bat', 'tab', 'cat'], [(0, 1), (1, 0)]),
        (['dog', 'cow', 'tap', 'god', 'pat'], [(0, 3), (2, 4), (3, 0), (4, 2)]),
        (['abcd', 'dcba', 'lls', 's', 'sssll'], [(0, 1), (1, 0), (2, 4), (3, 2)]),
        (['a'], []),
        ([], []),
    ],
)
def test_13_palindrome_pairs(solution, a0, expected):
    f = solution("palindrome_pairs", "palindrome_pairs")
    assert f(a0) == expected
