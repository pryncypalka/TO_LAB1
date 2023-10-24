import DataProvider
import Format
import Collection as coll
import Currency as Curr
import TkApp as TA


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
        dp1.url = "https://www.nbp.pl/kursy/xml/lasta.xml"

        format1 = Format.Format(dp1.get_data())
        collection1 = format1.get_collection()





