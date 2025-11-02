try:
    from .strings import get_hamming_distance, get_dna_complement
except Exception:
    # Fallback: load the sibling strings.py directly so the script can be run
    # both as a package and as a standalone script.
    import importlib.util
    import pathlib
    strings_path = pathlib.Path(__file__).resolve().parent / "strings.py"
    spec = importlib.util.spec_from_file_location("strings", str(strings_path))
    strings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(strings)
    get_hamming_distance = strings.get_hamming_distance
    get_dna_complement = strings.get_dna_complement

def main():
    while True:
        print("\nMenu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            result = get_hamming_distance(dna1, dna2)
            print("Hamming Distance:", result)

        elif choice == "2":
            dna = input("Enter DNA string: ")
            result = get_dna_complement(dna)
            print("DNA Complement:", result)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()