Co
# Обязательные задания 


> **Половину задач нужно решить на python, половину на Си. Вы выбираете сами**

## 1. 

> `task_1{.py|c}`

Дано расстояние в метрах, вводимое пользователем. Переведите метры в
сантиметры, результат выведите в консоль в формате «Distance in centimeters: `distance`»;

## 2. 

> `task_2{.py|c}`

Известны два расстояния, вводимые пользователем: одно в километрах,
другое — в метрах. С помощью условной конструкции выведите наименьшее расстояние;

## 3. 

> `task_3{.py|c}`

Дан массив с числами от 0 до 9. Используя цикл for, выведите в консоль таблицу
умножения для числа, вводимого пользователем. 

## 4. 

> `task_4{.py|c}`

Определите, является ли число a делителем числа b;
 
## 5. 

> `task_5{.py|c}`

Напишите программу вывода на экран числа, вводимого с клавиатуры. После
выводимого числа должно следовать сообщение: «Thats the number you entered
`number`;

## 6. 

> `task_6{.py|c}`

Если число m больше числа n, то выведите на экран «Number m > n», Если
число m меньше числа n, то выведите на экран «Number m < n», в противном случае
выведите сообщение «The numbers are equal»;

## 7. 

> `task_7{.py|c}`

Дан радиус окружности. Найдите ее диаметр;
Найдите:
	- сумму всех целых чисел от 100 до 500;
	- сумму всех целых чисел от a до 500 (значение a вводится с клавиатуры; a<500);

## 8. 

> `task_8{.py|c}`

Напишите программу, которая запрашивает у пользователя его имя и выводит
сообщение в следующем формате «Hello, `username`»;

## 9. 

> `task_9{.py|c}`

Пусть a, b, c – переменные, которым присваиваются введенные числа, а
переменная m в конечном итоге должна будет содержать значение наибольшей
переменной;

## 10. 

>`task_10{.py|c}`

Пользователь вводит два числа. Одно присваивается одной переменной, а
второе — другой. Необходимо поменять значения переменных так, чтобы значение первой оказалось во второй, а второй — в первой;

## 11. 

> `task_11{.py|c}`

Найти номер минимального элемента массива. Например, в массиве [10, -3, -
5, 2, 5] номер минимального элемента;

## 12.

> `task_12{.py|c}`

Переведите число, введенное пользователем, в байты или килобайты в
зависимости от его выбора. В данном задании вам нужно будет создать функции, для
перевода из килобайтов в байты и из байтов в килобайты. 

## 13. 

> `task_13{.py|c}`

Создайте программу, которая просит пользователя ввести свое имя и возраст. Распечатайте адресованное им послание, в котором будет указан год, в котором им исполнится 100 лет.

## 14.

>`task_14{.py|c}`

Напечатайте месяц из календаря по заданному начальному дню и количеству дней. Ваш ответ должен выглядеть примерно так:

