from decimal import Decimal, ROUND_HALF_UP
class Exchange:
    def __init__(self):
        self.w1 = None  # Pierwsza waluta
        self.w2 = None  # Druga waluta
        self.amount = 0.0  # Ilość waluty do wymiany

    def set_W1(self, currency):
        # Ustaw pierwszą walutę
        self.w1 = currency

    def set_W2(self, currency):
        # Ustaw drugą walutę
        self.w2 = currency

    def set_amount(self, amount):
        # Ustaw ilość waluty do wymiany
        self.amount = amount

    def result(self):
        # Oblicz wynik wymiany walut
        if self.w1 and self.w2:
            self.amount = Decimal(str(self.amount))
            exchange_rate1 = Decimal(str(self.w1.get_exchange_rate()))
            exchange_rate2 = Decimal(str(self.w2.get_exchange_rate()))
            conversion_factor1 = Decimal(str(self.w1.get_conversion_factor()))
            conversion_factor2 = Decimal(str(self.w2.get_conversion_factor()))

            try:
                result = (self.amount * exchange_rate1 / conversion_factor1 /
                          (exchange_rate2 / conversion_factor2))

                formatted_result = result.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
                return formatted_result
            except:
                return "Wynik przekracza zakres dopuszczalnych wartości"



