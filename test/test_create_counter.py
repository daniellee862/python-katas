from src.create_counter.create_counter import create_counter
counter = create_counter(5)


def test_return_value_is_dict():
    assert isinstance(counter, dict)


def test_properties_of_dict():
    assert 'up' in counter
    assert 'down' in counter


def test_return_vaules_of_properties_of_dict():
    up = counter['up']
    down = counter['down']
    incremented = up()
    down()
    decremented = down()
    assert incremented == 6
    assert decremented == 4
