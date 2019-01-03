import os

import pytest

from secret_key import secret_key

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY_PATHS = [
    './dir/.secret_key',  # Check relative path
    './.secret_key',  # Check relative path but, base dir == '.'
    '.secret_key_2',  # Check relative path but, base dir == ''
    os.path.join(BASE_DIR, '.secret_key_3'),  # Check abs path
    './.secret_key',  # Check file already exist
]


def teardown_module(module):
    for path in set(SECRET_KEY_PATHS):
        os.remove(path)
    os.removedirs('./dir')


def test_generate():
    assert len(secret_key.generate()) == 50
    assert len(secret_key.generate(35)) == 35
    assert len(secret_key.generate(70)) == 70


@pytest.mark.parametrize("path", SECRET_KEY_PATHS)
def test_from_file(path):
    key = secret_key.from_file(path)
    with open(path, 'r') as f:
        assert key == f.read().strip()


def test_from_env_system_env():
    key = secret_key.from_env()
    assert key == 'env_test_content'


def test_from_env_call_twice():
    key1 = secret_key.from_env('unknown_env')
    key2 = secret_key.from_env('unknown_env')
    assert key1 == key2

