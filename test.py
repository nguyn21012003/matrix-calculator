import random as rd
from random import randint


def main():
    n = get_level()
    a = generate_interger(n)
    print(a)


def get_level():
    while True:
        try:
            level = int(input("Input: "))
            if level in [1, 2, 3]:
                return level
        except EOFError:
            break


def generate_interger(level):
    if level == 1:
        wrong_answer = 0
        for i in range(10):
            x, y = randint(0, 9), randint(0, 9)
            result = x + y
            tries = 0
            while tries < 3:
                try:
                    print(f"{x} + {y} = ", end="")
                    answer = int(input())
                    try:
                        if answer == result:
                            wrong_answer = wrong_answer
                            tries = tries
                            break
                        else:
                            print("EEE")
                            tries += 1
                            if tries == 3:
                                wrong_answer += 1
                                print(f"{x} + {y} = {result}")
                            score = 10 - wrong_answer
                    except EOFError:
                        break
                except ValueError:
                    break
        return f"Score: {score} out of 10"


if __name__ == "__main__":
    main()
