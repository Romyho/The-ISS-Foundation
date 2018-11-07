from cargo import Cargo
class Inventory(object):
    def __init__(self):
        self.inventory = []
    def add(self, item):
        self.inventory.append(item)
    def remove(self, item):
        self.inventory.remove(item)
