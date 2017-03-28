import string
import operator

text = '''Remove the item at the given position in the list, and return it. If no index is specified, a.pop()
 removes and returns the last item in the list. (The square brackets around the i in the method signature denote
 that the parameter is optional, not that you should type square brackets at that position.
 You will see this notation frequently in the Python Library Reference.)'''


raw_words = text.split()
words = [word.strip(string.punctuation) for word in text.split()]
words_dict = {}

for word in words:
    words[words.index(word)] = word.lower()

for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

sorted_dict = sorted(words_dict.items(), key=operator.itemgetter(1))
sorted_dict.reverse()
print("Word \"{}\" is the most used one, it was used {} times".format(sorted_dict[0][0], sorted_dict[0][1]))
