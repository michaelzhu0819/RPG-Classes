"""This includes the class, child classes and different
functions that generates the map and accepts user inputs"""


# class that initializes the map tiles and coords
class map_tiles:
    def __init__(self, x, y, Map):
        self.x = x
        self.y = y
        self.mapp = Map

    def friendly_tile():
        print("\nnothing here")

    def enemy_tile():
        print("\nenmey here!")

    def loot_tile():
        print("\nthis is a loot location!")

    def start():
        print("\nyou started here")

    def key_tile(val):
        if val == 1:
            print("\nyou came across a key")
            val -= 1
        else:
            print("\nnothing here")
        thing = val
        return thing


def game_end(key):
    if key < 1:
        print("\nYou came across a mysteriously locked door, " +
              "need a key to unlock")
    else:
        print("\nyou have opened the door to your freedom")


# The reaction of users movement
class MapReaction(map_tiles):
    def __init__(self, x, y, Map):
        super().__init__(x, y, Map)
        try:
            if self.x < 0 or self.y < 0:  # so that you can't teleport
                print("You can't go in that direction anymore!")
                self.x = loca_reset(self.x)
                self.y = loca_reset(self.y)

            # Actual reactions from the map
            if self.mapp[self.x][self.y] == "nothing":
                map_tiles.friendly_tile()
            elif self.mapp[self.x][self.y] == "enemy":
                map_tiles.enemy_tile()
            elif self.mapp[self.x][self.y] == "supply":
                map_tiles.loot_tile()
            elif self.mapp[self.x][self.y] == "start":
                map_tiles.start()
            elif self.mapp[self.x][self.y] == "key":
                print("this will be the key place")
            elif self.mapp[self.x][self.y] == "end":
                print("this will the end of the game")

        except IndexError:  # The border of the map
            print("\nYou can't go in that direction anymore!")
            self.x = loca_reset(self.x)
            self.y = loca_reset(self.y)


# Resets coords if they are of an unacceptable value
def loca_reset(x):
    coord_x = x
    if x > 3 or x < 0:
        if x > 3:
            coord_x -= 1
        elif x < 0:
            coord_x += 1
    return coord_x


# Makes and prints out the map
def Map():
    Map = [["end", "enemy", "enemy", "key"],
           ["supply", "nothing", "nothing", "enemy"],
           ["nothing", "start", "supply", "nothing"],
           ["enemy", "supply", "nothing", "enemy"]]

    print("\n*---------------------------------------*")
    for i in Map:
        print("|", end=" ")
        for j in i:
            print(j, end="")
            for k in range(8 - len(j)):
                print(" ", end="")
            print("|", end=" ")
        print("\n*---------------------------------------*")
