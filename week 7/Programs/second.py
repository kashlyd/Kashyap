def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))
def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))
def letters_in_either_not_both(word1, word2):
    return sorted((set(word1.lower()) | set(word2.lower())) - (set(word1.lower()) & set(word2.lower())))
try:
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    result_either = letters_in_either(word1, word2)
    print(f"Letters in either word: {result_either}")

    result_both = letters_in_both(word1, word2)
    print(f"Letters in both words: {result_both}")

    result_either_not_both = letters_in_either_not_both(word1, word2)
    print(f"Letters in either, but not in both: {result_either_not_both}")

except Exception as e:
    print(f"An error occurred: {e}")
