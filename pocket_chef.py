from models import Recipe, CookingStyle, SkillLevel
from input_handlers import IngredientInput
from recipe_generator import RecipeGenerator
from input_handlers import TextInput, ImageInput
import json
from datetime import datetime
import os

class PocketChef:
    def __init__(self):
        self.recipe_generator = RecipeGenerator()
        self.recipes_dir = "recipes"
        os.makedirs(self.recipes_dir, exist_ok=True)

    def create_recipe(
        self,
        ingredient_input: IngredientInput,
        style: CookingStyle,
        max_time: int,
        skill_level: SkillLevel
    ) -> Recipe:
        ingredients = ingredient_input.get_ingredients()
        recipe = self.recipe_generator.generate_recipe(
            ingredients,
            style,
            max_time,
            skill_level
        )
        self._save_recipe(recipe)
        return recipe

    def _save_recipe(self, recipe: Recipe):
        """Save recipe to JSON file with timestamp"""
        recipe_data = {
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions,
            "cooking_time": recipe.cooking_time,
            "skill_level": recipe.skill_level.value,
            "style": recipe.style.value,
            "created_at": datetime.now().isoformat()
        }
        
        filename = f"{recipe.name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.recipes_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(recipe_data, f, indent=2)

    def get_recipe_history(self) -> list[dict]:
        """Retrieve all saved recipes"""
        recipes = []
        for filename in os.listdir(self.recipes_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.recipes_dir, filename), 'r') as f:
                    recipes.append(json.load(f))
        return sorted(recipes, key=lambda x: x['created_at'], reverse=True)

# Example usage
def main():
    chef = PocketChef()
    
    # Text input example
    text_input = TextInput("tomatoes, onions, garlic, pasta")
    recipe = chef.create_recipe(
        text_input,
        CookingStyle.ITALIAN,
        30,
        SkillLevel.BEGINNER
    )
    print(recipe)
    
    # Save recipe to a file
    # with open(f"{recipe.name.lower().replace(' ', '_')}_recipe.txt", 'w') as f:
    #     f.write(f"Recipe: {recipe.name}\n\n")
    #     f.write("Ingredients:\n")
    #     for ingredient in recipe.ingredients:
    #         f.write(f"- {ingredient}\n")
    #     f.write("\nInstructions:\n")
    #     for i, instruction in enumerate(recipe.instructions, 1):
    #         f.write(f"{i}. {instruction}\n")
    #     f.write(f"\nCooking Time: {recipe.cooking_time} minutes")
    #     f.write(f"\nSkill Level: {recipe.skill_level.value}")
    #     f.write(f"\nStyle: {recipe.style.value}")
    # Image input example
    # image_input = ImageInput("ingredients.jpg")
    # recipe = chef.create_recipe(
    #     image_input,
    #     CookingStyle.ASIAN,
    #     45,
    #     SkillLevel.INTERMEDIATE
    # )

if __name__ == "__main__":
    main()


