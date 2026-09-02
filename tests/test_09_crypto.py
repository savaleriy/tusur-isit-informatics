"""Занятие 9. Криптография и безопасность.

Задачи 1-5 - обязательные, они встроены в конспект (docs/09-crypto/note.md).
Задачи 6-15 - балльные (в task.md они пронумерованы 1-10).
"""

import pytest


# Достаточно длинный английский текст, чтобы частотный анализ работал надёжно.
LONG_TEXT = (
    "the quick brown fox jumps over the lazy dog while the sun rises over the "
    "eastern hills and the birds begin to sing their morning songs as the village "
    "slowly wakes up and the market opens its doors to the people who come to buy "
    "fresh bread and milk and vegetables for their families and the children run "
    "to school with their books and pencils and the old men sit by the fire and "
    "tell stories of the days when they were young and strong and the world was "
    "full of wonder and every road led somewhere new and exciting and the nights "
    "were filled with stars and the mornings smelled of rain and fresh grass and "
    "the whole village gathered in the square to celebrate the harvest and sing "
    "the songs that their fathers had sung before them and their fathers before "
    "that for as long as anyone could remember the seasons turning one into the "
    "next"
)


# --------------------------------------------------------------------------
# Обязательные задания (встроены в конспект)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text, shift, expected",
    [
        ("hello", 3, "khoor"),
        ("khoor", -3, "hello"),
        ("xyz", 5, "cde"),
        ("Hello!", 1, "Ifmmp!"),
        ("abc", 26, "abc"),
    ],
)
def test_01_caesar(solution, text, shift, expected):
    f = solution("caesar", "caesar")
    assert f(text, shift) == expected


def test_01_caesar_roundtrip(solution):
    f = solution("caesar", "caesar")
    text = "Attack at dawn"
    assert f(f(text, 9), -9) == text


def test_02_break_caesar(solution):
    caesar = solution("caesar", "caesar")
    break_caesar = solution("break_caesar", "break_caesar")
    for shift in (3, 7, 13, 20):
        cipher = caesar(LONG_TEXT, shift)
        assert break_caesar(cipher) == LONG_TEXT


def test_03_xor_cipher(solution):
    f = solution("xor_cipher", "xor_cipher")
    assert f(b"hello", b"k") == bytes([3, 14, 7, 7, 4])
    assert f(bytes([3, 14, 7, 7, 4]), b"k") == b"hello"
    assert f(b"abc", b"abc") == b"\x00\x00\x00"


def test_03_xor_cipher_roundtrip(solution):
    f = solution("xor_cipher", "xor_cipher")
    data = b"some secret message"
    key = b"key"
    assert f(f(data, key), key) == data


def test_04_diffie_hellman(solution):
    public = solution("diffie_hellman", "diffie_hellman_public")
    shared = solution("diffie_hellman", "diffie_hellman_shared")
    p, g = 23, 5
    a, c = 6, 15
    A = public(a, g, p)
    C = public(c, g, p)
    assert A == 8
    assert C == 19
    assert shared(C, a, p) == 2
    assert shared(A, c, p) == 2


def test_04_diffie_hellman_agrees(solution):
    public = solution("diffie_hellman", "diffie_hellman_public")
    shared = solution("diffie_hellman", "diffie_hellman_shared")
    p, g = 101, 2
    a, c = 13, 27
    A = public(a, g, p)
    C = public(c, g, p)
    assert shared(C, a, p) == shared(A, c, p)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"),
        ("", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
        ("abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"),
    ],
)
def test_05_sha256(solution, text, expected):
    f = solution("sha256", "sha256")
    assert f(text) == expected


# --------------------------------------------------------------------------
# Балльные задания
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, World!", "Uryyb, Jbeyq!"),
        ("Uryyb, Jbeyq!", "Hello, World!"),
        ("123!@#", "123!@#"),
    ],
)
def test_06_rot13(solution, text, expected):
    f = solution("rot13", "rot13")
    assert f(text) == expected


