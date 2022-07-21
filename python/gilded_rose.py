# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_quality_aged_brie(self, item):
        if item.quality < 50:
            self.increase_item_quality(item)

    def update_quality_backstage_passes(self, item):
        if item.quality < 50:
            self.increase_item_quality(item)
        if item.sell_in < 11:
            self.increase_item_quality(item)
        if item.sell_in < 6:
            self.increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = 0

    @staticmethod
    def decrease_item_quality(item):
        item.sell_in = item.sell_in - 1

    @staticmethod
    def increase_item_quality(item):
        item.quality = item.quality + 1

    def update_item_quality(self, item):
        if item.name == SULFURAS:
            return

        if item.name == AGED_BRIE:
            self.update_quality_aged_brie(item)

        if item.name == BACKSTAGE_PASSES:
            self.update_quality_backstage_passes(item)

        self.decrease_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
