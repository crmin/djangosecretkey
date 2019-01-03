import os

import pytest

from secret_key import secret_key

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_generate():
    assert len(secret_key.generate()) == 50
    assert len(secret_key.generate(35)) == 35
    assert len(secret_key.generate(70)) == 70


@pytest.mark.parametrize("path", [
    './dir/.secret_key',  # Check relative path
    './.secret_key',  # Check relative path but, base dir == '.'
    '.secret_key_2',  # Check relative path but, base dir == ''
    os.path.join(BASE_DIR, '.secret_key_3'),  # Check abs path
    './.secret_key',  # Check file already exist
])
def test_from_file(path):
    key = secret_key.from_file(path)
    with open(path, 'r') as f:
        assert key == f.read().strip()
