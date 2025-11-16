import os
import sys
# Ensure the project root (parent of src) is on sys.path so "src" can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

def get_user_dna_list():
    print("Enter DNA strings as comma-separated characters (e.g., A,T,G,G,C)")

    n = int(input("How many DNA strings? "))

    dna_lists = []
    for i in range(n):
        raw = input(f"Enter DNA string #{i+1}: ")
        dna_lists.append(raw.replace(" ", "").split(","))

    return dna_lists


def main():
    while True:
        print("\nMENU")
        print("1 - Get p-distance matrix")
        print("2 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            dna_lists = get_user_dna_list()
            matrix = get_p_distance_matrix(dna_lists)

            print("\nP-Distance Matrix:")
            for row in matrix:
                print(" ".join(f"{value:.5f}" for value in row))

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()