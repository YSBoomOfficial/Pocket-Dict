import pytest
import os
import clean_data as cd
import search as sh

if __name__ == '__main__':
    os.system("pytest -v ./tests.py")


def test_list_length():
    # make sure both lists are the same length
    assert len(cd.en_data) == len(cd.fr_data), "Data lists not the same length"

def test_hello():
    text = sh.clean_input_str(" hello ")
    my_data = sh.get_all_data(text)
    result = sh.reduce_search_results(text, my_data)
    assert result == ['salut', 'bonjour', 're-bonjour'], "Incorrect Results"
