from src.lengthen_date.lengthen_date import lengthen_date


def test_lengthen_date_data_type():
    assert type(lengthen_date('21.03.2017')) == str


def test_lengthen_date_basic():
    assert lengthen_date('21.03.2017') == 'Tuesday 21st March 2017'
