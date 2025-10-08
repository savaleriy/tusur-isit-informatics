## 1. Stack

Вам необходимо реализовать класс `Stack`, который будет представлять собой стек. Стек — это структура данных, работающая по принципу "последний пришёл — первый вышел" (LIFO).

**Класс `Stack`**:

- Реализуйте класс `Stack`, который будет содержать следующие методы:
    - `__init__(self)`: инициализирует пустой стек.
    - `is_empty(self)`: возвращает `True`, если стек пуст, и `False` в противном случае.
    - `push(self, item)`: добавляет элемент на верх стека.
    - `pop(self)`: удаляет и возвращает верхний элемент стека. Если стек пуст, необходимо обработать ошибку.
    - `peek(self)`: возвращает верхний элемент стека, не удаляя его. Если стек пуст, необходимо обработать ошибку.
    - `size(self)`: возвращает количество элементов в стеке.

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
	   pass 
	   
    def push(self, item):
	   pass 
	   
    def pop(self):
	   pass 
	   
    def peek(self):
	   pass 
	   
    def size(self):
	   pass 

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items)

# Pop an item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)

# Peek at the top of the stack
top_item = my_stack.peek()
print("Top item:", top_item)

# Check if the stack is empty
print("Is stack empty?", my_stack.is_empty())

# Get the size of the stack
print("Stack size:", my_stack.size())
```

## 2. Queue

Вам необходимо реализовать класс `Queue`, который будет представлять собой очередь. Очередь — это структура данных, работающая по принципу "первый пришёл — первый вышел" (FIFO).

**Класс `Queue`**:
- Реализуйте класс `Queue`, который будет содержать следующие методы:
    - `__init__(self)`: инициализирует пустую очередь.
    - `is_empty(self)`: возвращает `True`, если очередь пуста, и `False` в противном случае.
    - `enqueue(self, item, priority=5)`: добавляет элемент в очередь с указанным приоритетом (по умолчанию 5). После добавления элемента, очередь должна быть отсортирована по приоритету.
    - `dequeue(self)`: удаляет и возвращает элемент из очереди с наивысшим приоритетом (наименьшее значение приоритета).
    - `front(self)`: возвращает элемент на переднем плане очереди без удаления его. Если очередь пуста, необходимо обработать ошибку.
    - `size(self)`: возвращает количество элементов в очереди.
    - `sort_queue(self)`: сортирует очередь на основе приоритета (в порядке возрастания).

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
	    pass
	    
    def enqueue(self, item, priority=5):
	    pass
	    
    def dequeue(self):
	    pass
	    
    def front(self):
	    pass
	    
    def size(self):
	    pass
	    
    def sort_queue(self):
	    pass

# Example usage:
my_queue = Queue()

my_queue.enqueue(1, priority=2)
my_queue.enqueue(2, priority=5)
my_queue.enqueue(3, priority=0)

print("Queue:", my_queue.items)

# Dequeue an item from the queue
dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)

# Get the front of the queue
front_item = my_queue.front()
print("Front item:", front_item)

# Enqueue a new item with priority
my_queue.enqueue(4, priority=3)
print("Queue after enqueue:", my_queue.items)

# Check if the queue is empty
print("Is queue empty?", my_queue.is_empty())

# Get the size of the queue
print("Queue size:", my_queue.size())


```
## 3. Linked List 

Вам необходимо реализовать класс `LinkedList`, который будет представлять собой связный список. Связный список — это структура данных, состоящая из узлов, каждый из которых содержит данные и ссылку на следующий узел в списке.

- **Класс `Node`**:
    
    - Реализуйте класс `Node`, который будет представлять отдельный узел в списке. Узел должен содержать:
        - `data`: данные, хранящиеся в узле.
        - `next`: ссылка на следующий узел (по умолчанию `None`).
