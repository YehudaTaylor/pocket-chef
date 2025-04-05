from models import Recipe, CookingStyle, SkillLevel
from input_handlers import IngredientInput
from recipe_generator import RecipeGenerator

class PocketChef:
    def __init__(self):
        self.recipe_generator = RecipeGenerator()

    def create_recipe(
        self,
        ingredient_input: IngredientInput,
        style: CookingStyle,
        max_time: int,
        skill_level: SkillLevel
    ) -> Recipe:
        ingredients = ingredient_input.get_ingredients()
        return self.recipe_generator.generate_recipe(
            ingredients,
            style,
            max_time,
            skill_level
        )

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
    
    # Image input example
    image_input = ImageInput("ingredients.jpg")
    recipe = chef.create_recipe(
        image_input,
        CookingStyle.ASIAN,
        45,
        SkillLevel.INTERMEDIATE
    )

if __name__ == "__main__":
    main()


