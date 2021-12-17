import pytest
import clean_data as cd
import os

if __name__ == '__main__':
    os.system("pytest -v ./tests.py")


def test_list_length():
    # make sure both lists are the same length
    assert len(cd.en_data) == len(cd.fr_data), "Data lists not the same length"
