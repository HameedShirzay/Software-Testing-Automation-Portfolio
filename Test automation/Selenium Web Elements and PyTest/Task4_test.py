import pytest


'''
Task 4 (Setting Up and Exploring PyTest)
Setup PyTest in your PyCharm project. 
Installation Command: pip install pytest 
Explore the PyTest basics. 
'''


# Installing pytest
# 1. pip install pytest
# 2. pytest --version


# writing a basic test:
def test_addition():
    assert 2 + 2 == 4


#Writing Assertions with some examples:

# 1. checking wiht some values:
def test_sum():
    assert 1 + 2 == 3  # Pass
    assert 2 + 2 == 5  # Fail

# 2.checking list:
def test_list():
    assert [1, 2, 3] == [1, 2, 3]  # Pass
    assert [1, 2, 3] == [3, 2, 1]  # Fail

# 3. Checking Exceptions:
def test_raises_error():
    with pytest.raises(ZeroDivisionError):
        1 / 0  # Pass


#Using Pytest Fixtures:
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_data_length(sample_data):
    assert len(sample_data) == 3

# Parametrizing Tests:
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 5, 8),
])
def test_add(a, b, expected):
    assert a + b == expected
