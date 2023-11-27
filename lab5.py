import pylint
class Furniture:
    """
    Represents a piece of furniture in a room.

    """

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates


class Room:
    """
    Represents a room that can contain multiple pieces of furniture.

    """

    def __init__(self):
        self.furniture = []

    def add_furniture(self, name, coordinates):
        """
        Add a new piece of furniture to the room.
        """
        furniture = Furniture(name, coordinates)
        self.furniture.append(furniture)

    def remove_furniture(self, name):
        """
        Remove a piece of furniture from the room by name.
        """
        self.furniture = [item for item in self.furniture if item.name != name]

    def rearrangement(self, name, new_coordinates):
        """
        Change the coordinates of a specific piece of furniture.
        """
        for furniture in self.furniture:
            if furniture.name == name:
                furniture.coordinates = new_coordinates

    def get_room_layout(self):
        """
        Get a dictionary representing the layout of the room, mapping furniture names to coordinates.
        """
        layout = {}
        for furniture in self.furniture:
            layout[furniture.name] = furniture.coordinates
        return layout


my_room = Room()

my_room.add_furniture("Bed", (1, 2))
my_room.add_furniture("Table", (3, 4))
my_room.add_furniture("Carpet", (5, 6))
my_room.add_furniture("Shelf", (7, 8))
my_room.add_furniture("Closet", (9, 0))
print("initial layout")
layout = my_room.get_room_layout()
for furniture, coordinates in layout.items():
    print(f"{furniture}: {coordinates}")

my_room.remove_furniture("Table")
my_room.remove_furniture("Carpet")

my_room.rearrangement("Bed", (11, 12))
my_room.rearrangement("Closet", (13, 14))

layout = my_room.get_room_layout()
for furniture, coordinates in layout.items():
    print(f"{furniture}: {coordinates}")
