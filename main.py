from pocket_chef import PocketChef
from input_handlers import TextInput, ImageInput
from models import CookingStyle, SkillLevel

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