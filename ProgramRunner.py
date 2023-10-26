import DataProvider
import Format
import Exchange
import tkinter as tk
import TkApp

class ProgramRunner:
    _instance = None
    def __init__(self):
        if not self.initialized:
            self.initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProgramRunner, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance




    def run_app(self):
        dp1 = DataProvider.DataProvider()
        dp1.set_url("https://www.nbp.pl/kursy/xml/lasta.xml")
        format1 = Format.Format(dp1.get_data())
        collection1 = format1.get_collection()
        exchange1 = Exchange.Exchange()
        root = tk.Tk()
        TkApp.TkApp(root, collection1, exchange1)
        root.mainloop()






