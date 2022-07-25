# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                return
            self.reduce_sell_in(item)

            if item.name == "Aged Brie":
                if item.quality < 50:
                    self.increase_item_quality(item)
                return

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    self.increase_item_quality(item)
                if item.sell_in < 11:
                    self.increase_item_quality(item)
                if item.sell_in < 6:
                    self.increase_item_quality(item)
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality
                return

            if item.quality > 0:
                self.decrease_item_quality(item)

    def reduce_sell_in(self, item):
        item.sell_in -= 1

    def increase_item_quality(self, item):
        item.quality += 1

    def decrease_item_quality(self, item):
        item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
