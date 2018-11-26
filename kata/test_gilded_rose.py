# -*- coding: utf-8 -*-
# test 10
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # 0
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    # 1
    def test_twise_fast(self):
        items = [Item("new_item", -0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(48, items[0].quality)
    # 2
    def test_not_negative(self):
        items = [Item("new_item", -0, -50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-50, items[0].quality)

    # 3
    def test_Aged_Brie(self):
        items = [Item("Aged Brie", -0, 10),
            Item("Aged Brie", -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(12, items[0].quality)

    # 4
    def test_more_that_50(self):
        items = [Item("new_item", 1, 100)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(True, items[0].quality != 100)
    
    # 5
    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].quality)

    # 6
    def test_Backstage_passes_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].quality)

    # 7
    def test_Backstage_passes_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(12, items[0].quality)

    # 8
    def test_conjured_1(self):
        items = [Item("Conjured III", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    # 9
    def test_conjured_2(self):
        items = [Item("Conjured III", -0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].quality)

if __name__ == '__main__':
    unittest.main()