# define coding dict
morseEncode = {
    'a': '.-', 'b': '-...', 'c': '-.-.', ' ': '  ',
    'd': '-..', 'e': '.', 'f': '..-.', '': '',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
}
# swap coding table for decoding dict
morseDecode = {val: key for key, val in morseEncode.items()}
morseDecode.update({'_': ' '})

# define coding function
def morseCode(string, decode=False):
    string = string.lower()
    output = ""
    if not decode:  # then encode
        for char in string:
            output += morseEncode.get(char, '')  # print '*' for unexpected characters
            if char != ' ': output += ' '
    else:
        string = string.replace('  ', ' _ ')
        for char in string.split(' '):
            output += morseDecode.get(char, '')  # print '*' for unexpected codes
    return output

# test
string = "A to jest alfabet Morsa"
coded = morseCode(string)
print("Coded:", coded)
decoded = morseCode(coded, decode=True)
print("Decoded:", decoded)

# This code is contributed by Pixel
