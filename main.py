import time

import pyfirmata

print("Creating configs")
pin = 13
port = 'COM4'
print("Connecting with arduino")
board = pyfirmata.Arduino(port)

print("Digite a frase a ser traduzida em morse: ")
word = input()

dialect = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
    "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----"
}


def do_dot():
    board.digital[pin].write(1)
    time.sleep(0.5)
    board.digital[pin].write(0)
    time.sleep(0.8)


def do_dash():
    board.digital[pin].write(1)
    time.sleep(1)
    board.digital[pin].write(0)
    time.sleep(0.8)


def do_space():
    time.sleep(2)


def do_morse(selectedWord):
    for char in selectedWord:
        print(char)
        if char != ' ':
            for code in dialect[char]:
                if code == ".":
                    print(".")
                    do_dot()
                else:
                    print("-")
                    do_dash()
        else:
            print("space")
            do_space()

        print("\n")


while True:
    print("Starting morse")
    do_morse(word.lower())
    time.sleep(3)
