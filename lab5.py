class Furniture:
    """
    Represents a piece of furniture in a room.

    """

    def __init__(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        self._name = name
        self._coordinate = coordinate

    def __del__(self):
        pass

    def __str__(self):
        return f"room:{self._name}"


class Room:
    """
    Represents a room that can contain multiple pieces of furniture.

    """

    def __init__(self):
        self.furniture = []
        self.room_name = "Living Room"

    def set_room_name(self, room_name):
        """
        Set the name of the room.
        """
        self.room_name = room_name

    def get_room_name(self):
        """
        Get the name of the room.
        """
        return self.room_name

    def add_furniture(self, name, coordinate):
        """
        Add a new piece of furniture_of_room to the room.
        """
        furniture_of_room = Furniture(name, coordinate)
        self.furniture.append(furniture_of_room)

    def remove_furniture(self, name):
        """
        Remove a piece of furniture from the room by name.
        """
        self.furniture = [item for item in self.furniture if item.name != name]

    def rearrangement(self, name, new_coordinate):
        """
        Change the coordinates of a specific piece of FURNITURE.
        """
        for furniture_of_room in self.furniture:
            if furniture_of_room.name == name:
                furniture_of_room.coordinate = new_coordinate

    def get_room_layout(self):
        """
        Get a dictionary representing the lay_out of the room,
        mapping furniture_of_room names to coordinates.
        """
        lay_out = {}
        for furniture_of_room in self.furniture:
            lay_out[furniture_of_room.name] = furniture_of_room.coordinate
        return lay_out

    def __del__(self):
        self.furniture = []


my_room = Room()
print("Room name:", my_room.get_room_name())
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
