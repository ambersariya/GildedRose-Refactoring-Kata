import { Item, GildedRose } from "@/gilded-rose";

describe("Gilded Rose Should", () => {
  it("foo", () => {
    const gildedRose = new GildedRose([new Item("foo", 0, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("foo");
    expect(items[0].quality).toBe(0);
    expect(items[0].sellIn).toBe(-1);
  });

  it("increase Aged Brie's quality by 1 the next day", () => {
    const gildedRose = new GildedRose([new Item("Aged Brie", 1, 1)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Aged Brie");
    expect(items[0].quality).toBe(2);
    expect(items[0].sellIn).toBe(0);
  });

  it("not increase Aged Brie's quality when it has aged by max amount", () => {
    const gildedRose = new GildedRose([new Item("Aged Brie", 1, 50)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Aged Brie");
    expect(items[0].quality).toBe(50);
    expect(items[0].sellIn).toBe(0);
  });

  it("not increase quality for Sulfuras, Hand of Ragnaros", () => {
    const gildedRose = new GildedRose([
      new Item("Sulfuras, Hand of Ragnaros", 1, 1),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Sulfuras, Hand of Ragnaros");
    expect(items[0].quality).toBe(1);
    expect(items[0].sellIn).toBe(1);
  });

  it("increase quality of Backstage passes to a TAFKAL80ETC concert  by 2 when sell in is less than 10 days", () => {
    const gildedRose = new GildedRose([
      new Item("Backstage passes to a TAFKAL80ETC concert", 7, 1),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Backstage passes to a TAFKAL80ETC concert");
    expect(items[0].quality).toBe(3);
    expect(items[0].sellIn).toBe(6);
  });

  it("increase quality of Backstage passes to a TAFKAL80ETC concert by 3 when sell in is less than 5 days", () => {
    const gildedRose = new GildedRose([
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 1),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Backstage passes to a TAFKAL80ETC concert");
    expect(items[0].quality).toBe(4);
    expect(items[0].sellIn).toBe(4);
  });

  it("quality of Backstage passes to a TAFKAL80ETC concert goes to Zero after concert is over", () => {
    const gildedRose = new GildedRose([
      new Item("Backstage passes to a TAFKAL80ETC concert", 0, 0),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Backstage passes to a TAFKAL80ETC concert");
    expect(items[0].quality).toBe(0);
    expect(items[0].sellIn).toBe(-1);
  });

  it("decrease the quality and sellin by 1 for Elixir of the Mongoose", () => {
    const gildedRose = new GildedRose([
      new Item("Elixir of the Mongoose", 5, 7),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Elixir of the Mongoose");
    expect(items[0].sellIn).toBe(4);
    expect(items[0].quality).toBe(6);
  });

  it("decrease quality and quantity by 1 for Conjured Mana Cake", () => {
    const gildedRose = new GildedRose([new Item("Conjured Mana Cake", 3, 6)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Conjured Mana Cake");
    expect(items[0].sellIn).toBe(2);
    expect(items[0].quality).toBe(5);
  });

  it("decrease quality and quantity by 1 for Conjured Mana Cake when the sellin date is 0", () => {
    const gildedRose = new GildedRose([new Item("Conjured Mana Cake", 0, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("Conjured Mana Cake");
    expect(items[0].sellIn).toBe(-1);
    expect(items[0].quality).toBe(0);
  });
});