```undefined
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

## 15.

> task_15{.py|c}

Напишите программу, выводящую количество дней в месяце по заданному номеру месяца и году.

### Формат ввода

На вход программе подается два целых положительных числа: номер месяца (от 1 до 12) и четырёхзначный год.

### Формат вывода

Необходимо вывести одно число — количество дней в заданном месяце.

#### Пример 1

Ввод

```
1 2001
```

Вывод

```
31
```

#### Пример 2

Ввод

```
2 2001
```

Вывод

```
28
```


## 16.

> task_16{.py|c}

На мероприятие приглашены $n$ гостей. Им предлагают занять места с номерами от $1$ до $n$ в зале. Гости занимают эти места в произвольном порядке. Известно, на каком месте сел очередной гость.

Выпишите для каждого очередного места номер гостя, который на него сел.

### Формат ввода

Дано число nn, а затем nn различных чисел $a1,a2,...,a_n$ ​ от $1$ до $n$. Число $ak$​ — это номер места, на которое сел $k$-й гость.

Число $n$ не превосходит $20000$.

### Формат вывода

Выведите $n$ чисел $b1​,b2​,...,b_n$​ от $1$ до $n$. Число $bk$​ должно обозначать номер гостя, который сел на $k$-е место.

#### Пример 1

Ввод

```
5
1 2 3 5 4
```

Вывод

```
1 2 3 5 4 
```

#### Пример 2

Ввод

```
11
11 6 8 2 10 9 4 7 3 1 5
```

Вывод

```
10 4 9 7 11 2 8 3 6 5 1 
```

# Балльные задания

> Нужно набрать 20 баллов


## 17. Черепашьи бега (C)

> `tortoise_racing.c`

У нас есть две черепахи:
*   **Черепаха A** (ленивая): Уползает со скоростью `v1` футов в час. У неё фора в `g` футов.
*   **Черепаха B** (голодная): Бежит со скоростью `v2` футов в час. Она хочет догнать A и вернуться к своей капусте.

Вопрос: **Через какое время B догонит A?**

Самое важное: если `v1` >= `v2`, то жадная черепашака никогда не догонит ленивую. Это же очевидно! В этом случае мы возвращаем `nil` (или что-то подобное, в зависимости от языка).

Так, смотрите, вся хитрость не в физике, а в *относительной скорости*. Представьте, что черепаха A стоит на месте (просто потому что нам так удобно!). Тогда с какой скоростью к ней приближается черепаха B?
Правильно! Со скоростью `v2 - v1` футов в час.

А расстояние между ними в этот момент? Именно `g` футов.

**Время = Расстояние / Скорость**

Итак, общее время в часах, которое потребуется B, чтобы догнать A, это:
`t = g / (v2 - v1)`

Всё! Задача решена. Но нет! Время `t` у нас получится дробным (например, 0.538456 часов), а нам нужно представить его в виде **[часы, минуты, секунды]**, отбросив доли секунды.

Давайте проверим на примере `race(720, 850, 70)`:

1.  `t = 70 / (850 - 720) = 70 / 130 ≈ 0.538461538 часов`
2.  **Часы:** `floor(0.538461538) = 0`
3.  **Минуты:** `0.538461538 * 60 ≈ 32.30769228`
4.  **Целые минуты:** `floor(32.30769228) = 32`
5.  **Секунды:** `(32.30769228 - 32) * 60 ≈ 0.30769228 * 60 ≈ 18.4615368`
6.  **Целые секунды:** `floor(18.4615368) = 18`

Получаем `[0, 32, 18]`. Сошлось!

**Предупреждение!** В коде нужно быть осторожным с целочисленным делением и преобразованиями. Лучше работать с плавающей точкой, а потом брать целые части. И не забыть краевой случай с `v1 >= v2`!


```c
#include <stdlib.h>
#include <math.h>

int* race(int v1, int v2, int g) 
{
   // ВАШЕ РЕШЕНИЕ ТУТ
   return result;
}


