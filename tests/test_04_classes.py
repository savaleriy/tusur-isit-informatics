"""Занятие 4.1. Классы и ООП.

Задачи 1-5 - обязательные, они встроены в конспект (docs/04-classes/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import datetime
import inspect
import math
import random

import pytest


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


def test_01_account_basic(solution):
    Account = solution("account", "Account")
    acc = Account("40817", "Иван", 1000)
    assert (acc.number, acc.owner, acc.balance) == ("40817", "Иван", 1000)
    acc.deposit(500)
    assert acc.balance == 1500
    acc.withdraw(200)
    assert acc.balance == 1300
    assert repr(acc) == "Account('40817', 'Иван', 1300)"
    assert Account("1", "Мария").balance == 0


def test_01_account_errors(solution):
    Account = solution("account", "Account")
    with pytest.raises(ValueError):
        Account("1", "Иван", -10)
    acc = Account("1", "Иван", 100)
    for bad in (0, -50):
        with pytest.raises(ValueError):
            acc.deposit(bad)
        with pytest.raises(ValueError):
            acc.withdraw(bad)
    with pytest.raises(ValueError):
        acc.withdraw(101)
    assert acc.balance == 100          # неудачные операции ничего не меняют
    acc.withdraw(100)
    assert acc.balance == 0


def test_02_book_borrow(solution):
    Book = solution("book", "Book")
    b = Book("1984", "Оруэлл", "123", 1949, 328)
    assert (b.title, b.author, b.isbn, b.year, b.pages) == ("1984", "Оруэлл", "123", 1949, 328)
    assert b.is_available is True
    assert b.last_read_pages == 0
    with pytest.raises(ValueError):
        b.give_back(10)                # книга и так на полке
    b.borrow()
    assert b.is_available is False
    with pytest.raises(ValueError):
        b.borrow()
    with pytest.raises(AttributeError):
        b.is_available = True
    for bad in (-1, 329):
        with pytest.raises(ValueError):
            b.give_back(bad)
    assert b.is_available is False     # неудачный возврат ничего не меняет
    assert b.last_read_pages == 0
    b.give_back(120)
    assert b.is_available is True
    assert b.last_read_pages == 120
    with pytest.raises(AttributeError):
        b.last_read_pages = 328
    b.borrow()
    b.give_back(328)                   # граница: прочитана целиком
    assert b.last_read_pages == 328
    with pytest.raises(ValueError):
        Book("Пустая", "Никто", "000", 2000, 0)


def test_02_book_compare(solution):
    Book = solution("book", "Book")
    b = Book("1984", "Оруэлл", "123", 1949, 328)
    assert b == Book("1984", "Оруэлл", "123", 1949, 328)
    assert b == Book("Другое издание", "Оруэлл", "123", 2020, 400)   # важен только ISBN
    assert b != Book("1984", "Оруэлл", "999", 1949, 328)
    old = Book("Мы", "Замятин", "456", 1924, 224)
    new = Book("Generation П", "Пелевин", "789", 1999, 320)
    assert sorted([new, b, old]) == [old, b, new]
    assert repr(b) == "Book('1984', 'Оруэлл', '123', 1949, 328)"


def test_03_library_lend(solution):
    Book = solution("library", "Book")
    Reader = solution("library", "Reader")
    Library = solution("library", "Library")
    lib = Library()
    assert len(lib) == 0
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    lib.add_book(Book("Мы", "Замятин", "456", 1924, 224))
    alice = Reader("Алиса")
    assert alice.books == []
    assert alice.pages_read == 0

    lib.lend("123", alice)
    assert len(alice.books) == 1
    assert alice.books[0] is lib.find_by_isbn("123")      # тот же объект, не копия
    assert lib.find_by_isbn("123").is_available is False
    assert [b.isbn for b in lib.available()] == ["124", "456"]

    lib.take_back("123", alice, 100)
    assert alice.books == []
    assert alice.pages_read == 100
    assert lib.find_by_isbn("123").is_available is True
    assert lib.find_by_isbn("123").last_read_pages == 100
    assert len(lib) == 3


def test_03_library_pages(solution):
    Book = solution("library", "Book")
    Reader = solution("library", "Reader")
    Library = solution("library", "Library")
    lib = Library()
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    lib.add_book(Book("Мы", "Замятин", "456", 1924, 224))
    alice, bob = Reader("Алиса"), Reader("Боб")
    assert lib.unfinished() == []

    lib.lend("123", alice)
    with pytest.raises(ValueError):
        lib.take_back("123", alice, 500)       # столько страниц в книге нет
    assert len(alice.books) == 1               # ничего не изменилось
    assert alice.pages_read == 0
    assert lib.find_by_isbn("123").is_available is False

    lib.take_back("123", alice, 100)
    lib.lend("124", alice)
    lib.take_back("124", alice, 112)           # дочитала
    lib.lend("456", bob)
    lib.take_back("456", bob, 0)               # даже не открыл
    assert alice.pages_read == 212
    assert bob.pages_read == 0
    assert [b.isbn for b in lib.unfinished()] == ["123"]

    lib.lend("123", bob)                       # второй читатель дочитал 1984
    lib.take_back("123", bob, 328)
    assert lib.unfinished() == []
    assert bob.pages_read == 328


def test_03_library_search_and_errors(solution):
    Book = solution("library", "Book")
    Reader = solution("library", "Reader")
    Library = solution("library", "Library")
    lib = Library()
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Мы", "Замятин", "456", 1924, 224))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    assert [b.isbn for b in lib.find_by_author("Оруэлл")] == ["123", "124"]
    assert lib.find_by_author("Толстой") == []
    assert lib.find_by_isbn("000") is None

    alice, bob = Reader("Алиса"), Reader("Боб")
    with pytest.raises(KeyError):
        lib.lend("000", alice)
    lib.lend("456", alice)
    with pytest.raises(ValueError):
        lib.lend("456", bob)
    assert bob.books == []
    with pytest.raises(ValueError):
        lib.take_back("456", bob, 10)
    assert len(alice.books) == 1


def test_04_bank_savings(solution):
    Account = solution("bank", "Account")
    SavingsAccount = solution("bank", "SavingsAccount")
    assert issubclass(SavingsAccount, Account)
    s = SavingsAccount("1", "Иван", 1000, rate=0.1)
    s.add_interest()
    assert s.balance == pytest.approx(1100)
    with pytest.raises(ValueError):
        s.withdraw(2000)
    with pytest.raises(AttributeError):
        s.balance = 0
    assert s.balance == pytest.approx(1100)
    assert repr(s) == "SavingsAccount('1', 'Иван', 1100.0, 0.1)"
    assert SavingsAccount("2", "Мария").rate == 0.05
    s.deposit(100)
    assert s.balance == pytest.approx(1200)


def test_04_bank_checking(solution):
    Account = solution("bank", "Account")
    CheckingAccount = solution("bank", "CheckingAccount")
    assert issubclass(CheckingAccount, Account)
    assert CheckingAccount.deposit is Account.deposit       # deposit унаследован
    c = CheckingAccount("2", "Мария", 100, overdraft=500)
    c.withdraw(400)
    assert c.balance == -300
    with pytest.raises(ValueError):
        c.withdraw(300)
    assert c.balance == -300
    c.withdraw(200)                    # ровно до -overdraft можно
    assert c.balance == -500
    with pytest.raises(ValueError):
        c.withdraw(-5)
    c.deposit(1200)
    assert c.balance == 700
    assert repr(c) == "CheckingAccount('2', 'Мария', 700, 500)"
    with pytest.raises(ValueError):
        CheckingAccount("3", "Пётр").withdraw(1)   # овердрафт по умолчанию 0


def test_05_zoo_basic(solution):
    Lion = solution("zoo", "Lion")
    Parrot = solution("zoo", "Parrot")
    Zoo = solution("zoo", "Zoo")
    zoo = Zoo()
    assert len(zoo) == 0
    assert zoo.total_food() == 0
    simba = Lion("Симба", 190)
    zoo.add(simba)
    zoo.add(Parrot("Кеша", 0.5))
    assert len(zoo) == 2
    assert zoo.sounds() == ["Симба: Р-р-р", "Кеша: Привет!"]
    assert zoo.total_food() == pytest.approx(9.55)
    assert simba.describe() == "Симба: Р-р-р"
    assert (simba.name, simba.weight) == ("Симба", 190)
    with pytest.raises(TypeError):
        zoo.add("слон")


def test_05_zoo_abstract_and_unknown_animal(solution):
    Animal = solution("zoo", "Animal")
    Zoo = solution("zoo", "Zoo")
    assert inspect.isabstract(Animal)
    with pytest.raises(TypeError):
        Animal("Нечто", 10)

    class Cow(Animal):
        def sound(self):
            return "Му"

        def food_per_day(self):
            return 20

    class HalfDone(Animal):            # food_per_day не реализован
        def sound(self):
            return "..."

    with pytest.raises(TypeError):
        HalfDone("Недоделка", 1)

    zoo = Zoo()
    zoo.add(Cow("Бурёнка", 500))
    zoo.add(Cow("Зорька", 450))
    assert zoo.sounds() == ["Бурёнка: Му", "Зорька: Му"]
    assert zoo.total_food() == 40


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


def test_06_student(solution):
    Student = solution("student", "Student")
    a = Student("Аня")
    assert a.average() == 0
    assert a.subjects() == [] and a.debts() == []
    a.add_grade("матанализ", 5)
    a.add_grade("матанализ", 4)
    a.add_grade("информатика", 5)
    b = Student("Боря")
    b.add_grade("матанализ", 2)
    b.add_grade("информатика", 4)
    assert a.average() == pytest.approx(14 / 3)
    assert a.average("матанализ") == pytest.approx(4.5)
    assert a.subjects() == ["информатика", "матанализ"]
    assert b.debts() == ["матанализ"]
    assert a.debts() == []
    assert b < a and not a < b
    assert max([b, a]) is a
    assert repr(a) == "Student('Аня', 4.67)"
    assert repr(Student("Вова")) == "Student('Вова', 0.00)"
    with pytest.raises(KeyError):
        a.average("физика")
    for bad in (1, 6, 0):
        with pytest.raises(ValueError):
            a.add_grade("физика", bad)
    assert a.subjects() == ["информатика", "матанализ"]   # неудачная оценка не завела предмет
    b.add_grade("матанализ", 5)                            # 3.5 по матанализу - долга нет
    assert b.debts() == []


def test_06_group(solution):
    Student = solution("student", "Student")
    Group = solution("student", "Group")

    def student(name, *grades):
        s = Student(name)
        for subject, grade in grades:
            s.add_grade(subject, grade)
        return s

    g = Group("ИСиТ-1")
    assert len(g) == 0 and g.ranking() == [] and g.with_debts() == []
    vera = student("Вера", ("физика", 4))
    anya = student("Аня", ("физика", 5), ("матанализ", 4))
    boris = student("Борис", ("физика", 2), ("матанализ", 5))
    gleb = student("Глеб", ("физика", 4))
    for s in (gleb, anya, boris, vera):         # Глеб раньше Веры: порядок при равенстве - по имени
        g.add(s)
    assert len(g) == 4
    assert "Аня" in g and "Дима" not in g
    assert [s.name for s in g.ranking()] == ["Аня", "Вера", "Глеб", "Борис"]
    assert g.ranking()[0] is anya
    assert g.with_debts() == ["Борис"]
    with pytest.raises(ValueError):
        g.add(Student("Аня"))
    with pytest.raises(TypeError):
        g.add("Аня")
    assert len(g) == 4


def test_07_money(solution):
    Money = solution("money", "Money")
    a, b = Money(10, 50), Money(2, 75)
    assert a + b == Money(13, 25)
    assert a - b == Money(7, 75)
    assert a - a == Money(0)
    with pytest.raises(ValueError):
        b - a
    assert Money(1, 150) == Money(2, 50)
    assert (Money(1, 150).rubles, Money(1, 150).kopecks) == (2, 50)
    assert Money(1, 0) == Money(0, 100)
    assert repr(Money(1, 150)) == "Money(2, 50)"
    assert str(Money(5, 7)) == "5 руб. 07 коп."
    assert str(Money(0)) == "0 руб. 00 коп."
    assert sorted([a, b]) == [b, a]
    assert b < a
    for args in ((-1,), (0, -5)):
        with pytest.raises(ValueError):
            Money(*args)
    with pytest.raises(AttributeError):
        a.rubles = 100
    assert a == Money(10, 50)          # операции не меняют слагаемые


def test_07_money_multiply_sum_split(solution):
    Money = solution("money", "Money")
    a = Money(10, 50)
    assert a * 3 == Money(31, 50)
    assert 3 * a == Money(31, 50)
    assert a * 0 == Money(0)
    with pytest.raises(ValueError):
        a * -1
    with pytest.raises(TypeError):
        a * 1.5
    assert sum([a, Money(2, 75), Money(0, 75)]) == Money(14, 0)
    assert sum([Money(1)]) == Money(1)

    assert Money(10).split(3) == [Money(3, 34), Money(3, 33), Money(3, 33)]
    assert Money(0, 5).split(3) == [Money(0, 2), Money(0, 2), Money(0, 1)]
    assert Money(7).split(1) == [Money(7)]
    parts = Money(1000, 1).split(7)
    assert len(parts) == 7
    assert sum(parts) == Money(1000, 1)
    totals = [p.rubles * 100 + p.kopecks for p in parts]
    assert max(totals) - min(totals) <= 1
    assert totals == sorted(totals, reverse=True)
    for bad in (0, -2):
        with pytest.raises(ValueError):
            Money(10).split(bad)


def test_08_hero_levels(solution):
    Hero = solution("hero", "Hero")
    h = Hero("Артур")
    assert (h.level, h.xp, h.hp, h.max_hp) == (1, 0, 100, 100)
    assert h.is_alive is True
    h.gain_xp(250)
    assert (h.level, h.xp, h.max_hp) == (2, 150, 120)
    assert repr(h) == "Hero('Артур', level=2, xp=150, hp=120/120)"
    h.take_damage(50)
    h.gain_xp(50)                      # новый уровень восстанавливает здоровье
    assert (h.level, h.xp, h.hp) == (3, 0, 140)
    h.gain_xp(1000)                    # 300 + 400 на два уровня, 300 остаётся
    assert (h.level, h.xp, h.hp) == (5, 300, 180)
    for bad in (0, -10):
        with pytest.raises(ValueError):
            h.gain_xp(bad)
    for attr in ("level", "xp", "hp", "max_hp"):
        with pytest.raises(AttributeError):
            setattr(h, attr, 99)


def test_08_hero_combat(solution):
    Hero = solution("hero", "Hero")
    arthur, orc = Hero("Артур"), Hero("Орк")
    arthur.gain_xp(250)
    orc.take_damage(85)
    assert orc.hp == 15
    arthur.attack(orc)
    assert orc.hp == 0 and orc.is_alive is False
    assert repr(arthur) == "Hero('Артур', level=3, xp=0, hp=140/140)"

    troll = Hero("Тролль")
    troll.gain_xp(100)                 # тролль второго уровня
    arthur.attack(troll)               # 30 урона, тролль жив - опыта нет
    assert troll.hp == 90 and arthur.xp == 0
    troll.attack(arthur)               # 20 урона
    assert arthur.hp == 120
    arthur.heal(1000)
    assert arthur.hp == 140            # не выше максимума
    arthur.take_damage(1000)
    assert arthur.hp == 0              # не ниже нуля

    for action in (lambda: orc.heal(10), lambda: orc.gain_xp(10),
                   lambda: orc.attack(troll), lambda: troll.attack(orc),
                   lambda: troll.attack(troll), lambda: troll.heal(0),
                   lambda: troll.take_damage(-5)):
        with pytest.raises(ValueError):
            action()
    assert troll.hp == 90


def test_08_hero_kill_reward(solution):
    Hero = solution("hero", "Hero")
    knight, dragon = Hero("Рыцарь"), Hero("Дракон")
    dragon.gain_xp(300)                # дракон третьего уровня
    dragon.take_damage(135)            # осталось 5 из 140
    knight.attack(dragon)              # 10 урона, награда 150 опыта
    assert dragon.is_alive is False
    assert (knight.level, knight.xp) == (2, 50)


def test_09_vector_arithmetic(solution):
    Vector = solution("vectors", "Vector")
    a, b = Vector(1, 0, 0), Vector(0, 1, 0)
    assert (Vector(1, 2).x, Vector(1, 2).y, Vector(1, 2).z) == (1, 2, 0)
    assert a + b == Vector(1, 1, 0)
    assert a - b == Vector(1, -1, 0)
    assert -Vector(1, -2, 3) == Vector(-1, 2, -3)
    assert 2 * Vector(1, 2, 3) == Vector(2, 4, 6)
    assert Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
    assert abs(Vector(3, 4)) == pytest.approx(5)
    assert abs(Vector(1, 2, 2)) == pytest.approx(3)
    assert repr(Vector(1, 2, 3)) == "Vector(1, 2, 3)"
    assert a == Vector(1, 0, 0)        # операции не меняют операнды


def test_09_vector_products(solution):
    Vector = solution("vectors", "Vector")
    a, b = Vector(1, 0, 0), Vector(0, 1, 0)
    assert a.dot(b) == 0
    assert Vector(1, 2, 3).dot(Vector(4, -5, 6)) == 12
    assert a.cross(b) == Vector(0, 0, 1)
    assert b.cross(a) == Vector(0, 0, -1)
    assert Vector(2, 3, 4).cross(Vector(5, 6, 7)) == Vector(-3, 6, -3)
    u, v = Vector(2, -1, 3), Vector(0, 4, 1)
    w = u.cross(v)
    assert u.dot(w) == 0 and v.dot(w) == 0          # перпендикулярен обоим
    assert a.is_orthogonal(b) and not a.is_orthogonal(Vector(1, 1, 0))
    assert Vector(1, 2, 3).is_collinear(Vector(-2, -4, -6))
    assert not Vector(1, 2, 3).is_collinear(Vector(1, 2, 4))


def test_09_vector_geometry(solution):
    Vector = solution("vectors", "Vector")
    triangle_area = solution("vectors", "triangle_area")
    volume = solution("vectors", "volume")
    n = Vector(3, 0, 4).normalized()
    assert (n.x, n.y, n.z) == (pytest.approx(0.6), pytest.approx(0), pytest.approx(0.8))
    assert abs(Vector(1, 2, 3).normalized()) == pytest.approx(1)
    with pytest.raises(ValueError):
        Vector(0, 0, 0).normalized()
    a = Vector(1, 0, 0)
    assert a.angle(Vector(1, 1, 0)) == pytest.approx(math.pi / 4)
    assert a.angle(Vector(-1, 0, 0)) == pytest.approx(math.pi)
    assert a.angle(Vector(0, 0, 5)) == pytest.approx(math.pi / 2)
    assert Vector(0.1, 0.2, 0.3).angle(Vector(0.1, 0.2, 0.3) * 3) == pytest.approx(0, abs=1e-6)
    with pytest.raises(ValueError):
        a.angle(Vector(0, 0, 0))
    assert triangle_area(Vector(0, 0), Vector(4, 0), Vector(0, 3)) == pytest.approx(6)
    assert triangle_area(Vector(1, 1, 1), Vector(2, 1, 1), Vector(1, 3, 1)) == pytest.approx(1)
    assert volume(Vector(1, 0, 0), Vector(0, 2, 0), Vector(0, 0, 3)) == pytest.approx(6)
    assert volume(Vector(0, 2, 0), Vector(1, 0, 0), Vector(0, 0, 3)) == pytest.approx(6)
    assert volume(Vector(1, 2, 3), Vector(2, 4, 6), Vector(0, 0, 1)) == pytest.approx(0)


def test_10_polygon(solution):
    Point = solution("polygon", "Point")
    Polygon = solution("polygon", "Polygon")
    corner = Point(0, 0)
    square = Polygon([corner, Point(2, 0), Point(2, 2), Point(0, 2)])
    assert len(square) == 4
    assert square.perimeter() == pytest.approx(8)
    assert square.area() == pytest.approx(4)
    square.move(5, 5)
    assert (corner.x, corner.y) == (0, 0)      # вершины - копии
    corner.x = 100
    assert square.area() == pytest.approx(4)   # и снаружи их не испортить
    assert square.bounding_box() == (5, 5, 7, 7)

    tri = Polygon([Point(0, 0), Point(0, 3), Point(4, 0)])   # обход по часовой
    assert tri.area() == pytest.approx(6)
    assert tri.perimeter() == pytest.approx(12)
    assert tri.bounding_box() == (0, 0, 4, 3)
    with pytest.raises(ValueError):
        Polygon([Point(0, 0), Point(1, 1)])


def test_10_polygon_convex_and_compare(solution):
    Point = solution("polygon", "Point")
    Polygon = solution("polygon", "Polygon")

    def poly(*coords):
        return Polygon([Point(x, y) for x, y in coords])

    square = poly((0, 0), (2, 0), (2, 2), (0, 2))
    letter_g = poly((0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2))
    assert letter_g.area() == pytest.approx(3)
    assert square.is_convex() is True
    assert letter_g.is_convex() is False
    assert poly((0, 2), (2, 2), (2, 0), (0, 0)).is_convex() is True      # обход в другую сторону
    assert poly((0, 0), (1, 0), (2, 0), (2, 2)).is_convex() is True      # три точки на прямой
    assert poly((0, 0), (4, 0), (2, 1), (2, 4)).is_convex() is False     # вмятина
    assert poly((0, 0), (2, 2), (2, 0), (0, 2)).is_convex() is False     # самопересечение
    assert letter_g < square and not square < letter_g
    assert sorted([square, letter_g])[0] is letter_g


def test_11_date_examples(solution):
    Date = solution("calendar_date", "Date")
    d = Date(31, 12, 2025)
    assert (d.day, d.month, d.year) == (31, 12, 2025)
    assert d + 1 == Date(1, 1, 2026)
    assert d + 60 == Date(1, 3, 2026)
    assert Date(1, 3, 2024) + (-1) == Date(29, 2, 2024)
    assert Date(1, 1, 2026) - Date(1, 1, 2025) == 365
    assert Date(1, 1, 2025) - Date(1, 1, 2026) == -365
    assert repr(d + 1) == "Date(1, 1, 2026)"
    assert str(Date(9, 5, 1945)) == "09.05.1945"
    assert Date(1, 1, 2025) < Date(2, 1, 2025)
    assert not Date(2, 1, 2025) < Date(1, 1, 2025)
    assert d == Date(31, 12, 2025)
    assert d + 0 == d


def test_11_date_validation(solution):
    Date = solution("calendar_date", "Date")
    for args in ((29, 2, 2025), (31, 4, 2025), (1, 13, 2025), (0, 1, 2025),
                 (32, 1, 2025), (29, 2, 1900)):
        with pytest.raises(ValueError):
            Date(*args)
    Date(29, 2, 2000)                  # делится на 400 - високосный
    Date(29, 2, 2024)


def test_11_date_against_calendar(solution):
    Date = solution("calendar_date", "Date")
    rng = random.Random(41)
    start = datetime.date(1900, 1, 1).toordinal()
    end = datetime.date(2100, 12, 31).toordinal()
    for _ in range(300):
        a = datetime.date.fromordinal(rng.randint(start, end))
        delta = rng.randint(-40_000, 40_000)
        b = a + datetime.timedelta(days=delta)
        da, db = Date(a.day, a.month, a.year), Date(b.day, b.month, b.year)
        assert da + delta == db, f"{a} + {delta}"
        assert db - da == delta, f"{b} - {a}"


def test_12_polynomial(solution):
    Polynomial = solution("polynomial", "Polynomial")
    p = Polynomial([1, 0, 2])
    q = Polynomial([0, 1])
    assert p(3) == 19
    assert p(0) == 1
    assert p + q == Polynomial([1, 1, 2])
    assert q + p == Polynomial([1, 1, 2])
    assert p * q == Polynomial([0, 1, 0, 2])
    assert p.derivative() == Polynomial([0, 4])
    assert Polynomial([5]).derivative() == Polynomial([0])
    assert p.degree() == 2
    assert Polynomial([7]).degree() == 0
    assert Polynomial([1, -1]) + Polynomial([0, 1]) == Polynomial([1])
    assert Polynomial([1, 2, 0, 0]).coeffs == [1, 2]
    assert Polynomial([0, 0]).coeffs == [0]
    assert Polynomial([1, 1]) * Polynomial([-1, 1]) == Polynomial([-1, 0, 1])
    assert repr(p) == "Polynomial([1, 0, 2])"
    assert p == Polynomial([1, 0, 2])          # операции не меняют операнды
    assert Polynomial([2, -3, 0, 1])(2) == 4


def test_13_matrix(solution):
    Matrix = solution("matrix", "Matrix")
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[0, 1], [1, 0]])
    assert a.shape == (2, 2)
    assert a[1, 0] == 3
    assert a + b == Matrix([[1, 3], [4, 4]])
    assert a * b == Matrix([[2, 1], [4, 3]])
    assert b * a == Matrix([[3, 4], [1, 2]])
    assert 2 * a == Matrix([[2, 4], [6, 8]])
    assert a * 2 == Matrix([[2, 4], [6, 8]])
    assert a * Matrix.identity(2) == a
    assert Matrix.identity(3) == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    row = Matrix([[1, 2, 3]])
    assert row.transpose() == Matrix([[1], [2], [3]])
    assert row.transpose().shape == (3, 1)
    assert row * row.transpose() == Matrix([[14]])
    assert repr(a) == "Matrix([[1, 2], [3, 4]])"
    assert a == Matrix([[1, 2], [3, 4]])       # операции не меняют операнды


def test_13_matrix_errors_and_copy(solution):
    Matrix = solution("matrix", "Matrix")
    a = Matrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        a * Matrix([[1, 2, 3]])
    with pytest.raises(ValueError):
        a + Matrix([[1, 2, 3]])
    for bad in ([], [[]], [[1, 2], [3]]):
        with pytest.raises(ValueError):
            Matrix(bad)
    rows = [[1, 2], [3, 4]]
    m = Matrix(rows)
    rows[0][0] = 100
    assert m[0, 0] == 1                        # матрица хранит копию


def test_14_showroom(solution):
    Car = solution("showroom", "Car")
    Serviceable = solution("showroom", "Serviceable")
    ElectricCar = solution("showroom", "ElectricCar")
    GasCar = solution("showroom", "GasCar")
    Showroom = solution("showroom", "Showroom")
    assert issubclass(ElectricCar, Car) and issubclass(ElectricCar, Serviceable)
    assert issubclass(GasCar, Car) and issubclass(GasCar, Serviceable)
    assert inspect.isabstract(Car) and inspect.isabstract(Serviceable)
    with pytest.raises(TypeError):
        Car("Ока", "1111", 1995, 50_000)

    tesla = ElectricCar("Tesla", "Model 3", 2022, 4_000_000, 75, 15)
    lada = GasCar("Lada", "Vesta", 2020, 1_200_000, 55, 7)
    assert tesla.range_km() == pytest.approx(500)
    assert lada.range_km() == pytest.approx(785.714, abs=1e-3)
    assert tesla.discounted_price(25) == pytest.approx(3_000_000)
    assert tesla.describe() == "Электромобиль Tesla Model 3 (2022)"
    assert lada.describe() == "Бензиновый Lada Vesta (2020)"

    salon = Showroom()
    assert len(salon) == 0
    assert salon.longest_range() is None
    salon.add(tesla)
    salon.add(lada)
    assert len(salon) == 2
    assert salon.total_price() == pytest.approx(5_200_000)
    assert salon.total_price(10) == pytest.approx(4_680_000)
    assert salon.longest_range() is lada
    assert salon.service_all() == ["Tesla Model 3: зарядка батареи", "Lada Vesta: замена масла"]
    with pytest.raises(TypeError):
        salon.add("машина")


def test_14_showroom_not_serviceable(solution):
    Car = solution("showroom", "Car")
    ElectricCar = solution("showroom", "ElectricCar")
    Showroom = solution("showroom", "Showroom")

    class ToyCar(Car):                 # не реализует Serviceable
        def range_km(self):
            return 1000

    toy = ToyCar("Hot Wheels", "Twin Mill", 2024, 300)
    assert toy.describe() == "Hot Wheels Twin Mill (2024)"
    salon = Showroom()
    salon.add(ElectricCar("Tesla", "Model 3", 2022, 4_000_000, 75, 15))
    salon.add(toy)
    assert salon.service_all() == ["Tesla Model 3: зарядка батареи"]
    assert salon.longest_range() is toy
    assert salon.total_price() == pytest.approx(4_000_300)


def test_15_bank_system_example(solution):
    Account = solution("bank_system", "Account")
    SavingsAccount = solution("bank_system", "SavingsAccount")
    CheckingAccount = solution("bank_system", "CheckingAccount")
    Customer = solution("bank_system", "Customer")
    Bank = solution("bank_system", "Bank")
    bank = Bank()
    bank.add_customer(Customer("Иван", "001"))
    bank.add_customer(Customer("Мария", "002"))
    bank.open_account("001", SavingsAccount("S1", "Иван", 1000, rate=0.05))
    bank.open_account("001", CheckingAccount("C1", "Иван", 100, overdraft=300))
    bank.open_account("002", Account("A1", "Мария", 0))

    bank.transfer("C1", "A1", 350)
    assert bank.customer("001").total_balance() == 750
    with pytest.raises(ValueError):
        bank.transfer("C1", "A1", 100)
    assert bank.customer("001").total_balance() == 750
    assert bank.customer("002").total_balance() == 350
    assert [a.number for a in bank.accounts("001")] == ["S1", "C1"]
    assert [a.number for a in bank.accounts("001", min_balance=0)] == ["S1"]
    assert [a.number for a in bank.customer("001").accounts()] == ["S1", "C1"]
    with pytest.raises(ValueError):
        bank.close_account("S1")
    assert bank.total_deposits() == 1100


def test_15_bank_system_rules(solution):
    Account = solution("bank_system", "Account")
    SavingsAccount = solution("bank_system", "SavingsAccount")
    Customer = solution("bank_system", "Customer")
    Bank = solution("bank_system", "Bank")
    bank = Bank()
    ivan = Customer("Иван", "001")
    bank.add_customer(ivan)
    with pytest.raises(ValueError):
        bank.add_customer(Customer("Самозванец", "001"))
    with pytest.raises(KeyError):
        bank.customer("999")
    bank.open_account("001", Account("A1", "Иван", 500))
    bank.open_account("001", SavingsAccount("S1", "Иван", 0))
    with pytest.raises(ValueError):
        bank.open_account("001", Account("A1", "Иван", 0))     # номер занят
    with pytest.raises(KeyError):
        bank.open_account("999", Account("X", "Никто", 0))

    with pytest.raises(ValueError):
        bank.transfer("A1", "S1", 600)                          # не хватает
    assert bank.total_deposits() == 500
    with pytest.raises(ValueError):
        bank.transfer("A1", "A1", 10)
    with pytest.raises(KeyError):
        bank.transfer("A1", "NOPE", 10)
    assert bank.total_deposits() == 500

    bank.transfer("A1", "S1", 500)
    bank.close_account("A1")                                    # остаток 0
    assert [a.number for a in ivan.accounts()] == ["S1"]
    with pytest.raises(KeyError):
        bank.close_account("A1")
    bank.open_account("001", Account("A1", "Иван", 0))          # номер освободился
    ivan.remove_account("A1")
    assert [a.number for a in ivan.accounts()] == ["S1"]
    assert ivan.total_balance() == 500
