import pytest


def test_dict_1():
    dict_test = {'1': 1}
    dict_test['2'] = '2'
    assert dict_test['1'] == 1
    assert dict_test['2'] == '2'


@pytest.mark.parametrize("test_input, test_res", [({'1': 1 + 2}, {'1': 3}), ({'2': 1 * 2}, {'2': 2}), ({'3': 'a' * 3}, {'3': 'aaa'})])
def test_dict_2(test_input, test_res):
    dict_test = dict(test_input)
    assert dict_test == test_res


def test_dict_3():
    dict_test = ['1', '2']
    try:
        assert dict(dict_test)
    except ValueError:
        pass


def test_tuple_1():
    tuple_test = tuple('Hello')
    assert tuple_test[0] == 'H'
    assert tuple_test[1] == 'e'
    assert tuple_test[2] == 'l'
    assert tuple_test[3] == 'l'
    assert tuple_test[4] == 'o'


@pytest.mark.parametrize("test_input, test_res", [((1 + 2,), (3,)), (tuple('Hi'), ('H', 'i')), (('H', True, 1 + 2), ('H', True, 3))])
def test_tuple_2(test_input, test_res):
    tuple_test = test_input
    assert tuple_test == test_res


def test_tuple_3():
    tuple_test = 2
    try:
        assert tuple(tuple_test)
    except TypeError:
        pass
