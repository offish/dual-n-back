import random
import string
import time
import os

from playsound import playsound


def letter() -> str:
    return list(string.ascii_lowercase)[random.randint(0, 25)]


def number() -> int:
    return random.randint(1, 9)


def grid(placement: int) -> str:
    size = 9
    grid = ""

    for i in range(size):
        if i + 1 == placement:
            grid += "[■]."
        else:
            grid += "[ ]."

    grid = grid.split(".")

    organized = ""
    number = 0

    for i in [i for i in grid if i]:
        number += 1

        organized += i + " "

        if number % 3 == 0 and not number == 9:
            organized += "\n"

    return organized


def check(previous: tuple, current: tuple, choice: int) -> bool:
    number = previous[0] == current[0]
    letter = previous[1] == current[1]
    both = True if number and letter else False
    is_correct = False

    if choice == 0 and not (number or letter or both):
        is_correct = True

    elif choice == 1 and number and not both:
        is_correct = True

    elif choice == 2 and letter and not both:
        is_correct = True

    elif choice == 3 and both:
        is_correct = True

    return is_correct


if __name__ == "__main__":
    rounds = 2 + int(input("How many rounds would you like to play? "))
    os.system("cls" if os.name == "nt" else "clear")

    correct = 0
    games = []

    for _ in range(rounds):
        _number = number()
        _grid = grid(_number)
        _letter = letter()
        game = (_number, _letter)

        games.append(game)
        print(_grid)

        playsound(f"sounds/{_letter}.mp3")

        if len(games) == 3:
            choice = int(input("0 for none, 1 placement, 2 for sound, 3 for both: "))
            is_correct = check(games[0], game, choice)

            if is_correct:
                print("Correct")
                correct += 1
            else:
                print("Incorrect")

            time.sleep(1)

            games.pop(0)

        else:
            time.sleep(3)

        os.system("cls" if os.name == "nt" else "clear")

    rounds -= 2
    print(
        f"Done. You played {rounds} rounds and got {correct} correct answers. Rate {round((correct / rounds) * 100, 2)}%"
    )
