from item.item import UpdatableItem
class NormalItem(UpdatableItem):
    """Standard item: -1/day before sell date, -2/day after."""
    def update(self):
        self.item.sell_in -= 1
        self.decrease_quality()
        if self.item.sell_in < 0:
            self.decrease_quality()
