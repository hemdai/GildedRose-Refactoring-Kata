from item.aged_brie import AgedBrie
from item.sulfuras import Sulfuras
from item.backstage_pass import BackstagePass
from item.conjured import ConjuredItem
from item.normal import NormalItem
from item.item import Item


class ItemFactory:
    """Maps an item's name to the right UpdatableItem.

    Add new item types here only — no other code needs to change.
    """

    @staticmethod
    def create_item(item: Item):
        if item.name == "Aged Brie":
            return AgedBrie(item)
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        if item.name.startswith("Backstage passes"):
            return BackstagePass(item)
        if item.name.startswith("Conjured"):
            return ConjuredItem(item)
        return NormalItem(item)
