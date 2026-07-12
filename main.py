def count_vowels(text):
    text = text.lower()
    vowels = text.count('a') + text.count('u') + text.count('o') + text.count('i') + text.count('e')
    return vowels

word = "HELLO"
print(count_vowels(word))
print(count_vowels("AdrianA"))