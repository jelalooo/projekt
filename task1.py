import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Konwersja plików między formatami .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", type=str, help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", type=str, help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
