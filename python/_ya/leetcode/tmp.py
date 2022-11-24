
from string import ascii_letters as alph

def alphabet_position(text):
    result = []
    for c in text.lower():
        print(c)
        print(c in alph)
        if c in alph:
            result.append(alph.index(c) + 1)
    print(result)
    return " ".join(result)

if __name__ == '__main__':
    alphabet_position(" tes.")