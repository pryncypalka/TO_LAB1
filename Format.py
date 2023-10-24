import xml.etree.ElementTree as ET
import Collection as Coll
import Currency as Curr


class Format:
    def __init__(self, byte=None):
        self._byte = byte

    def set_byte(self, value):
        self._byte = value

    def get_collection(self):
        root = ET.fromstring(self._byte)
        col1 = Coll.Collection()
        for pozycja in root.findall('.//pozycja'):
            name = pozycja.find('nazwa_waluty').text
            conversion_factor = pozycja.find('przelicznik').text
            code = pozycja.find('kod_waluty').text
            exchange_rate = pozycja.find('kurs_sredni').text

            col1.add_item(Curr.Currency(name, conversion_factor, code, exchange_rate))

        return col1
