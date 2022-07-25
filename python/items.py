MAX_QUALITY = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _reduce_sell_in(self):
        self.sell_in -= 1

    def _increase_item_quality(self):
        pass

    def _decrease_item_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def tick(self):
        self._reduce_sell_in()
        self._increase_item_quality()
        self._decrease_item_quality()


class Sulfuras(Item):
    def _reduce_sell_in(self):
        pass

    def _increase_item_quality(self):
        pass

    def _decrease_item_quality(self):
        pass


class AgedBrie(Item):
    def _increase_item_quality(self):
        if self.quality < MAX_QUALITY:
            self.quality += 1

    def _decrease_item_quality(self):
        pass


class BackstagePasses(Item):
    def _increase_item_quality(self):
        if self.quality < MAX_QUALITY:
            self.quality += 1

        if self.quality < MAX_QUALITY:
            if self.sell_in < 11:
                self.quality += 1
            if self.sell_in < 6:
                self.quality += 1

    def _decrease_item_quality(self):
        if self.sell_in < 0:
            self.quality = 0


def CreateItem(name: str, sell_in: int, quality: int):
    if name == "Sulfuras, Hand of Ragnaros":
        return Sulfuras(name, sell_in, quality)
    if name == "Aged Brie":
        return AgedBrie(name, sell_in, quality)
    if name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePasses(name, sell_in, quality)
    return Item(name, sell_in, quality)
