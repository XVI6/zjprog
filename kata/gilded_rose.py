# -*- coding: utf-8 -*-
# reek
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)
    
    def my_if_1(self,item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1
            # added
            if "conjured" in item.name.lower():
                item.quality = item.quality - 1
    
    def my_else_1(self,item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.my_else_1_1(item)
                

    def my_else_1_1(self,item):
        if item.sell_in < 11:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1
    
    def my_diff_1(self,item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.my_diff_1_1(item)
            
    
    def my_diff_1_1(self,item):
        if item.name != "Aged Brie":
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.my_diff_1_1_1(item)
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < 50:
                item.quality = item.quality + 1

    def my_diff_1_1_1(self,item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1

    def update_item(self,item):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            self.my_if_1(item)
        else:
            self.my_else_1(item)
        self.my_diff_1(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)