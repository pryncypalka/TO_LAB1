from tkinter import ttk

class TkApp:
    def __init__(self, root, collection, exchange):
        self.currencies_dict = collection.get_dict()
        self.currency_names = list(self.currencies_dict.keys())
        self.exchange = exchange
        self.root = root
        self.collection = collection
        root.title("Kalkulator Walutowy")

        self.label_currency1 = ttk.Label(root, text="Waluta 1:")
        self.label_currency1.grid(row=0, column=0)
        self.currency1 = ttk.Combobox(root, values=self.currency_names)
        self.currency1["state"] = "readonly"
        self.currency1.grid(row=0, column=1)
        self.currency1.set("PLN")
        self.currency1.bind("<<ComboboxSelected>>", self.update_conversion)


        self.label_currency2 = ttk.Label(root, text="Waluta 2:")
        self.label_currency2.grid(row=1, column=0)
        self.currency2 = ttk.Combobox(root, values=self.currency_names)
        self.currency2["state"] = "readonly"
        self.currency2.grid(row=1, column=1)
        self.currency2.set("USD")
        self.currency2.bind("<<ComboboxSelected>>", self.update_conversion)


        self.label_amount1 = ttk.Label(root, text="Ilość waluty 1:")
        self.label_amount1.grid(row=2, column=0)
        self.amount1 = ttk.Entry(root)
        self.amount1.grid(row=2, column=1)
        self.amount1.insert(0, "1")
        self.amount1.bind("<KeyRelease>", self.update_conversion)

        # Pole do wyświetlania ilości waluty 2
        self.label_result = ttk.Label(root, text="Wynik:")
        self.label_result.grid(row=3, column=0)
        self.result = ttk.Label(root, text="")
        self.result.grid(row=3, column=1)

    def update_conversion(self, event):
        try:
            amount1_str = self.amount1.get()
            if amount1_str and float(amount1_str) > 0:  # Sprawdź, czy wpisano liczbę dodatnią
                amount1 = float(amount1_str)
                currency1 = self.currency1.get()
                currency2 = self.currency2.get()
                self.exchange.set_W1(self.currencies_dict[currency1])
                self.exchange.set_W2(self.currencies_dict[currency2])
                self.exchange.set_amount(amount1)

                self.result.config(text=f"{amount1_str} {currency1} = {self.exchange.result()} {currency2}")
            else:
                self.result.config(text="Podaj poprawną ilość waluty")
        except ValueError:
            self.result.config(text="Błąd - wprowadź liczbę")