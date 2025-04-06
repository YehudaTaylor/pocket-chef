from typing import List
from models import Recipe, CookingStyle, SkillLevel
import openai
from openai import OpenAI

class RecipeGenerator:
    def __init__(self):
        self.available_recipes = []  # This would be populated from a database

    def generate_recipe(
        self,
        ingredients: List[str],
        style: CookingStyle,
        max_time: int,
        skill_level: SkillLevel
    ) -> Recipe:

        client = OpenAI()

        # Prepare the prompt for GPT-4
        prompt = f"""Create a recipe using these ingredients: {', '.join(ingredients)}
        Style: {style.value}
        Maximum cooking time: {max_time} minutes
        Skill level: {skill_level.value}
        
        Please provide:
        1. A creative recipe name
        2. Step-by-step instructions
        3. Estimated cooking time
        4. Any additional tips or notes"""

        # Call GPT-4 API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional chef creating detailed recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Parse the response
        recipe_text = response.choices[0].message.content
        
        # Extract recipe components 
        lines = recipe_text.split('\n')
        name = lines[0].strip()
        instructions = [line.strip() for line in lines[2:] if line.strip()]

        return Recipe(
            name=name,
            ingredients=ingredients,
            instructions=instructions,
            cooking_time=max_time,  # Using the requested max_time
            skill_level=skill_level,
            style=style
        )