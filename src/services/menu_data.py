import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str):
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = self._get_or_create_dish(dish_name, dish_price)
                ingredient = self._get_or_create_ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish

    def _get_or_create_ingredient(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient

        ingredient = Ingredient(name)
        self.ingredients.add(ingredient)
        return ingredient
