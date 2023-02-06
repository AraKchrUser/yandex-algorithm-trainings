import sys
words = {}
for word in sys.stdin.read().split():
    if word not in words:
        words[word] = 0
    else:
        words[word] += 1
    print(words[word], end=' ')
