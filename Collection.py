

class Collection:
    def __init__(self):
        self._col = []

    def get_item(self, currency):
        for item in self._col:
            if item.equals(currency):
                return item
        return None

    def remove_item(self, currency):
        for item in self._col:
            if item.equals(currency):
                self._col.remove(item)
                return True
        return False 

    def add_item(self, currency):
        if not self.get_item(currency):
            self._col.append(currency)

    def set_item(self, currency):
        if self.get_item(currency):
            self.remove_item(currency)
        self.add_item(currency)

