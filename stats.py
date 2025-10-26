def get_word_count(some_text):
    return len(some_text.split())

def get_letter_counts(some_text):
    counts = {}
    for c in some_text:
        lc = c.lower()
        if not c.isalpha():
            continue
        if lc in counts:
            counts[lc] += 1
        else:
            counts[lc] = 1
    return counts

def sort_pred(items):
    return items["num"]

def sort_letters(letter_counts):
    sorted = []
    for k in letter_counts:
        sorted.append({"char":k, "num": letter_counts[k]})
    sorted.sort(reverse = True, key=sort_pred)
    return sorted