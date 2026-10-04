from item.item import UpdatableItem


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
