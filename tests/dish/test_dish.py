import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    test_dish_instantiation()
    test_dish_repr()
    test_dish_eq()
    test_dish_not_eq()
    test_dish_hash_equal()
    test_dish_hash_not_equal()
    test_dish_add_ingredient_dependency()
    test_dish_invalid_price_type()
    test_dish_invalid_price_value()
    test_dish_recipe_get_quantity()
    test_dish_get_restrictions()
    test_dish_get_ingredients()


def test_dish_instantiation():
    dish = Dish("Lasagna", 25.0)
    assert isinstance(dish, Dish)
    assert dish.name == "Lasagna"
    assert dish.price == 25.0
    assert dish.recipe == {}


def test_dish_repr():
    dish = Dish("Lasagna", 25.0)
    assert repr(dish) == "Dish('Lasagna', R$25.00)"


def test_dish_eq():
    dish1 = Dish("Lasagna", 25.0)
    dish2 = Dish("Lasagna", 25.0)
    assert dish1 == dish2


def test_dish_not_eq():
    dish1 = Dish("Lasagna", 25.0)
    dish2 = Dish("Spaghetti", 15.0)
    assert dish1 != dish2


@pytest.mark.xfail(strict=True)
def test_dish_hash_equal():
    dish1 = Dish("Lasagna", 25.0)
    dish2 = Dish("Lasagna", 25.0)
    assert hash(dish1) == hash(dish2)


@pytest.mark.xfail(strict=True)
def test_dish_hash_not_equal():
    dish1 = Dish("Lasagna", 25.0)
    dish2 = Dish("Spaghetti", 15.0)
    assert hash(dish1) != hash(dish2)


def test_dish_add_ingredient_dependency():
    dish = Dish("Lasagna", 25.0)
    ingredient = Ingredient("cheese")
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe[ingredient] == 2


def test_dish_invalid_price_type():
    with pytest.raises(TypeError):
        Dish("Lasagna", "25.0")


def test_dish_invalid_price_value():
    with pytest.raises(ValueError):
        Dish("Lasagna", -10.0)


def test_dish_recipe_get_quantity():
    dish = Dish("Lasagna", 25.0)
    ingredient = Ingredient("cheese")
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe.get(ingredient) == 2


def test_dish_get_restrictions():
    dish = Dish("Lasagna", 25.0)
    ingredient1 = Ingredient("cheese")
    ingredient2 = Ingredient("tomato")
    ingredient3 = Ingredient("beef")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 3)
    dish.add_ingredient_dependency(ingredient3, 1)
    expected_restrictions = {
        ingredient1.restrictions,
        ingredient2.restrictions,
        ingredient3.restrictions,
    }
    assert dish.get_restrictions() == expected_restrictions


def test_dish_get_ingredients():
    dish = Dish("Lasagna", 25.0)
    ingredient1 = Ingredient("cheese")
    ingredient2 = Ingredient("tomato")
    ingredient3 = Ingredient("beef")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 3)
    dish.add_ingredient_dependency(ingredient3, 1)
    expected_ingredients = {ingredient1, ingredient2, ingredient3}
    assert dish.get_ingredients() == expected_ingredients
