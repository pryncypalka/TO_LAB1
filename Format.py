import xml.etree.ElementTree as ET

class Format:
    def __init__(self):
        self._byte = None

    @property
    def byte(self):
        return self._byte

    @byte.setter
    def byte(self, value):
        self._byte = value

    def get_collection(self):
        root = ET.fromstring(self._byte)
        print(ET.tostring(root, encoding="unicode"))


