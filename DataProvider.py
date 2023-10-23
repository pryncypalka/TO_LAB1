import requests
import xml.etree.ElementTree as ET

class DataProvider:
    def __init__(self):
        self._url = "https://www.nbp.pl/kursy/xml/lasta.xml"

    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, value):
        self._url = value


    @property
    def data(self):
        response = requests.get(self._url)

        # Sprawdź, czy pobranie zakończyło się sukcesem
        if response.status_code == 200:
            # Parsowanie zawartości jako XML
            xml_content = response.content
            root = ET.fromstring(xml_content)

            # Teraz masz dostęp do drzewa XML i możesz wykonywać operacje na nim
            # Na przykład, możesz wydrukować zawartość:
            print(ET.tostring(root, encoding="unicode"))

            # Teraz możesz przeszukiwać i analizować drzewo XML za pomocą modułu ElementTree
        else:
            print("Błąd podczas pobierania pliku XML")