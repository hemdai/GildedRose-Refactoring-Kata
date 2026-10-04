# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
import gilded_rose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].name,"foo")

    def test_normal_item_quality_decreases(self):
        items = [Item("Charger cable type C", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality,19)
        self.assertEqual(items[0].sell_in, 9)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)


if __name__ == '__main__':
    unittest.main()
