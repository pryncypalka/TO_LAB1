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
            exchange_rate1 = self.w1.get_exchange_rate()
            exchange_rate2 = self.w2.get_exchange_rate()
            return (self.amount * float(exchange_rate1)) / float(exchange_rate2)
        else:
            return 0.0