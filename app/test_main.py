from app.main import get_human_age


def test_cat_and_dog_less_than_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_with_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_all_animals_with_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_all_animals_with_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_all_animals_with_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_all_animals_with_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_all_animals_with_100_years() -> None:
    get_human_age(100, 100) == [21, 17]
