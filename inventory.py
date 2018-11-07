from cargo import Cargo
class Inventory(object):
    def __init__(self):
        self.inventory = []
    def add(self, item):
        self.inventory.append(item)
    def remove(self, item_name):
        for i in self.inventory:
            if item_name == i.name:
                self.inventory.remove(i)
                return i
