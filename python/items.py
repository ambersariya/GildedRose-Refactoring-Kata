class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def reduce_sell_in(self):
        self.sell_in -= 1

    def increase_item_quality(self):
        pass

    def decrease_item_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def tick(self):
        self.reduce_sell_in()
        self.increase_item_quality()
        self.decrease_item_quality()


class Sulfuras(Item):
    def reduce_sell_in(self):
        pass

    def increase_item_quality(self):
        pass

    def decrease_item_quality(self):
        pass


class AgedBrie(Item):
    def increase_item_quality(self):
        if self.quality < 50:
            self.quality += 1

    def decrease_item_quality(self):
        pass


class BackstagePasses(Item):
    def increase_item_quality(self):
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 11:
            self.quality += 1
        if self.sell_in < 6:
            self.quality += 1

    def decrease_item_quality(self):
        if self.sell_in < 0:
            self.quality = 0


class ItemFactory:
    def create_item(name: str, sell_in: int, quality: int):
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)