static int arrays_equal(const int *a, const int *b, size_t n) {
    for (size_t i = 0; i < n; i++) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

static void do_test(int v1, int v2, int g, const int expected[3], int test_num) {
    int *actual = race(v1, v2, g);
    
    if (!arrays_equal(actual, expected, 3)) {
        free(actual);
        exit(test_num); // Возвращаем номер проваленного теста
    }
    
    free(actual);
}

int main() {
    do_test(720, 850, 70, (int[]){0, 32, 18}, 1);
    do_test(820, 81, 550, (int[]){-1, -1, -1}, 2);
    do_test(80, 91, 37, (int[]){3, 21, 49}, 3);
    do_test(80, 100, 40, (int[]){2, 0, 0}, 4);
    do_test(720, 850, 37, (int[]){0, 17, 4}, 5);
    do_test(720, 850, 370, (int[]){2, 50, 46}, 6);
    do_test(120, 850, 37, (int[]){0, 3, 2}, 7);
    do_test(820, 850, 550, (int[]){18, 20, 0}, 8);
    do_test(82, 50, 55, (int[]){-1, -1, -1}, 9);
    
    return 0; 
}
```


##  18. Преобразование в Стиль Джейдена Смита (Python)

> `jaden.py`

Смотрите, в чём тут дело. На входе у нас обычная строка, например:
`"How can mirrors be real if our eyes aren't real"`

А на выходе мы должны получить:
`"How Can Mirrors Be Real If Our Eyes Aren't Real"`

Видите? Первая буква каждого слова стала заглавной, а все остальные — строчными.

Но давайте посмотрим на пример с апострофом: `"aren't"`.
*   Глупый алгоритм мог бы сделать `"Aren'T"`, потому что увидел бы букву `'t'` после апострофа и тоже захотел бы её capitalize.
*   Но умный алгоритм, который использует встроенную функцию `capitalize()` (или её аналог в вашем языке), сделает правильно: `"Aren't"`. Потому что стандартные функции обычно обрабатывают только первый символ слова.

Вот вам и ответ! Получилась строка в стиле Джейдена Смита.


```c
def to_jaden_case(string):
	# ВАШЕ РЕШЕНИЕ ТУТ
    return result

def test():
    test_cases = [
        [
            "most trees are blue",
            "Most Trees Are Blue"
        ],
        [
            "How can mirrors be real if our eyes aren't real",
            "How Can Mirrors Be Real If Our Eyes Aren't Real"
        ],
        [
            "All the rules in this world were made by someone no smarter than you. So make your own.",
            "All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own."
        ],
        [
            "School is the tool to brainwash the youth.",
            "School Is The Tool To Brainwash The Youth."
        ],
        [
            "If newborn babies could speak they would be the most intelligent beings on planet Earth.",
            "If Newborn Babies Could Speak They Would Be The Most Intelligent Beings On Planet Earth."
        ],
        [
            "If everybody in the world dropped out of school we would have a much more intelligent society.",
            "If Everybody In The World Dropped Out Of School We Would Have A Much More Intelligent Society."
        ],
        [
            "Trees are never sad look at them every once in awhile they're quite beautiful.",
            "Trees Are Never Sad Look At Them Every Once In Awhile They're Quite Beautiful."
        ],
        [
            "When I die. then you will realize",
            "When I Die. Then You Will Realize"
        ],
        [
            "I should just stop tweeting, the human conciousness must raise before I speak my juvenile philosophy.",
            "I Should Just Stop Tweeting, The Human Conciousness Must Raise Before I Speak My Juvenile Philosophy."
        ],
        [
            "Jonah Hill is a genius",
            "Jonah Hill Is A Genius"
        ],
        [
            "Dying is mainstream",
            "Dying Is Mainstream"
        ],
        [
            "If there is bread winners, there is bread losers. But you can't toast what isn't real.",
            "If There Is Bread Winners, There Is Bread Losers. But You Can't Toast What Isn't Real."
        ],
        [
            "You Can Discover Everything You Need to Know About Everything by Looking at your Hands",
            "You Can Discover Everything You Need To Know About Everything By Looking At Your Hands"
        ],
        [
            "Fixed habits to respond to authority takes 12 years. Have fun",
            "Fixed Habits To Respond To Authority Takes 12 Years. Have Fun"
        ],
        [
            "When you Live your Whole life In a Prison freedom Can be So dull.",
            "When You Live Your Whole Life In A Prison Freedom Can Be So Dull."
        ],
        [
            "Young Jaden: Here's the deal for every time out you give me, you'll give me 15 dollars for therapy when I get older.",
            "Young Jaden: Here's The Deal For Every Time Out You Give Me, You'll Give Me 15 Dollars For Therapy When I Get Older."
        ],
        [
            "The moment that truth is organized it becomes a lie.",
            "The Moment That Truth Is Organized It Becomes A Lie."
        ],
        [
            "Three men, six options, don't choose.",
            "Three Men, Six Options, Don't Choose."
        ],
        [
            "Water in the eyes and alcohol in the eyes are pretty much the same I know This from first Hand Experience.",
            "Water In The Eyes And Alcohol In The Eyes Are Pretty Much The Same I Know This From First Hand Experience."
        ],
        [
            "Pay attention to the numbers in your life they are vastly important.",
            "Pay Attention To The Numbers In Your Life They Are Vastly Important."
        ],
        [
            "We need to stop teaching the Youth about the Past and encourage them to change the Future.",
            "We Need To Stop Teaching The Youth About The Past And Encourage Them To Change The Future."
        ],
        [
            "If a book store never runs out of a certain book, dose that mean that nobody reads it, or everybody reads it",
            "If A Book Store Never Runs Out Of A Certain Book, Dose That Mean That Nobody Reads It, Or Everybody Reads It"
        ],
        [
            "People tell me to smile I tell them the lack of emotion in my face doesn't mean I'm unhappy",
            "People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy"
        ],
        [
            "I watch Twilight every night",
            "I Watch Twilight Every Night"
        ]
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        try:
            result = to_jaden_case(input_str)
            if result != expected:
                exit(i)  # Возвращаем номер проваленного теста
        except Exception:
            exit(i)  # Если возникла ошибка - тоже провал
    
    return True  # Все тесты пройдены

if __name__ == "__main__":
    test()
    exit(0)  # Все тесты пройдены успешно
```


## 19. Возвести каждую цифру в квадрат и склеить (C)

> `square_digits.c`

Итак, у нас на входе целое число. Например, `9119`. Нам нужно:
1.  Разобрать его на отдельные цифры: `9`, `1`, `1`, `9`.
2.  Каждую цифру возвести в квадрат: $9^2 = 81, 1^2 = 1, 1^2 = 1, 9^2 = 81$.
3.  Получившиеся результаты **склеить** вместе в одно новое число: `81` + `1` + `1` + `81` = `811181`.

Вот и всё! Из `9119` получился `811181`.

Поэтому самый простой путь:
1.  Превратить число в строку. Почему? Со строкой легко работать посимвольно!
    `9119` -> `"9119"`
2.  Пройтись по каждому символу (цифре) в этой строке:
    *   Взять символ `'9'`
    *   Превратить его обратно в цифру `9` (чтобы можно было возвести в квадрат)
    *   Возвести в квадрат: `9 * 9 = 81`
    *   Получившийся результат снова превратить в строку `"81"`
3.  По мере прохода по строке, мы будем собирать эти маленькие строки-квадраты в одну большую строку.
    `"81" + "1" + "1" + "81" = "811181"`
4.  Финальный шаг — взять эту большую строку и превратить её обратно в целое число!
    `"811181"` -> `811181`

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

unsigned long long square_digits(unsigned n) {
    // ВАШЕ РЕШЕНИЕ ТУТ!
    return result;
}

static void do_test(unsigned n, unsigned long long expected, int test_num) {
    unsigned long long actual = square_digits(n);
    
    if (actual != expected) {
        exit(test_num); 
    }
}

int main() {
    do_test(3212u, 9414ull, 1);
    do_test(2112u, 4114ull, 2);
    do_test(0u, 0ull, 3);
    do_test(999u, 818181ull, 4);
    do_test(10001u, 10001ull, 5);
    do_test(3210987654u, 9410816449362516ull, 6);
    do_test(3999999999u, 9818181818181818181ull, 7);
    do_test(UINT_MAX, 164811681364948125ull, 8);
    
    return 0; 
}
```


О, классическая задачка! Я её обожаю. Она идеально подходит для того, чтобы проиллюстрировать красоту простого решения.

## 20. Сумма кратных 3 или 5 (Python)

> `mult_3_or_5.py`

Давайте разберём условие:
*   У нас есть любое число (скажем, `number`).
*   Нам нужно найти сумму всех натуральных чисел, которые:
    1.  Меньше этого `number`
    2.  И являются кратными либо 3, либо 5 (либо и тому, и другому одновременно).
*   **Важно:** Если число кратно и 3, и 5 (например, 15), мы должны посчитать его только один раз.
*   **На всякий случай:** Если нам подсунули отрицательное число, просто возвращаем 0.

Пример для `number = 10`:
Числа меньше 10, кратные 3 или 5: `3, 5, 6, 9`.
Их сумма: `3 + 5 + 6 + 9 = 23`.

```python
def mult_3_or_5(number):
	# ВАШЕ РЕШЕНИЕ ТУТ   
    return result

def test():
    test_cases = [
        (3, 0),    # Test 1
        (4, 3),    # Test 2
        (5, 3),    # Test 3
        (6, 8),    # Test 4
        (7, 14),   # Test 5
        (10, 23),  # Test 6
        (20, 78),   # Test 7
        (10, 23)   # Test 8
    ]
    
    for i, (input_num, expected) in enumerate(test_cases, 1):
        try:
            result = mult_3_or_5(input_num)
            if result != expected:
                exit(i) 
        except Exception:
            exit(i)
    
    return True  

if __name__ == "__main__":
	test()
    exit(0)
```

## 21. Разность двух списков (C)

> `diff_two_list.c`

У нас есть два списка: `a` и `b`.
Нам нужно из списка `a` удалить **все** элементы, которые есть в списке `b`. При этом порядок оставшихся элементов в `a` должен остаться таким же, как и был.

**Примеры, чтобы прояснить:**
*   `a = [1, 2]`, `b = [1]` **->** Результат: `[2]` (Удалили одну единицу)
*   `a = [1, 2, 2, 2, 3]`, `b = [2]` -> Результат: `[1, 3]` (Удалили все тройки двойки, а не только одну!)
*   `a = [1, 2, 3]`, `b = [4, 5]` -> Результат: `[1, 2, 3]` (Нечего удалять)
*   `a = [1, 2, 3]`, `b = []` -> Результат: `[1, 2, 3]` (Второй список пустой, удалять нечего)

Так, смотрите. Самое главное здесь — слово **"все вхождения"**. Если в списке `b` есть элемент `2`, то из списка `a` должны исчезнуть все двойки, а не только первая попавшаяся.

Самый простой и понятный способ — это пройтись по всем элементам списка `a` и для каждого элемента спросить: "А нет ли тебя в списке `b`?".

*   Если элемента в `b` **нет** — замечательно! Мы оставляем его в результате.
*   Если элемент в `b` **есть** — мы его пропускаем и не включаем в результат.

**Но есть нюанс!** Если мы будем для каждого элемента `a` проверять его наличие в `b` методом `element in b`, то при больших списках это может быть медленно (потому что проверка `in` для списка — это операция, которая в худшем случае просматривает весь список `b`).

Мы сохранили порядок элементов из `a` и удалили все вхождения элементов из `b`.

```с
#include <stdlib.h>

int *array_diff(const int *arr1, size_t n1, const int *arr2, size_t n2, size_t *z) {
	// ВАШЕ РЕШЕНИЕ ТУТ
    return result;
}

static int arrays_equal(const int *a, const int *b, size_t n) {
    for (size_t i = 0; i < n; i++) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

static void test_case(const int *arr1, size_t n1, const int *arr2, size_t n2, 
                     const int *expected, size_t expected_len, int test_num) {
    size_t z;
    int *result = array_diff(arr1, n1, arr2, n2, &z);
    
    if (z != expected_len || !arrays_equal(result, expected, z)) {
        exit(test_num); // Возвращаем номер проваленного теста
    }
    
    free(result);
}

int main() {
    {
        const int arr1[2] = {1, 2};
        const int arr2[1] = {1};
        const int expected[1] = {2};
        test_case(arr1, 2, arr2, 1, expected, 1, 1);
    }

    {
        const int arr1[3] = {1, 2, 2};
        const int arr2[1] = {1};
        const int expected[2] = {2, 2};
        test_case(arr1, 3, arr2, 1, expected, 2, 2);
    }
    {
        const int arr1[3] = {1, 2, 2};
        const int arr2[1] = {2};
        const int expected[1] = {1};
        test_case(arr1, 3, arr2, 1, expected, 1, 3);
    }
    {
        const int arr1[3] = {1, 2, 3};
        const int arr2[3] = {1, 2, 3};
        const int expected[1] = {3};
        test_case(arr1, 3, arr2, 2, expected, 1, 4);
    }
    {
        const int arr1[3] = {1, 2, 2};
        const int arr2[0] = {};
        const int expected[3] = {1, 2, 2};
        test_case(arr1, 3, arr2, 0, expected, 3, 5);
    }
    {
        const int arr1[0] = {};
        const int arr2[2] = {1, 2};
        const int expected[0] = {};
        test_case(arr1, 0, arr2, 2, expected, 0, 6);
    }
    {
        const int arr1[5] = {1, 2, 3, 4, 5};
        const int arr2[3] = {1, 3, 4};
        const int expected[2] = {2, 5};
        test_case(arr1, 5, arr2, 3, expected, 2, 7);
    }
    return 0; 
}
```


## 22. Сумма чётных чисел Фибоначчи (Python)

Смотрите, у нас есть последовательность Фибоначчи. Она начинается с 1 и 2 (иногда начинают с 1 и 1, но здесь именно так!), а каждое следующее число — это сумма двух предыдущих.

$$F_0 = 0, \space F_1 = 1$$
$$F_n = F_{n-1} + F_{n-2}$$


Нам нужно:

1. Сгенерировать все числа Фибоначчи, которые **не превышают четыре миллиона** (4,000,000).
2. Из этих чисел выбрать только **чётные**.
3. Найти **сумму** этих чётных чисел.

```python
def evenFibSum(limit):
	# ВАШЕ РЕШЕНИЕ ТУТ
	return result 

def test():
    test_cases = [
        (13, 10),      # Test 1
        (34, 44),      # Test 2  
        (100, 44),     # Test 3
        (200, 188),    # Test 4
        (10000, 3382), # Test 5
        (4000000, 4613732) # Test 6
    ]
    
    for i, (limit, expected) in enumerate(test_cases, 1):
        try:
            result = evenFibSum(limit)
            if result != expected:
                exit(i)
        except Exception:
            exit(i)
    
    return True

if __name__ == "__main__":
    test()
    exit(0)
```




# Бонус
## 23. Разобрать Числа из Букв (Python)

> `words_to_number.{c|py}`

У нас есть строки — слова, которые люди используют для обозначения чисел, — и нам нужно превратить их обратно в обычные, удобные для машины цифры. 

*   `"one"` -> `1` (Ну, это просто, правда?)
*   `"twenty"` -> `20` (Тоже ничего сложного)
*   `"two hundred forty-six"` -> `246` (Вот здесь уже начинается веселье! Нужно учесть множители и сложить всё вместе)
*   `"seven hundred eighty-three thousand nine hundred and nineteen"` -> `783919` (Ого! Целый миллион! Ну, почти.)

**Несколько важных заметок на полях:**

1.  Самый маленький числословный ребёнок — это `"zero"`. Да-да, ноль тоже считается!
2.  А самый большой, самый упитанный наш друг — это `"one million"`. Больше миллиона можно не приносить, наш парсер ещё не вырос.

3.  Словечко `"and"` — оно, понимаете ли, капризное. Иногда оно в предложении есть, а иногда его нет. Как шаловливый электрон! Наш алгоритм должен быть настолько ловким, чтобы игнорировать эту помеху. 

4.  И главное — все строки на входе уже правильные. Не нужно тратить силы на проверку, что «двадцать пятдесят» — это ерунда. 

Представьте, что слова вроде `"hundred"`, `"thousand"`, `"million"` — это математические операторы, как `+` или `*`. Они умножают всё, что было до них, на свой коэффициент.

Вот смотрите:
`"two hundred"` — это ведь `2 * 100`.
`"forty-six"` — это `40 + 6`.

А теперь сложный пример! Давайте разберём его на части, как я разбираю двигатель:

`"seven hundred eighty-three thousand nine hundred and nineteen"`

1.  **"seven hundred"**: Видим оператор `hundred` -> `7 * 100 = 700`
2.  **"eighty-three"**: Это просто число, которое мы позже прибавим -> `80 + 3 = 83`
3.  ️Ага! **"thousand"**! Это наш *большой* оператор. Он значит: «Всё, что я набрал до этого момента, нужно умножить на 1000 и отложить в большую копилку». Итак: `(700 + 83) * 1000 = 783 * 1000 = 783,000`
4.  Дальше пошли разряды поменьше. **"nine hundred"** -> `9 * 100 = 900`
5.  И наконец, **"nineteen"** -> `19`
6.  Теперь всё это добро складываем: `783,000 + 900 + 19 = 783,919`


```python
def words_to_number(words):
    # ВАШЕ РЕШЕНИЕ
    return result

def test():
    test_cases = [
	     ["one", 1],
	     ["twenty", 20],
	    ["two hundred and forty-six", 246],
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        try:
            result = to_jaden_case(input_str)
            if result != expected:
                exit(i)  # Возвращаем номер проваленного теста
        except Exception:
            exit(i)  # Если возникла ошибка - тоже провал
    
    return True  # Все тесты пройдены

if __name__ == "__main__":
    test()
    exit(0)  # Все тесты пройдены успешно
```



## 24. Функция `accum` (C)

> `accum.c`

Смотрите, у нас есть функция. Назовём её `accum`. Она принимает одну строку — какие-то буквы. А на выходе должна получиться другая строка, очень специфическая.

**Примеры, чтобы не запутаться:**

*   `accum("abcd")` превращается в `"A-Bb-Ccc-Dddd"`
*   `accum("RqaEzty")` разворачивается в `"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"`
*   `accum("cwAt")` становится `"C-Ww-Aaa-Tttt"`

Видите закономерность? Каждая буква в новой строке повторяется столько раз, каким по счёту она идёт в исходном слове. Первая буква — один раз (но с большой буквы!), вторая — два раза, третья — три, и так далее. И всё это великолепие соединено дефисами.

Для буквы с индексом `i` нам нужно повторить её `i+1` раз.

Давайте проиллюстрируем на примере `"abcd"`:

*   Индекс 0 (буква 'a'): `'A'` (верхний регистр) + `''` (повторить нижний регистр 0 раз) -> `"A"`
*   Индекс 1 (буква 'b'): `'B'` + `'b'` (повторить 1 раз) -> `"Bb"`
*   Индекс 2 (буква 'c'): `'C'` + `'cc'` (повторить 2 раза) -> `"Ccc"`
*   Индекс 3 (буква 'd'): `'D'` + `'ddd'` (повторить 3 раза) -> `"Dddd"`

А теперь — самое интересное! — соединяем всё это через дефис: `"A" + "-" + "Bb" + "-" + "Ccc" + "-" + "Dddd"`

Вот вам и ответ: `"A-Bb-Ccc-Dddd"`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

char *accum(const char *source) {
	// Ваше решение
	return result;
}

// Helper function for assertion (since standard assert doesn't take a format string)
void assert_strings_equal(const char *expected, const char *actual, const char *msg) {
    if (strcmp(expected, actual) != 0) {
        fprintf(stderr, "Assertion failed: %s\n", msg);
        fprintf(stderr, "Expected: \"%s\"\n", expected);
        fprintf(stderr, "Actual:   \"%s\"\n", actual);
        abort();
    }
}

int main() {
    {
        const char *source = "ZpglnRxqenU";
        const char *expected = "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu";
        char *actual = accum(source);
        assert_strings_equal(expected, actual, "Test 1");
        free(actual);
    }

    {
        const char *source = "NyffsGeyylB";
        const char *expected = "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb";
        char *actual = accum(source);
        assert_strings_equal(expected, actual, "Test 2");
        free(actual);
    }

    {
        const char *source = "MjtkuBovqrU";
        const char *expected = "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu";
        char *actual = accum(source);
        assert_strings_equal(expected, actual, "Test 3");
        free(actual);
    }

    {
        const char *source = "EvidjUnokmM";
        const char *expected = "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm";
        char *actual = accum(source);
        assert_strings_equal(expected, actual, "Test 4");
        free(actual);
    }

    {
        const char *source = "HbideVbxncC";
        const char *expected = "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc";
        char *actual = accum(source);
        assert_strings_equal(expected, actual, "Test 5");
        free(actual);
    }

    return 0;
}
```

