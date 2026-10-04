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
