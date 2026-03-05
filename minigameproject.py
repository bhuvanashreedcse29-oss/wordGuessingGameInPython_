import random
def word_game():
    words = [
        "python", "java", "loops", "string", "tuple", "dictionary",
        "football", "cricket", "chess", "guitar", "piano", "mountain",
        "river", "ocean", "sunflower", "rose", "computer", "keyboard",
        "science", "history", "mathematics", "galaxy", "planet", "star"
    ]

    hints = (
        "Popular programming language with snakes",
        "Programming language used for OOP",
        "Used to repeat tasks",
        "Sequence of characters",
        "Immutable ordered collection",
        "Key-value storage",
        "Sport played with a ball and goalposts",
        "Sport with bat and ball",
        "Strategic board game",
        "Musical instrument with strings",
        "Musical instrument with keys",
        "Large natural elevation",
        "Flowing body of water",
        "Huge body of salt water",
        "Bright yellow flower",
        "Beautiful red flower",
        "Electronic device",
        "Input device with keys",
        "Study of the natural world",
        "Study of past events",
        "Numbers and formulas",
        "Massive system of stars",
        "Celestial body orbiting a star",
        "Twinkling object in the night sky"
    )

    word_hints = {words[i]: hints[i] for i in range(len(words))}
    chosen_word = random.choice(words)
    hint = word_hints[chosen_word]

    print("Welcome to the Word Guessing Game!")
    print("Hint:", hint)

    attempts = 6
    score = 0
    guessed_correctly = False

    while attempts > 0:
        guess = input("Enter your guess: ").lower()

        if guess == chosen_word:
            print("Correct! You win!")
            score += attempts * 10
            guessed_correctly = True
            break
        else:
            print("Wrong guess!")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    if not guessed_correctly:
        print("Game Over!")
    print("The word was:", chosen_word)
    print("Your final score:", score)


word_game()
