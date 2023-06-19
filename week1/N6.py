import random


def play_hangman():
    words = ["apple", "banana", "orange", "kiwi", "grape", "lemon"]

    word = random.choice(words)

    attempts = 6

    guessed_letters = []

    hidden_word = "_" * len(word)

    while attempts > 0 and hidden_word != word:
        print("\n" + hidden_word)
        print("Осталось попыток:", attempts)

        guess = input("Введите букву: ").lower()

        if len(guess) != 1:
            print("введите только одну букву")
            continue

        if guess in guessed_letters:
            print("вы уже отгадали жту букву")
            continue

        guessed_letters.append(guess)

        if guess in word:
            hidden_word = reveal_letters(word, hidden_word, guess)
            print("верно")
        else:
            attempts -= 1
            print("неправильно")

    if hidden_word == word:
        print("\n вы победили, правильное слово - ", word)
    else:
        print("\n вы проиграли, загаднное слово было - ", word)


def reveal_letters(word, hidden_word, letter):
    new_hidden_word = ""
    for i in range(len(word)):
        if word[i] == letter:
            new_hidden_word += letter
        else:
            new_hidden_word += hidden_word[i]
    return new_hidden_word


play_hangman()
