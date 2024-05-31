import xmltodict

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except Exception as e:
        print(f"Błąd wczytywania pliku XML: {e}")
        raise