# Create a new file called recipe_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from models import CookingStyle, SkillLevel
from input_handlers import TextInput

class RecipeGUI:
    def __init__(self, chef):
        self.chef = chef
        self.root = None
        self.ingredients_entry = None
        self.style_var = None
        self.time_var = None
        self.skill_var = None

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Pocket Chef Recipe Generator")
        self.root.geometry("400x500")
        self._create_widgets()
        self.root.mainloop()

    def _create_widgets(self):
        # Ingredients input
        tk.Label(self.root, text="Ingredients (comma-separated):").pack(pady=5)
        self.ingredients_entry = tk.Entry(self.root, width=40)
        self.ingredients_entry.pack(pady=5)

        # Cooking style dropdown
        tk.Label(self.root, text="Cooking Style:").pack(pady=5)
        self.style_var = tk.StringVar()
        style_combo = ttk.Combobox(self.root, textvariable=self.style_var)
        style_combo['values'] = [style.value for style in CookingStyle]
        style_combo.set(CookingStyle.ITALIAN.value)
        style_combo.pack(pady=5)

        # Cooking time input
        tk.Label(self.root, text="Maximum Cooking Time (minutes):").pack(pady=5)
        self.time_var = tk.StringVar(value="30")
        time_entry = tk.Entry(self.root, textvariable=self.time_var, width=10)
        time_entry.pack(pady=5)

        # Skill level dropdown
        tk.Label(self.root, text="Skill Level:").pack(pady=5)
        self.skill_var = tk.StringVar()
        skill_combo = ttk.Combobox(self.root, textvariable=self.skill_var)
        skill_combo['values'] = [level.value for level in SkillLevel]
        skill_combo.set(SkillLevel.BEGINNER.value)
        skill_combo.pack(pady=5)

        # Generate button
        tk.Button(self.root, text="Generate Recipe", command=self._generate_recipe).pack(pady=20)

    def _generate_recipe(self):
        try:
            ingredients = self.ingredients_entry.get()
            style = CookingStyle(self.style_var.get())
            max_time = int(self.time_var.get())
            skill_level = SkillLevel(self.skill_var.get())

            text_input = TextInput(ingredients)
            recipe = self.chef.create_recipe(
                text_input,
                style,
                max_time,
                skill_level
            )
            
            self._show_recipe_window(recipe)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _show_recipe_window(self, recipe):
        recipe_window = tk.Toplevel(self.root)
        recipe_window.title(recipe.name)
        recipe_window.geometry("600x400")
        
        text_widget = tk.Text(recipe_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill='both', padx=10, pady=10)
        
        recipe_text = f"""Recipe: {recipe.name}

                    Ingredients:
                    {chr(10).join(f'- {ing}' for ing in recipe.ingredients)}

                    Instructions:
                    {chr(10).join(f'{i+1}. {inst}' for i, inst in enumerate(recipe.instructions))}

                    Cooking Time: {recipe.cooking_time} minutes
                    Skill Level: {recipe.skill_level.value}
                    Style: {recipe.style.value}"""
        
        text_widget.insert('1.0', recipe_text)
        text_widget.config(state='disabled')
