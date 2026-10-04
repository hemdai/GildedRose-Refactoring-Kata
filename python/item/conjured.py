from item.item import UpdatableItem

class ConjuredItem(UpdatableItem):
    """Conjured items degrade twice as fast: -2/day, -4/day after sell date."""
    def update(self):
        self.item.sell_in -= 1
        self.decrease_quality(2)
        if self.item.sell_in < 0:
            self.decrease_quality(2)
