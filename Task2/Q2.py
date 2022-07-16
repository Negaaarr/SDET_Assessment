from collections import OrderedDict

def find_max_letter_count(word):
    counts = OrderedDict()
    word = word.lower()
    for char in word:
        if char not in counts:
            counts[char] = word.count(char)
    max_letter_list = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return max_letter_list[0][0]


if __name__:
    word = input("Input: ")
    max_count = find_max_letter_count(word)
    print("Output: " + max_count)

