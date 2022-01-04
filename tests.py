import pytest
import os
import clean_data as cd
import search as sh

if __name__ == '__main__':
    os.system("pytest -v ./tests.py")


def test_list_length():
    # make sure both lists are the same length
    assert len(cd.en_data) == len(cd.fr_data), "Data lists not the same length"


def test_clean_input_str():
    # make sure the string cleaning work properly
    assert sh.clean_input_str(" * ._ hello )") == "hello", "Incorrect Output"

# test some strings and see results


def test_hello():
    text = " hello "
    result = sh.get_result(text, True)
    assert result == ['salut', 'bonjour', 're-bonjour'], "Incorrect Results"


def test_goodbye():
    text = "goodbye"
    result = sh.get_result(text, True)
    assert result == ['adieu', 'à la revoyure',
                      'dis au revoir'], "Incorrect Results"


def test_gibberish():
    text = "qwertyuiopasdfghjklzxcvbnm"
    result = sh.get_result(text, True)
    assert result == [], "Incorrect Results"

### NOTE: Not testing with empty string because callsite will only allow the get_all function to be called with a non empty string.
# if I had to test for empty string, this is what I would do:
# def test_empty():
#     text = ""
#     result = sh.get_result(text, False)
#     assert result == [], "Incorrect Results"
