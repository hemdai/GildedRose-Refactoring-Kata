from abc import ABC, abstractmethod
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class UpdatableItem(ABC):
    def __init__(self, item: Item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

    def increase_quality(self, amount=1):
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(0, self.item.quality - amount)

class NormalItem(UpdatableItem):
    def update(self):
        self.item.sell_in -= 1
        self.decrease_quality()
        if self.item.sell_in < 0:
            self.decrease_quality()

class AgedBrie(UpdatableItem):
    """Aged Brie updater.
    Aged Brie doesn't have problem with time
    Rule:
        - Before sell date: quality +1
        - After sell date: quality +2
    """
    def update(self):
        self.item.sell_in -= 1
        self.increase_quality()
        if self.item.sell_in < 0:
            self.increase_quality()

class Sulfuras(UpdatableItem):
    """ Legendary item — never changes (sell_in and quality stay fixed). """
    def update(self):
        pass

class ItemFactory:
    @staticmethod
    def create_item(item:Item):
        return NormalItem(item)
