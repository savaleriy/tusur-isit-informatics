# Python: классы и объекты

Инструменты этого занятия: классы, атрибуты объекта и класса, свойства, методы класса, специальные методы, наследование и абстрактные классы, модуль `copy` и исключения.

Всё, что было в предыдущих занятиях, считается известным: функции, списки, словари, f-строки, `lambda` и `sorted` с ключом.

---

## Класс за одну минуту

```python
class Counter:
    def __init__(self, start=0):     # конструктор: вызывается при создании объекта
        self.value = start           # атрибут объекта

    def add(self, step=1):           # метод: первый параметр всегда self
        self.value += step


c = Counter()
c.add()
c.add(5)
c.value          # 6
Counter(10).value  # 10
```

- `self` - ссылка на объект, с которым работает метод. Python подставляет его сам: `c.add(5)` - это `Counter.add(c, 5)`.
- Атрибуты объекта создаются присваиванием `self.имя = ...`. Хорошая привычка - заводить все атрибуты в `__init__`, чтобы по нему было видно, из чего состоит объект.
- Значения по умолчанию у параметров конструктора заменяют несколько конструкторов: перегрузки функций, как в C++, в Python нет.

## Атрибуты объекта и атрибуты класса

Атрибут, объявленный прямо в теле класса, принадлежит **классу** и общий для всех объектов:

```python
class Circle:
    count = 0                        # атрибут класса

    def __init__(self, r):
        self.r = r                   # атрибут объекта
        Circle.count += 1


a = Circle(1)
b = Circle(2)
Circle.count     # 2
a.count          # 2 - объект видит атрибут класса
```

Атрибуты класса хороши для констант и общих счётчиков. А вот изменяемое значение в атрибуте класса - классическая ловушка:

```python
class Basket:
    items = []                       # один список на ВСЕ корзины!

    def add(self, item):
        self.items.append(item)


a = Basket()
b = Basket()
a.add("яблоко")
b.items          # ['яблоко'] - корзины делят один список
```

Список, который должен быть у каждого объекта свой, создавайте в `__init__`: `self.items = []`.

## Методы класса и статические методы

Иногда объект удобно создавать разными способами. Конструктор один, но можно добавить **альтернативные конструкторы** - методы класса:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

    @classmethod
    def origin(cls):
        return cls(0, 0)

    @staticmethod
    def is_valid(x, y):
        return isinstance(x, (int, float)) and isinstance(y, (int, float))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


Point.from_tuple((3, 4))   # Point(3, 4)
Point.origin()             # Point(0, 0)
Point.is_valid(1, "a")     # False
```

- `@classmethod` получает первым параметром не объект, а сам класс (`cls`). Вызывать его принято через класс: `Point.origin()`.
- `@staticmethod` не получает ни объекта, ни класса - это обычная функция, которую положили внутрь класса, потому что по смыслу она к нему относится.

## Свойства

`@property` превращает метод в атрибут для чтения, `@имя.setter` - перехватывает присваивание:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius            # пойдёт через сеттер

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):                 # вычисляемое свойство, только для чтения
        return self._celsius * 9 / 5 + 32


t = Temperature(100)
t.fahrenheit     # 212.0
t.celsius = -300 # ValueError: ниже абсолютного нуля
t.fahrenheit = 0 # AttributeError
```

Внутри сеттера пишите в `self._celsius`, а не в `self.celsius`: присваивание `self.celsius = ...` снова вызовет сеттер, тот вызовет себя ещё раз - и так до `RecursionError`.

## Специальные методы

Специальные методы вызывает сам Python, когда встречает оператор или встроенную функцию.

| Метод | Когда вызывается | Что вернуть |
| - | - | - |
| `__init__(self, ...)` | `X(...)` | ничего |
| `__repr__(self)` | `repr(x)`, объект внутри списка, интерактивная консоль | строку для программиста |
| `__str__(self)` | `str(x)`, `print(x)`, f-строка | строку для пользователя |
| `__eq__(self, other)` | `x == y` (и `x != y`, если нет `__ne__`) | `True` или `False` |
| `__lt__(self, other)` | `x < y`, а также `sorted`, `min`, `max` | `True` или `False` |
| `__le__`, `__gt__`, `__ge__` | `x <= y`, `x > y`, `x >= y` | `True` или `False` |
| `__add__(self, other)` | `x + y` | новый объект |
| `__sub__`, `__mul__`, `__truediv__` | `x - y`, `x * y`, `x / y` | новый объект |
| `__neg__(self)` | `-x` | новый объект |
| `__abs__(self)` | `abs(x)` | число |
| `__len__(self)` | `len(x)` | целое число |
| `__bool__(self)` | `if x:`, `bool(x)` | `True` или `False` |
| `__contains__(self, item)` | `item in x` | `True` или `False` |
| `__getitem__(self, key)` | `x[key]` | элемент |
| `__iter__(self)` | `for item in x` | итератор, например `iter(self._items)` |
| `__call__(self, ...)` | `x(...)` | что угодно |
| `__hash__(self)` | ключ словаря, элемент множества | целое число |