- **Класс `LinkedList`**:
    
    - Реализуйте класс `LinkedList`, который будет содержать следующие методы:
        - `__init__(self)`: инициализирует пустой связный список.
        - `is_empty(self)`: возвращает `True`, если список пуст, и `False` в противном случае.
        - `append(self, data)`: добавляет новый узел с указанными данными в конец списка.
        - `prepend(self, data)`: добавляет новый узел с указанными данными в начало списка.
        - `delete(self, data)`: удаляет узел с указанными данными из списка.
        - `display(self)`: выводит данные всех узлов в списке.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
	    pass
	    
    def append(self, data):
	    pass
	    
    def prepend(self, data):
	    pass
	    
    def delete(self, data):
	    pass
	    
    def display(self):
	    pass

# Example usage:
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()
```
## 4. Unorder map

Вам необходимо реализовать класс `UnorderedMap`, который будет представлять собой хэш-таблицу (неупорядоченную карту). Хэш-таблица позволяет эффективно хранить и извлекать пары "ключ-значение".

- **Класс `KeyValuePair`**:
    
    - Реализуйте класс `KeyValuePair`, который будет представлять собой пару "ключ-значение". Он должен содержать:
        - `key`: ключ пары.
        - `value`: значение, связанное с ключом.
- **Класс `UnorderedMap`**:
    
    - Реализуйте класс `UnorderedMap`, который будет содержать следующие методы:
        - `__init__(self, size=10)`: инициализирует хэш-таблицу с заданным количеством "ведер" (по умолчанию 10).
        - `_hash(self, key)`: простая хэш-функция, которая вычисляет индекс для данного ключа.
        - `set(self, key, value)`: добавляет или обновляет значение для указанного ключа.
        - `get(self, key, default=None)`: возвращает значение по указанному ключу. Если ключ не найден, возвращает значение по умолчанию.
        - `remove(self, key)`: удаляет пару "ключ-значение" по указанному ключу.
        - `keys(self)`: возвращает список всех ключей в карте.
        - `values(self)`: возвращает список всех значений в карте.
        - `items(self)`: возвращает список всех пар "ключ-значение".

```python
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def set(self, key, value):
	    pass
	    
    def get(self, key, default=None):
	    pass
	    
    def remove(self, key):
	    pass
	    
    def keys(self):
	    pass
	    
    def values(self):
	    pass
	    
    def items(self):
	    pass
		
my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
```

## 5. Unordered Set

Вам необходимо реализовать класс `UnorderedSet`, который будет представлять собой неупорядоченное множество. Неупорядоченное множество позволяет хранить уникальные элементы и выполнять операции, такие как добавление, удаление и проверка наличия элементов.

**Класс `UnorderedSet`**:

- Реализуйте класс `UnorderedSet`, который будет содержать следующие методы:
    - `__init__(self, size=10)`: инициализирует множество с заданным количеством (по умолчанию 10).
    - `_hash(self, value)`: простая хэш-функция, которая вычисляет индекс для данного значения.
    - `add(self, value)`: добавляет значение в множество, если его там еще нет.
    - `remove(self, value)`: удаляет значение из множества, если оно присутствует.
    - `contains(self, value)`: возвращает `True`, если значение присутствует в множестве, иначе — `False`.
    - `elements(self)`: возвращает список всех элементов в множестве.

```python
class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
	    pass
	    
    def add(self, value):
	    pass
	    
    def remove(self, value):
	    pass
	    
    def contains(self, value):
	    pass
	    
    def elements(self):
	    pass
		
