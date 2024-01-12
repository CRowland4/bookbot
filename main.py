from collections import defaultdict


def main() -> None:
    with open("books/frankenstein.txt", "r") as book:
        contents = book.read()

    print("--- Begin report of books/frankenstein.txt --")
    print(f"{word_count(contents)} words found in the document")
    print()

    print(book_report(contents))
    return


def word_count(book: str) -> int:
    return len(book.split())


def character_counts(book: str) -> dict[str, int]:
    character_counts = defaultdict(int)
    for char in book:
        character_counts[char.lower()] += 1

    return character_counts


def book_report(book: str) -> str:
    char_frequencies = character_counts(book)
    sorted_characters_by_frequency = sorted(list(char_frequencies.keys()), key=lambda char: char_frequencies[char], reverse=True)

    report = ""
    for char in sorted_characters_by_frequency:
        if char.isalpha():
            report += f"The '{char}' character was found {char_frequencies[char]} times\n"

    return report


if __name__ == "__main__":
    main()