Пример - вектор на плоскости:

```python
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}; {self.y})"


v = Vector(1, 2) + Vector(2, 2)
v                        # Vector(3, 4)
abs(v)                   # 5.0
v * 2                    # Vector(6, 8)
v == Vector(3, 4)        # True
v == "вектор"            # False
print(v)                 # (3; 4)
```

Арифметические методы **не меняют** объект, а возвращают новый - как `+` для чисел не меняет слагаемые.

Если `other` - объект неподходящего типа, верните специальное значение `NotImplemented`. Тогда Python попробует спросить второй операнд, а если и тот не умеет, `==` вернёт `False`, а `+` поднимет понятный `TypeError`.

### Равенство и хеш

Объявив `__eq__`, вы теряете возможность класть объекты в множество и использовать их как ключи словаря:

```python
{Vector(1, 2)}   # TypeError: unhashable type: 'Vector'
```

Вспомните второе занятие: ключом словаря может быть только неизменяемое значение. Python рассуждает так: раз объекты сравниваются по содержимому, а содержимое можно поменять, хешировать такой объект опасно. Если объекты вашего класса после создания не меняются, разрешите хеширование явно - хешем от тех же полей, что сравниваются в `__eq__`:

```python
class Vector:
    ...

    def __hash__(self):
        return hash((self.x, self.y))
```

```python
{Vector(1, 2), Vector(1, 2)}   # {Vector(1, 2)}
```

Правило одно: если `a == b`, то обязательно `hash(a) == hash(b)`. Иначе множество и словарь перестанут находить ваши объекты.

## Наследование

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} - животное"


class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name)           # родитель заполняет свою часть
        self.indoor = indoor

    def describe(self):                  # переопределение
        return super().describe() + ", кошка"


tom = Cat("Том", indoor=True)
tom.describe()               # 'Том - животное, кошка'
isinstance(tom, Animal)      # True
issubclass(Cat, Animal)      # True
type(tom) == Animal          # False
```

- `super()` - доступ к методам родителя. В конструкторе наследника вызов `super().__init__(...)` почти всегда нужен.
- Проверяйте тип через `isinstance`, а не `type(x) == X`: `isinstance` учитывает наследников, а сравнение типов - нет.
- Все классы в Python неявно наследуют `object`. Оттуда приходят стандартные `__repr__` с адресом в памяти и `__eq__`, сравнивающий объекты через `is`.

## Абстрактные классы

```python
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def choose_move(self, state):
        """Вернуть ход по состоянию игры."""


class FirstMovePlayer(Player):
    def choose_move(self, state):
        return state[0]


FirstMovePlayer("бот").choose_move([3, 1, 2])   # 3
Player("никто")                                 # TypeError
```

- Абстрактный класс наследует `ABC`, абстрактные методы помечаются `@abstractmethod`.
- Создать объект можно только у наследника, который реализовал все абстрактные методы.
- Тело абстрактного метода может быть пустым (`pass`) или состоять из одной строки документации, как выше.

## Ссылки и копии

```python
a = [1, 2]
b = a
b is a           # True - одно и то же
a == [1, 2]      # True - равно по содержимому
a is [1, 2]      # False - но это другой объект
```

`is` сравнивает объекты, `==` - содержимое. `is` используют почти только для `None`: `if result is None:`.

```python
import copy

grid = [[0, 0], [0, 0]]
shallow = copy.copy(grid)        # новый внешний список, строки - общие
deep = copy.deepcopy(grid)       # всё новое
grid[0][0] = 1
shallow[0][0]    # 1
deep[0][0]       # 0
```

### Изменяемое значение по умолчанию

Значение по умолчанию вычисляется **один раз** - когда Python читает `def`, а не при каждом вызове. Если это список, он будет общим для всех вызовов:

```python
class Team:
    def __init__(self, members=[]):    # ошибка!
        self.members = members


a = Team()
b = Team()
a.members.append("Аня")
b.members        # ['Аня'] - у двух команд один список
```

Правильно - `None` по умолчанию и новый список внутри:

```python
class Team:
    def __init__(self, members=None):
        if members is None:
            members = []
        self.members = members
```

## Исключения

Когда операция невозможна, о ней надо сообщить громко - поднять исключение:

```python
def sqrt_int(n):
    if n < 0:
        raise ValueError("корень из отрицательного числа")
    return int(n ** 0.5)
```

`raise` немедленно прерывает выполнение функции. Вызывающий код может поймать исключение и обработать его:

```python
try:
    sqrt_int(-4)
except ValueError as e:
    print("не получилось:", e)   # не получилось: корень из отрицательного числа
