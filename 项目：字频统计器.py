def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
import re

def clean_words(text):
    return re.findall(r"[a-z]+", text.lower())
def count_words(words):
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts
def top_n(counts, n):
    top_n = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return top_n[:n]
def save_report(path, rows):
    with open(path, 'w', encoding='utf-8') as f:
        for word, count in rows:
            f.write(f"{word:<16}{count}\n")


if __name__ == "__main__":

    text = read_text('Wonderland.txt')
    words = clean_words(text)
    counts = count_words(words)
    rows = top_n(counts, 10)
    save_report("report.txt", rows)
    print(read_text('report.txt'))
