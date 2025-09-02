
## 20. Разобрать Числа из Букв (Python | C)

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
# Test cases
    shouldBe ("one", 1)
    shouldBe ("twenty", 20)
    shouldBe ("two hundred and forty-six", 246)
```



## 5. Функция `accum` (C)

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

char *accum (const char *source)
{
  // Solution 
}

int main()
{
    const char *source = "ZpglnRxqenU";
    const char *expected = "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu";
    char *actual = accum(source);
    assert(expected, actual, "Source: \"%s\" Expected: \"%s\" Actual: \"%s\"", source, expected, actual);
    free(actual); actual = NULL;
 
    const char *source = "NyffsGeyylB";
    const char *expected = "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb";
    char *actual = accum(source);
    assert(expected, actual, "Source: \"%s\" Expected: \"%s\" Actual: \"%s\"", source, expected, actual);
    free(actual); actual = NULL;

    const char *source = "MjtkuBovqrU";
    const char *expected = "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu";
    char *actual = accum(source);
    assert(expected, actual, "Source: \"%s\" Expected: \"%s\" Actual: \"%s\"", source, expected, actual);
    free(actual); actual = NULL;
    const char *source = "EvidjUnokmM";
    const char *expected = "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm";
    char *actual = accum(source);
    assert(expected, actual, "Source: \"%s\" Expected: \"%s\" Actual: \"%s\"", source, expected, actual);
    free(actual); actual = NULL;
    const char *source = "HbideVbxncC";
    const char *expected = "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc";
    char *actual = accum(source);
    assert(expected, actual, "Source: \"%s\" Expected: \"%s\" Actual: \"%s\"", source, expected, actual);
    free(actual); actual = NULL;
}
```