my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())
```



## 6. Binary Tree

Вам необходимо реализовать класс для представления узла бинарного дерева и само бинарное дерево. Бинарное дерево — это структура данных, в которой каждый узел может иметь не более двух дочерних узлов, обычно называемых левым и правым.

1. **Класс `TreeNode`**:
    - Реализуйте класс `TreeNode`, который будет представлять узел бинарного дерева. Узел должен содержать:
        - `data`: данные узла (может быть любого типа).
        - `left`: ссылка на левое дочернее узло (по умолчанию `None`).
        - `right`: ссылка на правое дочернее узло (по умолчанию `None`).
2. **Класс `BinaryTree`**:
    
    - Реализуйте класс `BinaryTree`, который будет предоставлять методы для работы с бинарным деревом:
        - `insert(data)`: добавляет новый узел в дерево.
        - `search(data)`: ищет узел с заданными данными и возвращает его, если он найден, или `None`, если не найден.
        - `in_order_traversal()`: выполняет обход дерева в симметричном порядке (левое, корень, правое).
        - `pre_order_traversal()`: выполняет обход дерева в префиксном порядке (корень, левое, правое).
        - `post_order_traversal()`: выполняет обход дерева в постфиксном порядке (левое, правое, корень).

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
	    pass

    def search(self, data):
	    pass

    def in_order_traversal(self):
	    pass

    def pre_order_traversal(self):
	    pass

    def post_order_traversal(self):
	    pass


# Пример использования
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(tree.search(20))  # Ожидаемый вывод: None

print(tree.in_order_traversal())  # Ожидаемый вывод: [5, 10, 15]
print(tree.pre_order_traversal())  # Ожидаемый вывод: [10, 5, 15]
print(tree.post_order_traversal())  # Ожидаемый вывод: [5, 15, 10]

```


## 7. Hashmap

Вам необходимо реализовать класс `HashMap`, который будет представлять собой хэш-таблицу. Хэш-таблица — это структура данных, которая обеспечивает эффективный доступ к данным, используя хэш-функцию для вычисления индексов.

1. **Класс `HashMap`**:
    - Реализуйте класс `HashMap`, который будет содержать следующие методы:
        - `__init__(self, size=10)`: инициализирует хэш-таблицу заданного размера.
        - `_hash(self, key)`: принимает ключ и возвращает индекс для хранения.
        - `put(self, key, value)`: добавляет новую пару ключ-значение в хэш-таблицу.
        - `get(self, key, default=None)`: возвращает значение, соответствующее ключу, или значение по умолчанию, если ключ не найден.
        - `remove(self, key)`: удаляет пару ключ-значение из хэш-таблицы.
        - `keys(self)`: возвращает список всех ключей в хэш-таблице.
        - `values(self)`: возвращает список всех значений в хэш-таблице.
        - `items(self)`: возвращает список всех пар ключ-значение в хэш-таблице.

```python
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        # A simple hash function using the length of the key
	    pass

    def put(self, key, value):
        hash_value = self._hash(key)
		# your code
	    pass
		
    def get(self, key, default=None):
		# your code
	    pass

    def remove(self, key):
		# your code
	    pass

    def keys(self):
		# your code
	    pass

    def values(self):
		# your code
	    pass
	    
    def items(self):
	    # your code
	    pass

# Пример использования 
my_hashmap = HashMap() 
my_hashmap.put("name", "John") 
my_hashmap.put("age", 25) 
my_hashmap.put("city", "Example City") 
print("Keys:", my_hashmap.keys()) # Ожидаемый вывод: Keys: ['name', 'age', 'city'] 
print("Values:", my_hashmap.values()) # Ожидаемый вывод: Values: ['John', 25, 'Example City'] 
print("Items:", my_hashmap.items()) # Ожидаемый вывод: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')] 

# Доступ к значениям по ключу 
print("Name:", my_hashmap.get("name")) # Ожидаемый вывод: Name: John
print("Gender:", my_hashmap.get("gender", "Not specified")) # Ожидаемый вывод: Gender: Not specified 

# Удаление пары ключ-значение 
my_hashmap.remove("age") 
print("Keys after removing 'age':", my_hashmap.keys()) # Ожидаемый вывод: Keys after removing 'age': ['name', 'city']
```
## 8. Map

Вам необходимо реализовать класс `SimpleMap`, который будет представлять собой простую ассоциативную коллекцию данных (или словарь). `SimpleMap` должен предоставлять основные методы для работы с ключами и значениями.

**Класс `SimpleMap`**:
- Реализуйте класс `SimpleMap`, который будет содержать следующие методы:
    - `__init__(self)`: инициализирует пустой список для хранения элементов.
    - `set(self, key, value)`: добавляет новую пару ключ-значение в коллекцию.
    - `get(self, key, default=None)`: возвращает значение, соответствующее ключу, или значение по умолчанию, если ключ не найден.
    - `remove(self, key)`: удаляет пару ключ-значение из коллекции.
    - `keys(self)`: возвращает список всех ключей в коллекции.
    - `values(self)`: возвращает список всех значений в коллекции.
    - `items(self)`: возвращает список всех пар ключ-значение в коллекции.

