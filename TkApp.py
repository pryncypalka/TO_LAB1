import tkinter as tk
import Collection as coll

from tkinter import ttk

class TkApp:
    def __init__(self, root):
        self.root = root
        root.title("Kalkulator Walutowy")

        self.label_currency1 = ttk.Label(root, text="Waluta 1:")
        self.label_currency1.grid(row=0, column=0)
        self.currency1 = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.currency1.grid(row=0, column=1)
        self.currency1.set("PLN")
        self.currency1.bind("<<ComboboxSelected>>", self.update_conversion)

        # Wybór drugiej waluty
        self.label_currency2 = ttk.Label(root, text="Waluta 2:")
        self.label_currency2.grid(row=1, column=0)
        self.currency2 = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.currency2.grid(row=1, column=1)
        self.currency2.set("USD")
        self.currency2.bind("<<ComboboxSelected>>", self.update_conversion)

        # Pole do wprowadzania ilości waluty 1
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

    def get_currency_names_from_collection(self):
        # Pobranie nazw walut z  class Collection
        currency_names = []
        for currency in self.collection.get_items():
            currency_names.append(currency.get_name())


    def update_conversion(self, event):
        # Aktualizacja wyświetlanego wyniku
        try:
            amount1 = float(self.amount1.get())
            currency1 = self.currency1.get()
            currency2 = self.currency2.get()
            exchange_rate1 = self.exchange_rates.get(currency1, 1)
            exchange_rate2 = self.exchange_rates.get(currency2, 1)
            converted_amount = amount1 * exchange_rate1 / exchange_rate2
            self.result.config(text=f"{amount1} {currency1} = {converted_amount:.2f} {currency2}")
        except ValueError:
            self.result.config(text="Błąd")