import requests


class DataProvider:
    def __init__(self):
        self._url = ""


    def get_url(self):
        return self._url

    def set_url(self, value):
        self._url = value



    def get_data(self):
        response = requests.get(self._url)

        if response.status_code == 200:
            xml_content = response.content


            return xml_content

        else:
            print("Błąd podczas pobierania pliku XML")