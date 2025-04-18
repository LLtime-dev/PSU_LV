try:
    with open("song.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Datoteka 'song.txt' nije pronađena.")
    exit()

import re
words = re.findall(r'\b\w+\b', content.lower())

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

unique_words = [word for word, count in word_count.items() if count == 1]

print(f"Broj riječi koje se pojavljuju samo jednom: {len(unique_words)}")
print("Riječi koje se pojavljuju samo jednom:")
for word in unique_words:
    print(word)