# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from parameterized import parameterized


class GildedRoseTest(unittest.TestCase):
    @parameterized.expand([
        ('Foo', 0, 0, -1, 0),
        ('Aged Brie', 1, 1, 0, 2),
        ('Aged Brie', 10, 50, 9, 50),
        ('Sulfuras, Hand of Ragnaros', 10, 80, 10, 80),
        ('Sulfuras, Hand of Ragnaros', -1, 80, -1, 80),
        ('Backstage passes to a TAFKAL80ETC concert', 15, 10, 14, 11),
        ('Backstage passes to a TAFKAL80ETC concert', 10, 10, 9, 12),
        ('Backstage passes to a TAFKAL80ETC concert', 4, 10, 3, 13),
        ('Backstage passes to a TAFKAL80ETC concert', -1, 10, -2, 0),
    ])
    def test_item(self, item_name, sell_in, quality, expected_sell_in, expected_quality):
        items = [Item(item_name, sell_in=sell_in, quality=quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(item_name, items[0].name)
        self.assertEquals(expected_quality, items[0].quality)
        self.assertEquals(expected_sell_in, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()