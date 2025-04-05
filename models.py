from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class CookingStyle(Enum):
    ITALIAN = "Italian"
    ASIAN = "Asian"
    VEGAN = "Vegan"
    COMFORT = "Comfort Food"

class SkillLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

@dataclass
class Recipe:
    name: str
    ingredients: List[str]
    instructions: List[str]
    cooking_time: int  # in minutes
    skill_level: SkillLevel
    style: CookingStyle
    nutritional_info: Optional[dict] = None 