# exploration inventory
def explore_inv(exploring_bag):
    exploring_bag = {
        "woter bottle": {
            "description": "a common woter bottle",
            "stats": "+2 focus",
            "usage": "2"
        },
        "first aid": {
            "description":
            "a first aid kit capable of healing fatal" + " wounds",
            "stats": "full heal, boost health to 8 and focus " + "to 15",
            "usage": "1"
        },
        "monke bar": {
            "description": "a tasty monke bar",
            "stats": "+4 health and +5 focus",
            "usage": "2"
        }
    }
    return exploring_bag


# Combat inventory
def combat_inv(combat_pouch):
    combat_pouch = {
        "fist": {
            "description": "your fist",
            "stats": "1 damage",
            "cooldown": None
        },
        "pistol": {
            "description": "a small firearm capable of piercing armor",
            "stats": "5 damage",
            "cooldown": "one round"
        },
        "knife": {
            "description": "a dull knife that does more than your fist",
            "stats": "2 damage",
            "cooldown": None
        },
        "grenade": {
            "description":
            "a high powered explosive with devastating " + "powers",
            "stats": "10 damage",
            "cooldown": "1 use per fight"
        }
    }
    return combat_pouch
