import sys
text = sys.stdin.read().split()
words_count = {}
for word in text:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1
max_word_count = 0
for word in words_count:
    if words_count[word] > max_word_count:
        max_word_count = words_count[word]
max_words = []
for word in words_count:
    if words_count[word] == max_word_count:
        max_words.append(word)
print(sorted(max_words)[0])