```python

class SimpleMap:
    def __init__(self):
        self.items = []

    def set(self, key, value):
	    pass
	    
    def get(self, key, default=None):
	    pass
	    
    def remove(self, key):
	    pass
	    
    def keys(self):
	    pass
	    
    def values(self):
	    pass
	    
    def items(self):
	    pass

# Example usage:
my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
```

## 9. Heap

Вам необходимо реализовать простую кучу (heap) на языке Python. Куча — это специализированная структура данных, которая удовлетворяет свойству кучи: в случае максимальной кучи, для любого узла `N` значение узла всегда больше или равно значениям его дочерних узлов. В случае минимальной кучи — наоборот.

**Класс `Heap`**:

- Реализуйте класс `Heap`, который будет содержать следующие методы:
    - `__init__(self, max_heap=True)`: инициализирует пустую кучу. Аргумент `max_heap` определяет, будет ли это максимальная куча или минимальная.
    - `insert(self, value)`: добавляет элемент в кучу.
    - `extract(self)`: удаляет и возвращает корень кучи (наибольший или наименьший элемент в зависимости от типа кучи).
    - `peek(self)`: возвращает корень кучи, не удаляя его.
    - `is_empty(self)`: возвращает `True`, если куча пуста, иначе — `False`.
    - `size(self)`: возвращает количество элементов в куче.
    - `_heapify_up(self, index)`: восстанавливает свойства кучи, поднимая элемент вверх.
    - `_heapify_down(self, index)`: восстанавливает свойства кучи, опуская элемент вниз.

```python
class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
	    pass

    def size(self):
	    pass

    def insert(self, value):
	    pass

    def extract(self):
	    pass

    def peek(self):
	    pass

    def _heapify_up(self, index):
	    pass

    def _heapify_down(self, index):
	    pass

# Пример использования
h = Heap(max_heap=True)  # Создаем максимальную кучу

# Вставка элементов
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

# Извлечение корней
while not h.is_empty():
	print("Извлеченный элемент:", h.extract())

```

## 10. Двухсвязный список

Вам необходимо реализовать класс для представления узла двухсвязного списка и сам двухсвязный список. Двухсвязный список — это структура данных, в которой каждый узел содержит данные и ссылки на следующий и предыдущий узлы.

- **Класс `Node`**:

    - Реализуйте класс `Node`, который будет представлять узел двухсвязного списка. Узел должен содержать:
        - `data`: данные узла (может быть любого типа).
        - `next`: ссылка на следующий узел (по умолчанию `None`).
        - `prev`: ссылка на предыдущий узел (по умолчанию `None`).
- **Класс `DoublyLinkedList`**:
    
    - Реализуйте класс `DoublyLinkedList`, который будет предоставлять методы для работы с двухсвязным списком:
        - `append(data)`: добавляет новый узел в конец списка.
        - `prepend(data)`: добавляет новый узел в начало списка.
        - `delete(data)`: удаляет первый узел, содержащий заданные данные.
        - `display()`: выводит элементы списка от начала до конца.
        - `display_reverse()`: выводит элементы списка от конца до начала.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
	    pass

    def prepend(self, data):
	    pass

    def delete(self, data):
	    pass

    def display(self):
	    pass

    def display_reverse(self):
	    pass
	    
# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # Ожидаемый вывод: 1 <-> 2 <-> 3 <-> None

dll.prepend(0)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 2 <-> 3 <-> None

dll.delete(2)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 3 <-> None

