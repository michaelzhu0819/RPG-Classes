""" These classes and functions define the four characters in the game"""


# The general class for all the characters
class characters:
    def __init__(self, hp, damage, focus):
        self.hp = hp
        self.damage = damage
        self.focus = focus


class beserker(characters):
    def __init__(self, hp, damage, focus):
        super().__init__(hp, damage, focus)
        self.hp = 100
        self.damage = 20
        self.focus = 15
        print("-beserker can do high damage when health and/or focus is low\n")


class healer(characters):
    def __init__(self, hp, damage, focus):
        super().__init__(hp, damage, focus)
        self.hp = 150
        self.damage = 18
        self.focus = 12
        print("-healer can heal themselves every 5 rounds")


class mage(characters):
    def __init__(self, hp, damage, focus):
        super().__init__(hp, damage, focus)
        self.hp = 80
        self.damage = 29
        self.focus = 14
        print(
            "-mage have high damage and can have less cooldown on weapons " +
            "and healing items")


class tank(characters):
    def __init__(self, hp, damage, focus):
        super().__init__(hp, damage, focus)
        self.hp = 200
        self.damage = 14
        self.focus = 8
        print("-tank can have +100% health as the start of the game")
