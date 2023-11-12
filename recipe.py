
import requests
from PyQt5 import QtWidgets, QtGui

def lookupRecipe(ingredients):
    
    api_key = "feb2cce07b13419da30cffe281bfc4a1"  
    query = ingredients.replace(" ", "+")
    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={query}"
    response = requests.get(url)
    data = response.json()

    recipe = data[0]["title"] + "\n"
    recipe += "Instructions: " + data[0]["instructions"] + "\n"
    recipe += "Servings: " + str(data[0]["servings"]) + "\n"
    ingredients = data[0]["extendedIngredients"]
    recipe += "Ingredients: \n"
    for ingredient in ingredients:
        recipe += " - " + ingredient["original"] + "\n"
    return recipe

def lookupImageURL(ingredients):
    api_key = "feb2cce07b13419da30cffe281bfc4a1"
    query = ingredients.replace(" ", "+")
    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={query}"
    response = requests.get(url)
    data = response.json()

    image_url = data[0]["image"]
    return image_url

class RecipeGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ingredients_label = QtWidgets.QLabel("Ingredients or nationality/cuisine:", self)
        self.ingredients_input = QtWidgets.QLineEdit(self)
        generate_button = QtWidgets.QPushButton("Generate Recipe", self)
        generate_button.clicked.connect(self.generateRecipe)
        self.recipe_label = QtWidgets.QLabel(self)
        self.image_label = QtWidgets.QLabel(self)
        input_layout = QtWidgets.QHBoxLayout()
        input_layout.addWidget(ingredients_label)


