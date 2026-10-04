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

class BackstagePass(UpdatableItem):
    """Backstage passes: value rises as concert nears, drops to 0 after.

    +1 normally, +2 within 10 days, +3 within 5 days, 0 after concert.
    """
    def update(self):
        self.item.sell_in -= 1
        # Check Logic from smaller due to less value has multiple declaration
        if self.item.sell_in < 0:
            self.item.quality = 0
            return
        if self.item.sell_in < 5:
            self.increase_quality(3)
            return
        if self.item.sell_in < 10:
            self.increase_quality(2)
            return
        self.increase_quality()

class ConjuredItem(UpdatableItem):
    def update(self):
        self.item.sell_in -= 1
        self.decrease_quality(2)
        if self.item.sell_in < 0:
            self.decrease_quality(2)

class ItemFactory:
    """Maps an item's name to the right UpdatableItem.

    Add new item types here only — no other code needs to change.
    """
    @staticmethod
    def create_item(item:Item):
        if item.name == "Aged Brie":
            return AgedBrie(item)
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        if item.name.startswith("Backstage passes"):
            return BackstagePass(item)
        if item.name.startswith("Conjured"):
            return ConjuredItem(item)
        return NormalItem(item)
