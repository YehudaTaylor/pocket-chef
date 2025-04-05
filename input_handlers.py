from abc import ABC, abstractmethod
from typing import List
import cv2

class IngredientInput(ABC):
    @abstractmethod
    def get_ingredients(self) -> List[str]:
        pass

class TextInput(IngredientInput):
    def __init__(self, ingredients_text: str):
        self.ingredients_text = ingredients_text

    def get_ingredients(self) -> List[str]:
        return [ing.strip() for ing in self.ingredients_text.split(',')]

class ImageInput(IngredientInput):
    def __init__(self, image_path: str):
        self.image_path = image_path

    def get_ingredients(self) -> List[str]:
        # This is a placeholder for actual image recognition logic
        image = cv2.imread(self.image_path)
        return ["placeholder_ingredient"] 