# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.tick()
