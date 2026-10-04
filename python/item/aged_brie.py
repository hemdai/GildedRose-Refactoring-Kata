from item.item import UpdatableItem


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
