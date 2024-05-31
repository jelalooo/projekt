import argparse
import json
import yaml
import xmltodict

def parse_args():
    parser = argparse.ArgumentParser(description="Konwersja plików między formatami .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", type=str, help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", type=str, help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd wczytywania pliku JSON: {e}")
        raise

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd wczytywania pliku YAML: {e}")
        raise

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except Exception as e:
        print(f"Błąd wczytywania pliku XML: {e}")
        raise

def save_xml(data, file_path):
    with open(file_path, 'w') as file:
        xml_content = xmltodict.unparse(data, pretty=True)
        file.write(xml_content)

def convert_file(input_file, output_file):
    input_ext = input_file.split('.')[-1].lower()
    output_ext = output_file.split('.')[-1].lower()

    load_func = {
        'json': load_json,
        'yml': load_yaml,
        'yaml': load_yaml,
        'xml': load_xml
    }.get(input_ext)

    save_func = {
        'json': save_json,
        'yml': save_yaml,
        'yaml': save_yaml,
        'xml': save_xml
    }.get(output_ext)

    if not load_func or not save_func:
        print("Nieobsługiwany format pliku.")
        return

    data = load_func(input_file)
    save_func(data, output_file)

if __name__ == "__main__":
    args = parse_args()
    convert_file(args.input_file, args.output_file)
    
