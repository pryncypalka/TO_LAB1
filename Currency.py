
class Currency:
    def __init__(self, name, conversion_factor, code, exchange_rate):
        self._name = name
        self._conversion_factor = conversion_factor
        self._code = code
        self._exchange_rate = exchange_rate

    def get_name(self):
        return self._name

    def get_conversion_factor(self):
        return self._conversion_factor

    def get_code(self):
        return self._code

    def get_exchange_rate(self):
        return self._exchange_rate

    def set_name(self, name):
        self._name = name

    def set_conversion_factor(self, conversion_factor):
        self._conversion_factor = conversion_factor

    def set_code(self, code):
        self._code = code

    def set_exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    def equals(self, other_currency):
        if isinstance(other_currency, Currency) and hasattr(other_currency, "get_code"):
            return self._code == other_currency.get_code()
        else:
            return False
