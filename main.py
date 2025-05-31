from content import fail_table, words
import random
import os


fails = 1
hidden_word = [elem for elem in random.choice(words)]

printing_words = ["?" for empty in hidden_word]

def update_scene():
    os.system("clear")
    print(fail_table[fails])
    format_printing = ""
    for wrd in printing_words: format_printing += wrd
    print("Слово: ", format_printing)


def check_words(word):
    if word in hidden_word:
        for cwd in range(hidden_word.count(word)):
            word_index = hidden_word.index(word)
            printing_words[word_index] = hidden_word[word_index]
            hidden_word[word_index] = "?"

    else:
        global fails
        fails += 1


print(f"\nЯ загадал слово из {len(hidden_word)} букв, отгадай его\n")
print("ВВОДИТЕ ТОЛЬКО ПО ОДНОЙ БУКВЕ")

if __name__ == "__main__":
    print(fail_table[fails])

    while fails != 8:
        if hidden_word == ["?" for empty in range(len(hidden_word))]: exit("Ты победил!")

        get_word = input("\n>>> ").lower()
        get_word = get_word[0] if len(get_word) > 1 else get_word

        check_words(get_word)
    
        update_scene()
    
print("\nУвы, проигрыш")
