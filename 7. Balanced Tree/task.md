
# BST

Реализовать базовое бинарное дерево поиска и и продемонстрировать его работу.

```python
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        """Вставка элемента в дерево"""
        pass
    
    def search(self, key):
        """Поиск элемента по ключу"""
        pass
    
    def delete(self, key):
        """Удаление элемента из дерева"""
        pass
    
    def inorder_traversal(self):
        """Центрированный обход (возвращает отсортированные ключи)"""
        pass
    
    def preorder_traversal(self):
        """Прямой обход"""
        pass
    
    def postorder_traversal(self):
        """Обратный обход"""
        pass
    
    def height(self):
        """Высота дерева"""
        pass
    
    def is_balanced(self):
        """Проверка сбалансированности дерева"""
        pass
    
    def find_min(self):
        """Найти минимальный ключ"""
        pass
    
    def find_max(self):
        """Найти максимальный ключ"""
        pass
    
    def successor(self, key):
        """Найти преемника для ключа"""
        pass
    
    def predecessor(self, key):
        """Найти предшественника для ключа"""
        pass

```

# Алгоритма Хаффмана

Реализовать алгоритм сжатия Хаффмана и продемонстрировать его работу на практических примерах.

```python
class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}
    
    def build_tree(self):
        # 1. Посчитать частоты символов
        # 2. Построить приоритетную очередь
        # 3. Построить дерево Хаффмана
        pass
    
    def _generate_codes(self, node, current_code):
        # Рекурсивно сгенерировать коды для символов
        pass
    
    def encode(self, text):
        # Закодировать текст используя таблицу кодов
        pass
    
    def decode(self, encoded_text):
        # Декодировать бинарную строку обратно в текст
        pass
```

# АВЛ-дерево

Реализовать самобалансирующееся АВЛ-дерево и продемонстрировать его работу.

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        # Вставка с последующей балансировкой
        pass
    
    def _get_height(self, node):
        pass
    
    def _get_balance(self, node):
        # Вычислить коэффициент балансировки
        pass
    
    def _left_rotate(self, z):
        # Левый поворот
        pass
    
    def _right_rotate(self, z):
        # Правый поворот
        pass
    
    def _left_right_rotate(self, z):
        # Лево-правый поворот
        pass
    
    def _right_left_rotate(self, z):
        # Право-левый поворот
        pass
    
    def search(self, key):
        pass
    
    def inorder_traversal(self):
        pass
```

# Косое дерево

Реализовать косое дерево и продемонстрировать его свойство перемещения часто используемых элементов ближе к корню.


```python
class SplayNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        """Вставка элемента с последующим перемещением в корень"""
        pass
    
    def search(self, key):
        """Поиск элемента с последующим перемещением в корень (если найден)"""
        pass
    
    def delete(self, key):
        """Удаление элемента с последующим перемещением родителя в корень"""
        pass
    
    def splay(self, node):
        """Перемещение узла в корень с помощью серии поворотов"""
        pass
    
    def _rotate_left(self, node):
        """Левый поворот"""
        pass
    
    def _rotate_right(self, node):
        """Правый поворот"""
        pass
    
    def _zig(self, node):
        """Поворот, когда node - левый ребенок корня"""
        pass
    
    def _zag(self, node):
        """Поворот, когда node - правый ребенок корня"""
        pass
    
    def _zig_zig(self, node):
        """Двойной поворот zig-zig"""
        pass
    
    def _zag_zag(self, node):
        """Двойной поворот zag-zag"""
        pass
    
    def _zig_zag(self, node):
        """Поворот zig-zag"""
        pass
    
    def _zag_zig(self, node):
        """Поворот zag-zig"""
        pass
    
    def inorder_traversal(self):
        """Центрированный обход"""
        pass
    
    def height(self):
        """Высота дерева"""
        pass
    
    def _get_height(self, node):
        pass
    ```

# B-дерево

Реализовать B-дерево и продемонстрировать его работу.

```python
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # минимальная степень
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t  # минимальная степень
    
    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == (2 * self.t - 1):
                new_root = BTreeNode(self.t, False)
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                self.root = new_root
            self._insert_non_full(self.root, key)
    
    def _insert_non_full(self, node, key):
        # Вставка в неполный узел
        pass
    
    def _split_child(self, parent, i):
        # Разделение дочернего узла
        pass
    
    def search(self, key, node=None):
        # Поиск ключа в дереве
        pass
    
    def traverse(self):
        # Обход дерева
        if self.root:
            self._traverse(self.root)
    
    def _traverse(self, node):
        for i in range(len(node.keys)):
            if not node.leaf:
                self._traverse(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self._traverse(node.children[len(node.keys)])
```

