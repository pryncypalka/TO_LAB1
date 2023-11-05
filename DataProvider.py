import requests
import time

class DataProvider:
    def __init__(self):
        self._url = ""

    def set_url(self, value):
        self._url = value



    def get_data(self):
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                response = requests.get(self._url)
                if response.status_code == 200:
                    xml_content = response.content
                    return xml_content
            except Exception as e:
                print(f"Błąd podczas próby {attempt}/{max_attempts} pobierania danych: {e}")

            if attempt < max_attempts:
                time.sleep(2)  # Czekaj 2 sekundy przed kolejną próbą

        print("Nie udało się pobrać danych po maksymalnej liczbie prób.")
        return None