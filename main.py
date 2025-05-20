import random
import os


fail_table = {
    1: """
_____________
|
|
|
|
|
|
|
|____________
|____________|
""",
    2: """
_____________
|       |
|       |
|
|
|
|
|
|____________
|____________|
""",
    3: """
_____________
|       |
|       |_
|       |_|
|       
|
|
|
|____________
|____________|
"""
,
    4: """
_____________
|       |
|       |_
|       |_|
|        |
|        |
|        
|
|____________
|____________|
"""
,
    5: """
_____________
|       |
|       |_
|       |_|
|        |\\
|        |
|        
|
|____________
|____________|
""",
    6: """
_____________
|       |
|       |_
|       |_|
|       /|\\
|        |
|        
|
|____________
|____________|
""",
    7: """
_____________
|       |
|       |_
|       |_|
|       /|\\
|        |
|       /
|
|____________
|____________|
""",
    8: """
_____________
|       |
|       |_
|       |_|
|       /|\\
|        |
|       / \\
|
|____________
|____________|
"""
}



words = [
    "собака",  
    "кот",  
    "кодинг",  
    "нееросети",  
    "бобр",  
    "программирование",  
    "алгоритм",  
    "нейросеть",  
    "питон",  
    "лиса",  
    "медведь",  
    "тигр",  
    "данные",  
    "обучение",  
    "интеллект",  
    "машина",  
    "обучение",  
    "заяц",  
    "волк",  
    "белка"  
]  


fails = 1
hidden_word = [elem for elem in random.choice(words)]

printing_words = ["?" for empty in hidden_word]

def update_scene():
    os.system("clear")
    print(fail_table[fails])
    format_printing = ""
    for wrd in printing_words: format_printing += wrd
    print("Слово: ", format_printing)

print(f"\nЯ загадал слово из {len(hidden_word)} букв, отгадай его\n")
print("ВВОДИТЕ ТОЛЬКО ПО ОДНОЙ БУКВЕ")

if __name__ == "__main__":
    print(fail_table[fails])

    while fails != 8:
        if hidden_word == ["?" for empty in range(len(hidden_word))]: exit("Ты победил!")

        get_word = input("\n>>> ").lower()
        get_word = get_word[0] if len(get_word) > 1 else get_word

        if get_word in hidden_word:
            for cwd in range(hidden_word.count(get_word)):
                word_index = hidden_word.index(get_word)
                printing_words[word_index] = hidden_word[word_index]
                hidden_word[word_index] = "?"
    

        else:
            fails += 1

        update_scene()
    
print("\nУвы, проигрыш")
