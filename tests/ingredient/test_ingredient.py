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
    test_ingredient_name()
    test_ingredient_repr_incorrect()


def test_ingredient_instantiation():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("manteiga")

    assert isinstance(ingredient1, Ingredient)
    assert ingredient1 == ingredient2


def test_ingredient_restrictions():
    ingredient = Ingredient("manteiga")
    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredient.restrictions == expected_restrictions


def test_ingredient_repr():
    ingredient = Ingredient("manteiga")
    assert repr(ingredient) == "Ingredient('manteiga')"


def test_ingredient_eq():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("manteiga")
    assert ingredient1 == ingredient2


def test_ingredient_not_eq():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 != ingredient2


def test_ingredient_hash_equal():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("manteiga")
    assert hash(ingredient1) == hash(ingredient2)


def test_ingredient_hash_not_equal():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)


def test_ingredient_repr_incorrect():
    ingredient = Ingredient("manteiga")
    assert repr(ingredient) != "Ingredient('bacon')"


def test_ingredient_name():
    ingredient = Ingredient("manteiga")
    assert ingredient.name == "manteiga"