def test_06_rot13_involution(solution):
    f = solution("rot13", "rot13")
    assert f(f("The Quick Brown Fox")) == "The Quick Brown Fox"


def test_10_vigenere(solution):
    enc = solution("vigenere", "vigenere_encrypt")
    dec = solution("vigenere", "vigenere_decrypt")
    assert enc("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert dec("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
    assert dec(enc("Hello, World!", "key"), "key") == "Hello, World!"


def test_12_frequency_analysis(solution):
    f = solution("frequency_analysis", "frequency_analysis")
    assert f("aabbbcccc") == ["c", "b", "a"]
    assert f("Hello, World!") == ["l", "o", "d", "e", "h", "r", "w"]


def test_12_frequency_analysis_empty(solution):
    f = solution("frequency_analysis", "frequency_analysis")
    assert f("") == []
    assert f("123 !@#") == []


def test_14_rsa(solution):
    modinv = solution("rsa", "modinv")
    encrypt = solution("rsa", "rsa_encrypt")
    decrypt = solution("rsa", "rsa_decrypt")
    assert modinv(17, 3120) == 2753
    assert encrypt(65, 17, 3233) == 2790
    assert decrypt(2790, 2753, 3233) == 65


def test_14_rsa_roundtrip(solution):
    modinv = solution("rsa", "modinv")
    encrypt = solution("rsa", "rsa_encrypt")
    decrypt = solution("rsa", "rsa_decrypt")
    p, q, e = 61, 53, 17
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    for m in (42, 100, 3000):
        assert decrypt(encrypt(m, e, n), d, n) == m


def test_10_break_vigenere(solution):
    enc = solution("vigenere", "vigenere_encrypt")
    break_vigenere = solution("break_vigenere", "break_vigenere")
    for key in ("KEY", "CODE"):
        cipher = enc(LONG_TEXT, key)
        assert break_vigenere(cipher, len(key)) == LONG_TEXT


@pytest.mark.parametrize(
    "a0, a1, expected",
    [
        ('karolin', 'kathrin', 3),
        ('1011101', '1001001', 2),
        ('abc', 'abc', 0),
        ('', '', 0),
        ('ab', 'ba', 2),
    ],
)
def test_07_hamming_distance(solution, a0, a1, expected):
    f = solution("hamming", "hamming_distance")
    assert f(a0, a1) == expected


@pytest.mark.parametrize(
    "a0, a1, expected",
    [
        (300, 45, 4),
        (0, 0, 0),
        (-124, -16, 1),
        (666666, 333111, 6),
        (545034, 5, 1),
        (0, 76899299, 14),
    ],
)
def test_08_gcd_bit_count(solution, a0, a1, expected):
    f = solution("gcd_bits", "gcd_bit_count")
    assert f(a0, a1) == expected


@pytest.mark.parametrize(
    "a0, a1, expected",
    [
        (7, 10, False),
        (7, 15, True),
        (10, 15, True),
        (0, 0, False),
        (255, 255, True),
        (1, 1, False),
    ],
)
def test_09_has_common_bits(solution, a0, a1, expected):
    f = solution("common_bits", "has_common_bits")
    assert f(a0, a1) == expected


@pytest.mark.parametrize(
    "a0, a1, expected",
    [
        ('zbk', [0, 1], 'b'),
        ('abcd', [1, 1, 1], 'a'),
        ('ab', [0], 'b'),
        ('hello', [0, 0, 0, 0], 'o'),
    ],
)
def test_11_last_survivor(solution, a0, a1, expected):
    f = solution("last_char", "last_survivor")
    assert f(a0, a1) == expected


@pytest.mark.parametrize(
    "a0, expected",
    [
        ('zzzab', 'cz'),
        ('aa', 'b'),
        ('aaaa', 'c'),
        ('abc', 'abc'),
        ('', ''),
        ('zz', 'a'),
        ('aabb', 'bc'),
    ],
)
def test_13_letter_substitution(solution, a0, expected):
    f = solution("substitution", "letter_substitution")
    assert f(a0) == expected