dll.display_reverse()  # Ожидаемый вывод: 3 <-> 1 <-> 0 <-> None
```

## 11. Реализация сбалансированного дерева (AVL-дерево)

Вам необходимо реализовать класс для представления узла сбалансированного дерева (AVL-дерево) и само AVL-дерево. AVL-дерево — это самобалансирующееся бинарное дерево поиска, в котором разница высот левого и правого поддеревьев любого узла не превышает 1.

- **Класс `AVLNode`**:
    - Реализуйте класс `AVLNode`, который будет представлять узел AVL-дерева. Узел должен содержать:
        - `data`: данные узла (может быть любого типа).
        - `height`: высота узла (по умолчанию `1`).
        - `left`: ссылка на левый дочерний узел (по умолчанию `None`).
        - `right`: ссылка на правый дочерний узел (по умолчанию `None`).
- **Класс `AVLTree`**:
    - Реализуйте класс `AVLTree`, который будет предоставлять методы для работы с AVL-деревом:
        - `insert(data)`: добавляет новый узел в дерево и выполняет балансировку.
        - `delete(data)`: удаляет узел с заданными данными и выполняет балансировку.
        - `search(data)`: ищет узел с заданными данными и возвращает его, если он найден, или `None`, если не найден.
        - `in_order_traversal()`: выполняет обход дерева в симметричном порядке.

```python
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, data):
	    pass

    def delete(self, root, data):
	    pass

    def rotate_left(self, z):
	    pass

    def rotate_right(self, z):
	    pass

    def get_height(self, node):
	    pass

    def get_balance(self, node):
	    pass

	def get_min_value_node(self, node):
	    pass
	    
    def in_order_traversal(self, root):
		pass

# Пример использования
avl_tree = AVLTree()
root = None
root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)

print(avl_tree.in_order_traversal(root))  # Ожидаемый вывод: [10, 20, 30]

```

## 12. Приоритетная Очередь

Вам необходимо реализовать приоритетную очередь с использованием собственного алгоритма. Эта очередь будет хранить элементы с приоритетами и обеспечивать доступ к элементам с наивысшим приоритетом.

**Класс `PriorityQueue`**:

- Реализуйте класс `PriorityQueue`, который будет содержать следующие методы:
    - `__init__(self)`: инициализирует пустую приоритетную очередь.
    - `push(self, item, priority)`: добавляет элемент с заданным приоритетом в очередь.
    - `pop(self)`: удаляет и возвращает элемент с наивысшим приоритетом.
    - `peek(self)`: возвращает элемент с наивысшим приоритетом, не удаляя его.
    - `is_empty(self)`: возвращает `True`, если очередь пуста, иначе — `False`.
    - `size(self)`: возвращает количество элементов в очереди.

```python
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
		pass

    def push(self, item, priority):
		pass

    def pop(self):
		pass

    def peek(self):
		pass

    def size(self):
		pass
		
pq = PriorityQueue()

pq.push("Задача 1", priority=2)
pq.push("Задача 2", priority=5)
pq.push("Задача 3", priority=1)

print("Первый элемент с наивысшим приоритетом:", pq.peek())  # Ожидаемый вывод: Задача 3

while not pq.is_empty():
    print("Обработка:", pq.pop())

```

## 13. Binary Tree 2

Вам необходимо реализовать класс для представления узла бинарного дерева поиска и само бинарное дерево поиска. Бинарное дерево поиска — это структура данных, в которой каждый узел содержит ключ, и для любого узла все ключи в левом поддереве меньше, чем ключ узла, а все ключи в правом поддереве больше.

- **Класс `TreeNode`**:
    
    - Реализуйте класс `TreeNode`, который будет представлять узел бинарного дерева. Узел должен содержать:
        - `data`: данные узла (может быть любого типа).
        - `left`: ссылка на левый дочерний узел (по умолчанию `None`).
        - `right`: ссылка на правый дочерний узел (по умолчанию `None`).
- **Класс `BinarySearchTree`**:
    
    - Реализуйте класс `BinarySearchTree`, который будет предоставлять методы для работы с BST:
        - `insert(data)`: добавляет новый узел в дерево.
        - `delete(data)`: удаляет узел с заданными данными.
        - `search(data)`: ищет узел с заданными данными и возвращает его, если он найден, или `None`, если не найден.
        - `in_order_traversal()`: выполняет обход дерева в симметричном порядке.

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
	    pass
    
	def delete(self, data):
	    pass

    def get_min_value_node(self, node):
	    pass

    def search(self, data):
	    pass

    def in_order_traversal(self):
	    pass

# Пример использования
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)

print(bst.in_order_traversal())  # Ожидаемый вывод: [3, 5, 10, 15]

bst.delete(5)
print(bst.in_order_traversal())  # Ожидаемый вывод: [3, 10, 15]

print(bst.search(10))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(bst.search(20))  # Ожидаемый вывод: None
```

