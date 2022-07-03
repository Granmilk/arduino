import time

import pyfirmata

print("Creating configs")
pin = 10
port = 'COM4'
print("Connecting with arduino")
board = pyfirmata.Arduino(port)

dot_interval = 0.1
dash_interval = 0.5
space_interval = 2
enable = 1
disable = 0
end_interval = 0.8
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
    board.digital[pin].write(enable)
    time.sleep(dot_interval)
    board.digital[pin].write(disable)
    time.sleep(end_interval)


def do_dash():
    board.digital[pin].write(enable)
    time.sleep(dash_interval)
    board.digital[pin].write(disable)
    time.sleep(end_interval)


def do_space():
    time.sleep(space_interval)


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
