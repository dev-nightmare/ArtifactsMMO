from enum import Enum


class Enum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value == value:
                return member
        return None


class Sort(Enum):
    
    """Needs for method 'get_all_characters' in class 'Game'"""

    WOODCUTTING = "woodcutting"
    MINING = "mining"
    FISHING = "fishing"
    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    GOLD = "gold"
    DEFAULT = None


class ContentType(Enum):

    """Needs for method 'get_all_maps' in class 'Game'"""

    MONSTER = "monster"
    RESOURCE = "resource"
    WORKSHOP = "workshop"
    BANK = "bank"
    GRAND_EXCHANGE = "grand_exchange"
    TASKS_MASTER = "tasks_master"
    DEFAULT = None


class Type(Enum):

    """Needs for method 'get_all_items' in class 'Game'"""

    CONSUMABLE = "consumable"
    BODY_ARMOR = "body_armor"
    WEAPON = "weapon"
    RESOURCE = "resource"
    LEG_ARMOR = "leg_armor"
    HELMET = "helmet"
    BOOTS = "boots"
    SHIELD = "shield"
    AMULET = "amulet"
    RING = "ring"
    DEFAULT = None


class CraftSkill(Enum):

    """Needs for method 'get_all_items' in class 'Game'"""

    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    WOODCUTTING = "woodcutting"
    MINING = "mining"
    DEFAULT = None


class Skill(Enum):

    """Needs for method 'get_all_resources' in class 'Game'"""

    MINING = "mining"
    WOODCUTTING = "woodcutting"
    FISHING = "fishing"
    DEFAULT = None


class Skin(Enum):

    """Needs for method 'create_character' in class 'MyAccount'"""

    MEN1 = "men1"
    MEN2 = "men2"
    MEN3 = "men3"
    WOMEN1 = "women1"
    WOMEN2 = "women2"
    WOMEN3 = "women3"


class Slot(Enum):

    """Needs for methods 'equip' and 'unequip' in class 'MyCharacter'"""

    WEAPON = "weapon"
    SHIELD = "shield"
    HELMET = "helmet"
    BODY_ARMOR = "body_armor"
    LEG_ARMOR = "leg_armor"
    BOOTS = "boots"
    RING1 = "ring1"
    RING2 = "ring2"
    AMULET = "amulet"
    ARTIFACT1 = "artifact1"
    ARTIFACT2 = "artifact2"
    ARTIFACT3 = "artifact3"
    CONSUMABLE1 = "consumable1"
    CONSUMABLE2 = "consumable2"