## 14. `swap`

Реализуйте функцию `swap_nodes` для односвязного списка, которая **меняет местами** два узла по заданным индексам в **разных** списках.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def linked_list(*values):
	pass
	
def print_linked_list(linked_list):
	pass
	
def swap_nodes(list_pointer1, index1, list_pointer2, index2):
	pass
	
def get_node_and_prev(linked_list, index):
	pass

# Example usage
list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  # Output: True

print_linked_list(list1)
# Output: 1 -> 2 -> 5 -> 4 -> None

print_linked_list(list2)
# Output: 3 -> 6 -> 7 -> 8 -> None

list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  # Output: False

print_linked_list(list1)
# Output: 1 -> 2 -> 3 -> None

print_linked_list(list2)
# Output: 4 -> 5 -> 6 -> None
```


## 15. `reduce`

Вам необходимо реализовать класс, представляющий узел связного списка, и функцию, которая будет аккумулировать значения элементов списка с помощью переданной функции.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reduce(head, func, initial_value):
		pass

def add(acc, curr):
    return acc + curr

list1 = Node(1, Node(2, Node(3)))
result1 = reduce(list1, add, 0)
print(result1)  # Output: 6

def multiply(acc, curr):
    return acc * curr

list2 = Node(1, Node(2, Node(3, Node(4))))
result2 = reduce(list2, multiply, 1)
print(result2)  # Output: 24

```

## 16. Получить N-й 

Вам нужно реализовать класс, представляющий узел связного списка, а также функцию, которая возвращает N-й элемент списка по заданному индексу.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(head, index):
	pass

list1 = Node(1, Node(2, Node(3)))
result1 = get_nth(list1, 0)
print(result1.data)  # Ожидаемый вывод: 1

list2 = Node(1, Node(2, Node(3, None)))
result2 = get_nth(list2, 2)
print(result2.data)  # Ожидаемый вывод: 3

try:
    get_nth(list2, 5)
except ValueError as e:
    print(e)  # Ожидаемый вывод: Index out of range

try:
    get_nth(None, 0)
except ValueError as e:
    print(e)  # Ожидаемый вывод: Invalid index or empty list
```

##  17. `length` и `count` 

Вам необходимо реализовать класс для представления узла связного списка и две функции, которые будут работать с этим списком: одна для вычисления длины списка, а другая для подсчета количества вхождений определённого значения.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(head):
	pass

def count(head, value):
	pass


list1 = Node(1, Node(2, Node(3)))
result_length = length(list1)
print(result_length)  # Output: 3


result_count = count(list1, 1)
print(result_count)  # Output: 1


list2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3)))))))))
result_count_2 = count(list2, 2)
print(result_count_2)  # Output: 4
```
## 18. `map` 

Вам необходимо реализовать класс для представления узла связного списка и функцию, которая будет применять заданную функцию к каждому элементу этого списка, создавая новый связный список с результатами.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def map_linked_list(head, mapping_function):
	pass

# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a mapping function: x => x * 2
def mapping_function(x):
    return x * 2

# Apply the map method
mapped_list = map_linked_list(original_list, mapping_function)

# Print the result
current = mapped_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 4 -> 6 ->

```

## 20. `filter` 

Вам необходимо реализовать класс для представления узла связного списка и функцию, которая будет фильтровать элементы списка на основе заданного предиката. Функция должна создавать новый связный список, содержащий только те элементы, которые соответствуют условию предиката.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def filter_linked_list(head, predicate_function):
	pass

# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a predicate function: x => x >= 2
def predicate_function(x):
    return x >= 2

# Apply the filter method
filtered_list = filter_linked_list(original_list, predicate_function)

# Print the result
current = filtered_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 3 ->
```

