# Data models
class ClothingItem:
    def __init__(self, name, category, frequency, size):
        self.name = name
        self.category = category
        self.frequency = frequency  # times worn per week
        self.size = size            # space required


class Shelf:
    def __init__(self, shelf_id, capacity, accessibility_rank):
        self.shelf_id = shelf_id
        self.capacity = capacity
        self.remaining_space = capacity
        self.accessibility_rank = accessibility_rank
        self.items = []


def arrange_clothes(clothes, shelves):
    """
    clothes  : list of ClothingItem
    shelves  : list of Shelf
    returns  : mapping of clothing item to shelf
    """

    # Step 1: Sort clothes by frequency (most used first)
    clothes.sort(key=lambda x: x.frequency, reverse=True)

    # Step 2: Sort shelves by accessibility (best first)
    shelves.sort(key=lambda x: x.accessibility_rank)

    # Step 3: Group clothes by category
    category_map = {}
    for item in clothes:
        if item.category not in category_map:
            category_map[item.category] = []
        category_map[item.category].append(item)

    # Step 4: Placement
    item_location = {}

    for category in category_map:
        for item in category_map[category]:
            placed = False

            for shelf in shelves:
                if shelf.remaining_space >= item.size:
                    shelf.items.append(item)
                    shelf.remaining_space -= item.size
                    item_location[item.name] = shelf.shelf_id
                    placed = True
                    break

            if not placed:
                raise Exception("Insufficient space in almirah")

    return item_location


def find_item(item_name, item_location):
    """
    Returns shelf number for quick lookup
    """
    return item_location.get(item_name, "Item not found")
