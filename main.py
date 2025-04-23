from stats import get_word_count, count_characters

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def print_report(fp, wc, dct: dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for k,v in dct.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bp = sys.argv[1]

    text_f = get_book_text(bp)

    wc_f = get_word_count(text_f)

    count_dct_f = count_characters(text_f)

    print_report(bp, wc_f, count_dct_f)
if __name__ == "__main__":
    main()