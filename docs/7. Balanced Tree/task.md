
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


