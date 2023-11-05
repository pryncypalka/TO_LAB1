import DataProvider
import Format
import Exchange
import tkinter as tk
import TkApp

class ProgramRunner:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProgramRunner, cls).__new__(cls)
        return cls._instance

    def run_app(self):
        dp1 = DataProvider.DataProvider()
        dp1.set_url("https://www.nbp.pl/kursy/xml/lasta.xml")
        byte = dp1.get_data()
        if byte is None:
            return
        format1 = Format.Format(byte)
        collection1 = format1.get_collection()
        exchange1 = Exchange.Exchange()
        root = tk.Tk()
        TkApp.TkApp(root, collection1, exchange1)
        root.mainloop()






