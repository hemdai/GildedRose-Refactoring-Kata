# -*- coding: utf-8 -*-
from item.item import Item, ItemFactory
from typing import List


class GildedRose:

    def __init__(self, items: List[Item]):
        self.items = [ItemFactory.create_item(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()
        return self.items
