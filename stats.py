from collections import Counter

def get_word_count(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    lst = list(text)
    count = Counter(lst)
    return count