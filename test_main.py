import sys

import pytest

import main


def test_python_version():
    assert sys.version_info.major == 3 and sys.version_info.minor >= 8


def test_for_integer_input():
    main.input = lambda x: 1
    with pytest.raises(
        ValueError,
        match=r"Somehow you didn't enter a string. Please try again."
    ):
        main.count_vowels()


def test_for_string_integer_input(capsys):
    main.input = lambda x: "1"
    with pytest.raises(SystemExit):
        main.count_vowels()
    captured = capsys.readouterr()
    assert captured.out == "That's not a string, that's a number. >_<\n"


def test_if_no_vowels(capsys):
    main.input = lambda x: "sky"
    main.count_vowels()
    captured = capsys.readouterr()
    assert captured.out == "The total is: \n"


def test_if_vowels(capsys):
    main.input = lambda x: "foobar"
    main.count_vowels()
    captured = capsys.readouterr()
    assert captured.out == "The total is: \no: 2 instances\na: 1 instances\n"


def test_if_vowel(capsys):
    main.input = lambda x: "few"
    main.count_vowels()
    captured = capsys.readouterr()
    assert captured.out == "The total is: \ne: 1 instances\n"