```

Если в `try` что-то пошло не так, выполнение переходит в подходящий `except`. Если исключение никто не поймал, программа падает и печатает его.

| Исключение | Когда поднимают |
| - | - |
| `ValueError` | значение подходящего типа, но недопустимое: отрицательный радиус, нехватка денег |
| `TypeError` | значение не того типа: в зоопарк добавили строку |
| `IndexError` | обращение по несуществующему индексу, `pop` из пустого списка |
| `KeyError` | нет такого ключа |
| `AttributeError` | у объекта нет такого атрибута |
| `NotImplementedError` | метод должен быть реализован в наследнике |

### Свои исключения

Исключения - тоже классы, и от них можно наследоваться. Собственное исключение делает ошибку узнаваемой:

```python
class InsufficientFunds(ValueError):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"на счёте {balance}, а снимают {amount}")
    return balance - amount


try:
    withdraw(100, 500)
except ValueError as e:
    print(type(e).__name__, e)   # InsufficientFunds на счёте 100, а снимают 500
```

Поскольку `InsufficientFunds` наследует `ValueError`, его ловит и `except InsufficientFunds`, и `except ValueError`. Это то же отношение "является", что и у фигур: нехватка денег *является* ошибкой значения.

---

## Для любопытных: `@dataclass`

Классы, которые в основном хранят данные, требуют однообразного кода: `__init__`, `__repr__`, `__eq__`. Декоратор `@dataclass` пишет его за вас по списку полей:

```python
from dataclasses import dataclass


@dataclass
class Card:
    color: str
    value: int


Card("red", 5)                       # Card(color='red', value=5)
Card("red", 5) == Card("red", 5)     # True
```

Запись `color: str` - **аннотация типа**: подсказка для читателя и редактора кода. Python её не проверяет, но `@dataclass` по аннотациям узнаёт, какие поля бывают у объекта. Пригодится в лабораторных; в задачах этого занятия пишите классы руками - так вы поймёте, что именно генерирует декоратор.

## Для любопытных: множественное наследование

Класс может наследовать сразу нескольким родителям:

```python
class Computer:
    def turn_on(self):
        return "компьютер включён"


class Monitor:
    def show(self):
        return "изображение на экране"


class Laptop(Computer, Monitor):
    pass


Laptop().turn_on()   # 'компьютер включён'
Laptop().show()      # 'изображение на экране'
```

Если у родителей есть методы с одинаковыми именами, Python ищет метод в строго определённом порядке - **порядке разрешения методов** (MRO). Посмотреть его можно атрибутом `__mro__`:

```python
class Device:
    def turn_on(self):
        return "устройство включено"


class Phone(Device):
    def turn_on(self):
        return "телефон включён"


class Camera(Device):
    def turn_on(self):
        return "камера включена"


class Smartphone(Phone, Camera):
    pass


Smartphone().turn_on()                          # 'телефон включён'
[c.__name__ for c in Smartphone.__mro__]        # ['Smartphone', 'Phone', 'Camera', 'Device', 'object']
```

Это и есть знаменитая "проблема ромба": `Smartphone` получает `turn_on` и от `Phone`, и от `Camera`, а оба они - от `Device`. В C++ такой вызов не скомпилируется, и программист решает конфликт сам. Python выбирает по MRO: сначала сам класс, потом родители слева направо, общий предок - в самом конце.

На практике множественное наследование используют осторожно: чаще всего, чтобы класс реализовал несколько интерфейсов сразу (`class ElectricCar(Car, Serviceable)`). Если начинаете путаться в MRO - это сигнал, что пора перейти на композицию.

## Для любопытных: а где деструктор?

В C++ момент уничтожения объекта известен точно: локальный объект уничтожается при выходе из блока, а созданный через `new` - при вызове `delete`. Тогда же вызывается деструктор и освобождает ресурсы объекта. В Python памятью управляет сам интерпретатор: объект удаляется, когда на него не остаётся ни одного ярлыка. Метод `__del__` существует, но *когда* он вызовется, не гарантировано, поэтому полагаться на него нельзя. Если ресурс - файл, соединение - нужно освободить вовремя, используют `with`, как при чтении файлов.

---

## Типичные ошибки этого занятия

| Ошибка | Причина |
| - | - |
| `TypeError: Circle.__init__() takes 2 positional arguments but 3 were given` | забыли `self` в объявлении метода |
| `TypeError: Circle.area() missing 1 required positional argument: 'self'` | вызвали метод у класса, а не у объекта: `Circle.area()` вместо `Circle(0, 0, 1).area()` |
| `<__main__.Circle object at 0x7f...>` | не определён `__repr__` |
| `AttributeError: 'Circle' object has no attribute 'x'` | опечатка в имени атрибута, атрибут не задан в `__init__` или наследник не вызвал `super().__init__` |
| `RecursionError` в свойстве | в сеттере написали `self.r = value` вместо `self._r = value` |
| список "перепутался" между объектами | изменяемый атрибут класса или изменяемое значение по умолчанию |
| `TypeError: unhashable type` | определили `__eq__`, но не `__hash__` |
| `TypeError: Can't instantiate abstract class` | наследник реализовал не все абстрактные методы |
| метод молча ничего не делает | забыли `raise` в ветке, где операция невозможна |

---

## Что дальше

Переходите к [задачам занятия](task.md). Пять обязательных встроены в [конспект](note.md), балльные отсортированы по возрастанию сложности.
