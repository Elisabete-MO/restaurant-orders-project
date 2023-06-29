import pytest
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    test_ingredient_instantiation()
    test_ingredient_restrictions()
    test_ingredient_repr()
    test_ingredient_eq()
    test_ingredient_not_eq()
    test_ingredient_hash_equal()
    test_ingredient_hash_not_equal()
    test_ingredient_repr_incorrect()
    test_ingredient_name()


def test_ingredient_instantiation():
    ingredient = Ingredient("queijo")
    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == "queijo"


def test_ingredient_restrictions():
    ingredient = Ingredient("queijo")
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    print(ingredient.restrictions)
    assert ingredient.restrictions == expected_restrictions


def test_ingredient_repr():
    ingredient = Ingredient("queijo")
    assert repr(ingredient) == "Ingredient('queijo')"


def test_ingredient_eq():
    ingredient1 = Ingredient("queijo")
    ingredient2 = Ingredient("queijo")
    assert ingredient1 == ingredient2


def test_ingredient_not_eq():
    ingredient1 = Ingredient("queijo")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 != ingredient2


@pytest.mark.xfail(strict=True)
def test_ingredient_hash_equal():
    ingredient1 = Ingredient("queijo")
    ingredient2 = Ingredient("queijo")
    assert hash(ingredient1) == hash(ingredient2)


@pytest.mark.xfail(strict=True)
def test_ingredient_hash_not_equal():
    ingredient1 = Ingredient("queijo")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)


@pytest.mark.xfail(strict=True)
def test_ingredient_repr_incorrect():
    ingredient = Ingredient("queijo")
    assert repr(ingredient) != "Ingredient('bacon')"


def test_ingredient_name():
    ingredient = Ingredient("queijo")
    assert ingredient.name == "queijo"
