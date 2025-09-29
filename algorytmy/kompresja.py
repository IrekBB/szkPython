text = "010111010011111001001100"

cipher = {'0': 'n', '101': 'i', '100': 'm', '111': 'z', '1101': 'e', '1100': 'd', '1001': 'a', '00': ' '}


def decrypt(cipher, text): #brak obsługi błedów, jeżeli zmienna text skonstruowana jest niepoprawnie.
    res = ""
    while text:
        for k in cipher:
            if text.startswith(k):
                res += cipher[k]
                text = text[len(k):]
    return res


to_code = "zdam"


def encrypt(cipher, text):
    res = ""
    for char in text:
        if char in cipher.values():
            for k, v in cipher.items():
                if v == char:
                    res += k
        else:
            res += "-"
    return res


print(decrypt(cipher, text))
print(encrypt(cipher, to_code))
