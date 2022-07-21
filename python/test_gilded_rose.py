# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_aged_brie_increases_in_quality_with_its_sell_in_date(self):
        items = [Item("Aged Brie", sell_in=1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(2, items[0].quality)

    def test_aged_brie_doesnt_increases_in_quality_when_its_already_at_max(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_not_increase_in_quality_for_sulfuras_within_sell_in_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

    def test_not_increase_in_quality_for_sulfuras_when_not_in_sell_in_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

    def test_backstage_passes_increase_in_value_by_1_when_above_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(14, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    def test_backstage_passes_increase_in_value_by_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(12, items[0].quality)

    def test_backstage_passes_increase_in_value_by_3_when_below_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(3, items[0].sell_in)
        self.assertEquals(13, items[0].quality)

    def test_backstage_passes_drop_quality_to_0_after_sellin_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
