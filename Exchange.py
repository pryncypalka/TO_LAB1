
class Exchange:
    def __init__(self):
        self._w1 = None
        self._w2 = None  
        self.amount = 0.0  

    def set_W1(self, currency):
        self._w1 = currency

    def set_W2(self, currency):
        self._w2 = currency

    def set_amount(self, amount):
        self.amount = amount

    def result(self):
        if self._w1 and self._w2:
            self.amount = self.amount
            exchange_rate1 = self._w1.get_exchange_rate()
            exchange_rate2 = self._w2.get_exchange_rate()
            conversion_factor1 = self._w1.get_conversion_factor()
            conversion_factor2 = self._w2.get_conversion_factor()

            try:
                result = (self.amount * exchange_rate1 / conversion_factor1 /
                          (exchange_rate2 / conversion_factor2))

                formatted_result = "{:.2f}".format(result)
                return formatted_result
            except:
                return "Wynik przekracza zakres dopuszczalnych wartości"



