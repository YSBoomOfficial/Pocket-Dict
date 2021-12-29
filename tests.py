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

def test_hello():
    # make sure reduce_results gives the correct output
    text = sh.clean_input_str(" hello ")
    my_data = sh.find_all(text)
    result = sh.reduce_results(text, my_data)
    assert result == ['salut', 'bonjour', 're-bonjour'], "Incorrect Results"
